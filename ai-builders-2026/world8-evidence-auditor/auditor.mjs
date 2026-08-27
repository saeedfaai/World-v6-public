const EPS = 1e-12;

export function clamp01(x) {
  return Math.min(1, Math.max(0, Number(x)));
}

export function mulberry32(seed = 8) {
  let a = seed >>> 0;
  return function rng() {
    a |= 0;
    a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function asMs(value) {
  const t = Date.parse(value);
  return Number.isFinite(t) ? t : NaN;
}

function hasAnyKey(row, keys) {
  return keys.filter((k) => Object.prototype.hasOwnProperty.call(row, k));
}

export function validateContracts(rows) {
  const errors = [];
  const warnings = [];
  const lifecycleCounts = {};
  const prohibited = [
    'order', 'order_id', 'execution_id', 'execute', 'quantity',
    'position_size', 'limit_price', 'market_order', 'broker_order_id'
  ];

  if (!Array.isArray(rows)) {
    return {
      status: 'FAIL',
      total: 0,
      errors: [{ code: 'DATASET_NOT_ARRAY', message: 'Input must be a JSON array.' }],
      warnings,
      lifecycle_counts: {},
    };
  }

  rows.forEach((row, index) => {
    const id = row?.contract_id ?? `row-${index}`;
    if (!row || typeof row !== 'object' || Array.isArray(row)) {
      errors.push({ index, contract_id: id, code: 'ROW_NOT_OBJECT', message: 'Contract must be an object.' });
      return;
    }

    const required = [
      'contract_id', 'issued_at', 'data_cutoff_at', 'valid_from', 'resolved_at',
      'lifecycle', 'raw_probability', 'candidate_probability', 'resolved_target'
    ];
    for (const key of required) {
      if (row[key] === undefined || row[key] === null || row[key] === '') {
        errors.push({ index, contract_id: id, code: 'MISSING_FIELD', field: key, message: `Missing required field: ${key}` });
      }
    }

    const cutoff = asMs(row.data_cutoff_at);
    const issued = asMs(row.issued_at);
    const valid = asMs(row.valid_from);
    const resolved = asMs(row.resolved_at);

    if (![cutoff, issued, valid, resolved].every(Number.isFinite)) {
      errors.push({ index, contract_id: id, code: 'INVALID_TIMESTAMP', message: 'One or more timestamps are invalid.' });
    } else {
      if (cutoff > issued) {
        errors.push({ index, contract_id: id, code: 'LOOKAHEAD_DATA_CUTOFF', message: 'data_cutoff_at is after issued_at.' });
      }
      if (issued > valid) {
        errors.push({ index, contract_id: id, code: 'VALIDITY_BEFORE_ISSUE', message: 'valid_from is before issued_at.' });
      }
      if (valid >= resolved) {
        errors.push({ index, contract_id: id, code: 'INVALID_RESOLUTION_ORDER', message: 'resolved_at must be after valid_from.' });
      }
    }

    for (const key of ['raw_probability', 'candidate_probability']) {
      const p = Number(row[key]);
      if (!Number.isFinite(p) || p < 0 || p > 1) {
        errors.push({ index, contract_id: id, code: 'INVALID_PROBABILITY', field: key, value: row[key], message: `${key} must be in [0,1].` });
      }
    }

    const y = Number(row.resolved_target);
    if (!(y === 0 || y === 1)) {
      errors.push({ index, contract_id: id, code: 'INVALID_TARGET', value: row.resolved_target, message: 'resolved_target must be 0 or 1.' });
    }

    const lifecycle = String(row.lifecycle ?? 'UNKNOWN').toUpperCase();
    lifecycleCounts[lifecycle] = (lifecycleCounts[lifecycle] || 0) + 1;
    if (lifecycle !== 'RESOLVED') {
      warnings.push({ index, contract_id: id, code: 'NON_RESOLVED_CONTRACT', value: lifecycle, message: 'This evaluator expects terminal RESOLVED contracts for scoring.' });
    }

    const leaked = hasAnyKey(row, prohibited);
    if (leaked.length) {
      errors.push({ index, contract_id: id, code: 'FORECAST_DECISION_ORDER_CONFLATION', fields: leaked, message: `Forecast object contains downstream execution/decision fields: ${leaked.join(', ')}` });
    }

    if (!row.strategy_version) {
      warnings.push({ index, contract_id: id, code: 'MISSING_STRATEGY_VERSION', message: 'strategy_version is recommended for reproducibility.' });
    }
    if (!row.snapshot_hash) {
      warnings.push({ index, contract_id: id, code: 'MISSING_SNAPSHOT_HASH', message: 'snapshot_hash is recommended for provenance.' });
    }
  });

  return {
    status: errors.length ? 'FAIL' : 'PASS',
    total: rows.length,
    errors,
    warnings,
    lifecycle_counts: lifecycleCounts,
  };
}

export function brierScore(rows, probabilityKey = 'candidate_probability', targetKey = 'resolved_target') {
  if (!rows.length) return NaN;
  return rows.reduce((sum, row) => {
    const p = Number(row[probabilityKey]);
    const y = Number(row[targetKey]);
    return sum + (p - y) ** 2;
  }, 0) / rows.length;
}

export function logLoss(rows, probabilityKey = 'candidate_probability', targetKey = 'resolved_target') {
  if (!rows.length) return NaN;
  return rows.reduce((sum, row) => {
    const p = Math.min(1 - EPS, Math.max(EPS, Number(row[probabilityKey])));
    const y = Number(row[targetKey]);
    return sum - (y * Math.log(p) + (1 - y) * Math.log(1 - p));
  }, 0) / rows.length;
}

export function ece(rows, probabilityKey = 'candidate_probability', targetKey = 'resolved_target', bins = 10) {
  if (!rows.length) return NaN;
  let total = 0;
  for (let b = 0; b < bins; b++) {
    const lo = b / bins;
    const hi = (b + 1) / bins;
    const subset = rows.filter((row) => {
      const p = Number(row[probabilityKey]);
      return b === bins - 1 ? p >= lo && p <= hi : p >= lo && p < hi;
    });
    if (!subset.length) continue;
    const avgP = subset.reduce((s, r) => s + Number(r[probabilityKey]), 0) / subset.length;
    const avgY = subset.reduce((s, r) => s + Number(r[targetKey]), 0) / subset.length;
    total += (subset.length / rows.length) * Math.abs(avgP - avgY);
  }
  return total;
}

export function pairedLossDifferences(rows, candidateKey = 'candidate_probability', baselineKey = 'raw_probability', targetKey = 'resolved_target') {
  return rows.map((row) => {
    const y = Number(row[targetKey]);
    const c = Number(row[candidateKey]);
    const b = Number(row[baselineKey]);
    return (c - y) ** 2 - (b - y) ** 2;
  });
}

export function mean(values) {
  return values.length ? values.reduce((a, b) => a + b, 0) / values.length : NaN;
}

export function quantile(sortedValues, q) {
  if (!sortedValues.length) return NaN;
  const pos = (sortedValues.length - 1) * q;
  const base = Math.floor(pos);
  const rest = pos - base;
  const next = sortedValues[base + 1];
  return next === undefined ? sortedValues[base] : sortedValues[base] + rest * (next - sortedValues[base]);
}

export function movingBlockBootstrap(differences, { replicates = 2000, blockSize = 24, seed = 8 } = {}) {
  const n = differences.length;
  if (!n) {
    return { estimate: NaN, lower: NaN, upper: NaN, replicates: 0, block_size: 0, seed };
  }
  const block = Math.max(1, Math.min(Number(blockSize) || 1, n));
  const reps = Math.max(100, Math.min(Number(replicates) || 2000, 20000));
  const rng = mulberry32(Number(seed) || 8);
  const boot = new Array(reps);

  for (let r = 0; r < reps; r++) {
    let total = 0;
    let count = 0;
    while (count < n) {
      const start = Math.floor(rng() * n);
      for (let j = 0; j < block && count < n; j++) {
        total += differences[(start + j) % n];
        count += 1;
      }
    }
    boot[r] = total / n;
  }

  boot.sort((a, b) => a - b);
  return {
    estimate: mean(differences),
    lower: quantile(boot, 0.025),
    upper: quantile(boot, 0.975),
    replicates: reps,
    block_size: block,
    seed: Number(seed) || 8,
  };
}

export function classifyClaim(ci) {
  if (![ci?.lower, ci?.upper].every(Number.isFinite)) return 'UNAVAILABLE';
  if (ci.upper < 0) return 'SUPPORTED_IMPROVEMENT';
  if (ci.lower > 0) return 'SUPPORTED_WORSENING';
  return 'INCONCLUSIVE';
}

export function humanClaim(classification, ci) {
  const delta = Number(ci.estimate);
  const fmt = (x) => Number.isFinite(x) ? x.toFixed(6) : 'n/a';
  if (classification === 'SUPPORTED_IMPROVEMENT') {
    return `Candidate Brier loss is lower than baseline in this audited dataset (delta ${fmt(delta)}, 95% CI [${fmt(ci.lower)}, ${fmt(ci.upper)}]). This supports a dataset-bounded improvement claim, not universal superiority.`;
  }
  if (classification === 'SUPPORTED_WORSENING') {
    return `Candidate Brier loss is higher than baseline in this audited dataset (delta ${fmt(delta)}, 95% CI [${fmt(ci.lower)}, ${fmt(ci.upper)}]). The tested candidate is supported as worse on this comparison.`;
  }
  if (classification === 'INCONCLUSIVE') {
    return `The paired Brier difference is inconclusive in this audited dataset (delta ${fmt(delta)}, 95% CI [${fmt(ci.lower)}, ${fmt(ci.upper)}]); the interval crosses zero, so no directional superiority claim is allowed.`;
  }
  return 'No statistical claim is available.';
}

export function auditDataset(rows, options = {}) {
  const validation = validateContracts(rows);
  const scoreable = rows.filter((row) => {
    const rp = Number(row.raw_probability);
    const cp = Number(row.candidate_probability);
    const y = Number(row.resolved_target);
    return Number.isFinite(rp) && rp >= 0 && rp <= 1 && Number.isFinite(cp) && cp >= 0 && cp <= 1 && (y === 0 || y === 1);
  });

  const baseline = {
    brier: brierScore(scoreable, 'raw_probability'),
    log_loss: logLoss(scoreable, 'raw_probability'),
    ece_10: ece(scoreable, 'raw_probability'),
  };
  const candidate = {
    brier: brierScore(scoreable, 'candidate_probability'),
    log_loss: logLoss(scoreable, 'candidate_probability'),
    ece_10: ece(scoreable, 'candidate_probability'),
  };

  const differences = pairedLossDifferences(scoreable);
  const ci = movingBlockBootstrap(differences, {
    replicates: options.replicates ?? 2000,
    blockSize: options.blockSize ?? 24,
    seed: options.seed ?? 8,
  });
  const claim = classifyClaim(ci);

  return {
    schema: 'WORLD8_EVIDENCE_AUDIT/1.0',
    status: validation.status === 'PASS' ? 'AUDIT_PASS' : 'AUDIT_FAIL',
    validation,
    scoreable_contracts: scoreable.length,
    baseline,
    candidate,
    candidate_minus_baseline_brier: ci,
    claim_classification: claim,
    allowed_claim: humanClaim(claim, ci),
    prohibited_claims: [
      'profitability',
      'market-beating performance',
      'production readiness',
      'universal cross-market superiority',
      'causal architectural superiority',
      'AGI/consciousness/autonomous intelligence',
    ],
  };
}

export function generateSample({ n = 720, seed = 42, tampered = false } = {}) {
  const rng = mulberry32(seed);
  const start = Date.parse('2026-01-01T00:00:00Z');
  const rows = [];
  for (let i = 0; i < n; i++) {
    const issued = start + i * 3600_000;
    const latent = 0.5 + 0.22 * Math.sin(i / 29) + 0.08 * Math.cos(i / 11);
    const truthP = Math.min(0.88, Math.max(0.12, latent));
    const target = rng() < truthP ? 1 : 0;
    const raw = clamp01(0.5 + (truthP - 0.5) * 1.65 + (rng() - 0.5) * 0.18);
    const candidate = clamp01(0.5 + (truthP - 0.5) * 0.92 + (rng() - 0.5) * 0.05);
    rows.push({
      contract_id: `W8EA-${String(i + 1).padStart(5, '0')}`,
      symbol: 'SYNTHETIC',
      issued_at: new Date(issued).toISOString(),
      data_cutoff_at: new Date(issued).toISOString(),
      valid_from: new Date(issued).toISOString(),
      resolved_at: new Date(issued + 6 * 3600_000).toISOString(),
      lifecycle: 'RESOLVED',
      raw_probability: Number(raw.toFixed(8)),
      candidate_probability: Number(candidate.toFixed(8)),
      resolved_target: target,
      strategy_version: 'sample-strategy/1.0',
      model_version: 'sample-model/1.0',
      feature_set_hash: 'sha256:sample-feature-set',
      snapshot_hash: 'sha256:sample-snapshot',
    });
  }

  if (tampered && rows.length > 40) {
    rows[5].data_cutoff_at = new Date(Date.parse(rows[5].issued_at) + 2 * 3600_000).toISOString();
    rows[12].candidate_probability = 1.4;
    rows[20].order_id = 'LEAKED-DOWNSTREAM-ORDER';
    rows[33].resolved_target = null;
    rows[40].lifecycle = 'ACTIVE';
  }
  return rows;
}

export function compactReceipt(audit, metadata = {}) {
  return {
    schema: 'WORLD8_EVIDENCE_AUDIT_RECEIPT/1.0',
    generated_at: new Date().toISOString(),
    metadata,
    audit_status: audit.status,
    total_contracts: audit.validation.total,
    scoreable_contracts: audit.scoreable_contracts,
    validation_error_count: audit.validation.errors.length,
    validation_warning_count: audit.validation.warnings.length,
    lifecycle_counts: audit.validation.lifecycle_counts,
    metrics: {
      baseline: audit.baseline,
      candidate: audit.candidate,
    },
    candidate_minus_baseline_brier: audit.candidate_minus_baseline_brier,
    claim_classification: audit.claim_classification,
    allowed_claim: audit.allowed_claim,
    prohibited_claims: audit.prohibited_claims,
  };
}
