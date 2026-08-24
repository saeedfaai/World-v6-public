const SUPABASE_URL = 'https://ogiqujrubsvzohqremuv.supabase.co';
const PUBLISHABLE_KEY = 'sb_publishable_7VzMz9MOj63TV3nFcYmGmA_qzRXsSVp';
const TERMS_URL = 'https://github.com/saeedfaai/World-v6-public/blob/main/world8-z0a/PAID_ACCESS/TERMS_OF_ACCESS.md';
const SESSION_KEY = 'world8_paid_access_session_v1';
const INVOICE_KEY = 'world8_current_invoice_v1';

let session = null;
let authMode = 'signin';
let pendingPlan = null;
let pendingPlanName = null;
let pendingManualPlan = null;
let currentInvoice = null;
let countdownTimer = null;

const $ = (id) => document.getElementById(id);
const qsa = (s) => [...document.querySelectorAll(s)];

function show(el){ if (typeof el === 'string') el = $(el); el?.classList.remove('hidden'); }
function hide(el){ if (typeof el === 'string') el = $(el); el?.classList.add('hidden'); }
function openModal(id){ show(id); document.body.style.overflow = 'hidden'; }
function closeModal(id){ hide(id); document.body.style.overflow = ''; }
function toast(text){ const t=$('toast'); t.textContent=text; show(t); setTimeout(()=>hide(t),2200); }
function message(id,text,type=''){ const el=$(id); el.textContent=text; el.className=`message ${type}`.trim(); show(el); }
function clearMessage(id){ hide(id); $(id).textContent=''; $(id).className='message hidden'; }
function sleep(ms){ return new Promise(r=>setTimeout(r,ms)); }

function saveSession(s){
  session = s;
  if (s) localStorage.setItem(SESSION_KEY, JSON.stringify(s));
  else localStorage.removeItem(SESSION_KEY);
  updateAccountUI();
}
function loadStoredSession(){
  try { return JSON.parse(localStorage.getItem(SESSION_KEY) || 'null'); } catch { return null; }
}
function saveInvoice(obj){
  currentInvoice = obj;
  if (obj) localStorage.setItem(INVOICE_KEY, JSON.stringify(obj));
  else localStorage.removeItem(INVOICE_KEY);
}
function loadStoredInvoice(){
  try { return JSON.parse(localStorage.getItem(INVOICE_KEY) || 'null'); } catch { return null; }
}

async function authFetch(path, options={}){
  const headers = { 'apikey': PUBLISHABLE_KEY, 'content-type':'application/json', ...(options.headers||{}) };
  return fetch(`${SUPABASE_URL}/auth/v1${path}`, { ...options, headers });
}
async function signIn(email,password){
  const r = await authFetch('/token?grant_type=password',{method:'POST',body:JSON.stringify({email,password})});
  const j = await r.json();
  if (!r.ok) throw new Error(j?.msg || j?.error_description || j?.message || 'Sign in failed');
  const s = {
    access_token:j.access_token, refresh_token:j.refresh_token,
    expires_at: Math.floor(Date.now()/1000) + Number(j.expires_in || 3600),
    user:j.user
  };
  saveSession(s); return s;
}
async function signUp(email,password){
  const r = await authFetch('/signup',{method:'POST',body:JSON.stringify({email,password})});
  const j = await r.json();
  if (!r.ok) throw new Error(j?.msg || j?.error_description || j?.message || 'Account creation failed');
  if (j.access_token) {
    saveSession({access_token:j.access_token,refresh_token:j.refresh_token,expires_at:Math.floor(Date.now()/1000)+Number(j.expires_in||3600),user:j.user});
    return {active:true};
  }
  return {active:false,user:j.user};
}
async function refreshSession(){
  if (!session?.refresh_token) return false;
  const r = await authFetch('/token?grant_type=refresh_token',{method:'POST',body:JSON.stringify({refresh_token:session.refresh_token})});
  const j = await r.json();
  if (!r.ok || !j.access_token) { saveSession(null); return false; }
  saveSession({access_token:j.access_token,refresh_token:j.refresh_token || session.refresh_token,expires_at:Math.floor(Date.now()/1000)+Number(j.expires_in||3600),user:j.user || session.user});
  return true;
}
async function validateSession(){
  if (!session?.access_token) return false;
  if (Number(session.expires_at||0) < Math.floor(Date.now()/1000)+30) {
    if (!await refreshSession()) return false;
  }
  const r = await fetch(`${SUPABASE_URL}/auth/v1/user`,{headers:{apikey:PUBLISHABLE_KEY,Authorization:`Bearer ${session.access_token}`}});
  if (!r.ok) {
    if (await refreshSession()) return validateSession();
    saveSession(null); return false;
  }
  const user=await r.json(); session.user=user; saveSession(session); return true;
}
async function invoke(name,body={},retry=true){
  if (!session?.access_token) throw new Error('Please sign in first');
  if (Number(session.expires_at||0) < Math.floor(Date.now()/1000)+30) await refreshSession();
  const r = await fetch(`${SUPABASE_URL}/functions/v1/${name}`,{
    method:'POST',
    headers:{apikey:PUBLISHABLE_KEY,Authorization:`Bearer ${session.access_token}`,'content-type':'application/json'},
    body:JSON.stringify(body)
  });
  if (r.status===401 && retry && await refreshSession()) return invoke(name,body,false);
  let j={}; try{ j=await r.json(); }catch{}
  if (!r.ok) { const e=new Error(j?.error || `Request failed (${r.status})`); e.status=r.status; e.data=j; throw e; }
  return j;
}

function updateAccountUI(){
  const btn=$('accountBtn');
  if (session?.user) {
    const email=session.user.email || 'Account';
    btn.textContent=`Sign out · ${email.length>20?email.slice(0,17)+'…':email}`;
    btn.dataset.logged='1';
  } else {
    btn.textContent='Sign in'; btn.dataset.logged='0';
  }
}
function setAuthMode(mode){
  authMode=mode;
  qsa('[data-auth-tab]').forEach(b=>b.classList.toggle('active',b.dataset.authTab===mode));
  $('authTitle').textContent = mode==='signin' ? 'Sign in' : 'Create account';
  $('authSubmit').textContent = mode==='signin' ? 'Sign in' : 'Create account';
  $('authPassword').setAttribute('autocomplete', mode==='signin'?'current-password':'new-password');
  clearMessage('authMessage');
}
function requireAuth(after){
  if (session?.user) return true;
  if (after?.type==='buy'){ pendingPlan=after.plan; pendingPlanName=after.name; }
  if (after?.type==='manual') pendingManualPlan=after.plan;
  openModal('authModal'); return false;
}

async function handleAuthSubmit(e){
  e.preventDefault(); clearMessage('authMessage');
  const email=$('authEmail').value.trim(); const password=$('authPassword').value;
  $('authSubmit').disabled=true;
  try{
    if(authMode==='signin'){
      await signIn(email,password);
      message('authMessage','Signed in successfully.','success');
      await sleep(450); closeModal('authModal');
      if(pendingPlan){ const p=pendingPlan,n=pendingPlanName; pendingPlan=pendingPlanName=null; openCheckout(p,n); }
      else if(pendingManualPlan){ const p=pendingManualPlan; pendingManualPlan=null; openRequest(p); }
      await loadVault();
    } else {
      const res=await signUp(email,password);
      if(res.active){
        message('authMessage','Account created and signed in.','success');
        await sleep(450); closeModal('authModal');
        if(pendingPlan){ const p=pendingPlan,n=pendingPlanName; pendingPlan=pendingPlanName=null; openCheckout(p,n); }
        else if(pendingManualPlan){ const p=pendingManualPlan; pendingManualPlan=null; openRequest(p); }
        await loadVault();
      } else {
        message('authMessage','Account created. Check your email for the confirmation message, then return here and sign in.','success');
        setAuthMode('signin'); $('authEmail').value=email;
      }
    }
  }catch(err){ message('authMessage',err.message,'error'); }
  finally{$('authSubmit').disabled=false;}
}

function openCheckout(plan,name){
  if(!requireAuth({type:'buy',plan,name})) return;
  pendingPlan=plan; pendingPlanName=name;
  $('selectedPlan').textContent=name;
  $('checkoutTitle').textContent=`${name} — BTC checkout`;
  $('acceptTerms').checked=false;
  show('checkoutPre'); hide('invoiceBox'); clearMessage('paymentMessage');
  openModal('checkoutModal');
}
async function createInvoice(){
  clearMessage('paymentMessage');
  if(!$('acceptTerms').checked){ toast('Accept the Paid Access Terms first'); return; }
  const btn=$('createInvoiceBtn'); btn.disabled=true; btn.textContent='Creating invoice…';
  try{
    const data=await invoke('create-btc-invoice',{plan_slug:pendingPlan,accept_terms:true});
    const obj={...data.invoice,plan_slug:pendingPlan,plan_name:pendingPlanName};
    saveInvoice(obj); renderInvoice(obj,data); hide('checkoutPre'); show('invoiceBox');
  }catch(err){ message('paymentMessage',err.message,'error'); show('invoiceBox'); }
  finally{btn.disabled=false;btn.textContent='Create 30-minute BTC invoice';}
}
function renderInvoice(inv,data={}){
  if(!inv) return;
  $('invoiceCode').textContent=inv.invoice_code;
  const btc=(Number(inv.required_sats)/1e8).toFixed(8);
  $('btcAmount').textContent=btc;
  $('satAmount').textContent=Number(inv.required_sats).toLocaleString('en-US');
  $('btcAddress').textContent=inv.destination_address;
  $('rateSource').textContent=inv.rate_source || data?.invoice?.rate_source || 'spot-rate';
  $('spotRate').textContent=inv.btc_usd_price ? ` · $${Number(inv.btc_usd_price).toLocaleString('en-US',{maximumFractionDigits:2})}/BTC` : '';
  $('openWallet').href=`bitcoin:${encodeURIComponent(inv.destination_address)}?amount=${btc}&label=${encodeURIComponent('World 8 / Z0-A')}&message=${encodeURIComponent(inv.invoice_code)}`;
  startCountdown(inv.expires_at);
}
function startCountdown(expiresAt){
  clearInterval(countdownTimer);
  const tick=()=>{
    const ms=new Date(expiresAt).getTime()-Date.now();
    if(ms<=0){ $('invoiceCountdown').textContent='EXPIRED'; clearInterval(countdownTimer); return; }
    const total=Math.floor(ms/1000),m=Math.floor(total/60),s=total%60;
    $('invoiceCountdown').textContent=`${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`;
  }; tick(); countdownTimer=setInterval(tick,1000);
}
async function verifyPayment(){
  clearMessage('paymentMessage');
  if(!currentInvoice?.id){ message('paymentMessage','Create an invoice first.','error'); return; }
  const txid=$('txid').value.trim().toLowerCase();
  if(!/^[0-9a-f]{64}$/.test(txid)){ message('paymentMessage','Enter a valid 64-character Bitcoin transaction ID.','error'); return; }
  const btn=$('verifyPaymentBtn'); btn.disabled=true; btn.textContent='Checking Bitcoin network…';
  try{
    const data=await invoke('verify-btc-payment',{invoice_id:currentInvoice.id,txid});
    if(data.invoice_status==='paid'){
      message('paymentMessage',`Payment confirmed. Access is active${data.entitlement?.expires_at ? ' until '+new Date(data.entitlement.expires_at).toLocaleString() : ''}.`,'success');
      currentInvoice.status='paid'; saveInvoice(currentInvoice); await loadVault();
    } else if(data.invoice_status==='confirming'){
      message('paymentMessage',`Transaction found. Confirmations: ${data.confirmations}/${data.required_confirmations}. Return and verify again after confirmation.`,'');
    } else if(data.invoice_status==='underpaid'){
      message('paymentMessage',`Underpayment detected: ${Number(data.paid_sats).toLocaleString()} sats received; ${Number(data.required_sats).toLocaleString()} sats required. Do not send a second transaction automatically; request manual review.`,'error');
    } else message('paymentMessage',`Payment status: ${data.invoice_status}.`,'');
  }catch(err){ message('paymentMessage',err.message,'error'); }
  finally{btn.disabled=false;btn.textContent='Verify payment';}
}

const manualNames={team_evaluation:'Team Evaluation',enterprise_due_diligence:'Enterprise Due Diligence',internal_pilot_license:'Internal Pilot License',commercial_license:'Commercial Production License'};
function openRequest(plan){
  if(!requireAuth({type:'manual',plan})) return;
  pendingManualPlan=plan;
  $('requestPlanLabel').textContent=manualNames[plan] || plan;
  $('requestOrg').value=''; $('requestNote').value=''; clearMessage('requestMessage');
  openModal('requestModal');
}
async function submitManualRequest(e){
  e.preventDefault(); clearMessage('requestMessage');
  const btn=$('requestForm').querySelector('button[type="submit"]'); btn.disabled=true; btn.textContent='Submitting…';
  try{
    const data=await invoke('request-manual-access',{plan_slug:pendingManualPlan,organization:$('requestOrg').value.trim(),note:$('requestNote').value.trim()});
    message('requestMessage',`${data.message} Request ID: ${data.request.id}`,'success');
  }catch(err){ message('requestMessage',err.message,'error'); }
  finally{btn.disabled=false;btn.textContent='Submit for manual review';}
}

async function loadVault(){
  const state=$('vaultState'), mats=$('vaultMaterials');
  if(!session?.user){
    show(state); hide(mats); hide('materialReader');
    state.innerHTML='<div class="lock">⌁</div><h3>Sign in to check your entitlement</h3><p>If your BTC payment is confirmed, your materials will appear here automatically.</p><button class="primary" id="vaultSignInDynamic">Sign in</button>';
    $('vaultSignInDynamic').onclick=()=>openModal('authModal'); return;
  }
  state.innerHTML='<div class="lock">⋯</div><h3>Checking entitlement…</h3><p>Validating your paid-access status.</p>'; show(state); hide(mats);
  try{
    const data=await invoke('get-paid-vault',{});
    const e=data.entitlement;
    state.innerHTML=`<div class="lock">✓</div><h3>${escapeHtml(e.plan_name)} active</h3><p>Licensed account: ${escapeHtml(session.user.email||'authenticated user')} · ${e.expires_at?'expires '+escapeHtml(new Date(e.expires_at).toLocaleString()):'no automatic expiry'} · commercial rights: ${e.commercial_rights?'granted':'not granted'}</p>`;
    mats.innerHTML='';
    (data.materials||[]).forEach(m=>{
      const card=document.createElement('article'); card.className='material-card';
      card.innerHTML=`<div class="eyebrow">PRIVATE · v${escapeHtml(m.version)}</div><h3>${escapeHtml(m.title)}</h3><p>${escapeHtml(m.summary)}</p><div class="material-meta"><span>SHA-256: ${escapeHtml(String(m.content_sha256).slice(0,16))}…</span><span>Controlled view</span></div><button class="secondary full">Open licensed material</button>`;
      card.querySelector('button').onclick=()=>openMaterial(m.slug); mats.appendChild(card);
    });
    show(mats);
  }catch(err){
    if(err.status===403) state.innerHTML='<div class="lock">⌁</div><h3>No active paid entitlement</h3><p>Choose Technical or Professional Access above, create a BTC invoice, and verify the transaction after confirmation.</p>';
    else state.innerHTML=`<div class="lock">!</div><h3>Vault check failed</h3><p>${escapeHtml(err.message)}</p>`;
  }
}
async function openMaterial(slug){
  try{
    const data=await invoke('get-paid-vault',{material_slug:slug});
    $('readerTitle').textContent=data.material.title;
    $('readerWatermark').textContent=data.watermark;
    $('readerBody').innerHTML=renderMarkdown(data.material.content_markdown);
    show('materialReader'); $('materialReader').scrollIntoView({behavior:'smooth',block:'start'});
  }catch(err){ toast(err.message); }
}
function escapeHtml(s=''){ return String(s).replace(/[&<>'"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c])); }
function renderMarkdown(md=''){
  const lines=escapeHtml(md).split('\n'); let out='',inUl=false,inOl=false;
  const closeLists=()=>{ if(inUl){out+='</ul>';inUl=false;} if(inOl){out+='</ol>';inOl=false;} };
  for(let line of lines){
    if(/^### /.test(line)){closeLists();out+=`<h3>${inline(line.slice(4))}</h3>`;continue;}
    if(/^## /.test(line)){closeLists();out+=`<h2>${inline(line.slice(3))}</h2>`;continue;}
    if(/^# /.test(line)){closeLists();out+=`<h1>${inline(line.slice(2))}</h1>`;continue;}
    if(/^\*\*.*\*\*$/.test(line) && line.length<180){closeLists();out+=`<p><strong>${inline(line.slice(2,-2))}</strong></p>`;continue;}
    if(/^- /.test(line)){if(inOl){out+='</ol>';inOl=false;}if(!inUl){out+='<ul>';inUl=true;}out+=`<li>${inline(line.slice(2))}</li>`;continue;}
    if(/^\d+\. /.test(line)){if(inUl){out+='</ul>';inUl=false;}if(!inOl){out+='<ol>';inOl=true;}out+=`<li>${inline(line.replace(/^\d+\. /,''))}</li>`;continue;}
    closeLists(); if(line.trim()) out+=`<p>${inline(line)}</p>`;
  }
  closeLists(); return out;
}
function inline(s){ return s.replace(/\*\*(.+?)\*\*/g,'<strong>$1</strong>').replace(/`(.+?)`/g,'<code>$1</code>'); }

qsa('[data-close]').forEach(b=>b.addEventListener('click',()=>closeModal(b.dataset.close)));
qsa('.modal').forEach(m=>m.addEventListener('click',e=>{if(e.target===m) closeModal(m.id);}));
qsa('[data-auth-tab]').forEach(b=>b.addEventListener('click',()=>setAuthMode(b.dataset.authTab)));
$('authForm').addEventListener('submit',handleAuthSubmit);
$('accountBtn').addEventListener('click',async()=>{
  if(session?.user){ saveSession(null); saveInvoice(null); await loadVault(); toast('Signed out'); }
  else openModal('authModal');
});
$('vaultSignIn').addEventListener('click',()=>openModal('authModal'));
qsa('.buy').forEach(b=>b.addEventListener('click',()=>openCheckout(b.dataset.plan,b.dataset.name)));
qsa('.request').forEach(b=>b.addEventListener('click',()=>openRequest(b.dataset.plan)));
$('createInvoiceBtn').addEventListener('click',createInvoice);
$('verifyPaymentBtn').addEventListener('click',verifyPayment);
$('requestForm').addEventListener('submit',submitManualRequest);
$('closeReader').addEventListener('click',()=>hide('materialReader'));
qsa('[data-copy]').forEach(b=>b.addEventListener('click',async()=>{const t=$(b.dataset.copy)?.textContent||'';try{await navigator.clipboard.writeText(t);toast('Copied');}catch{toast('Copy failed');}}));
window.addEventListener('keydown',e=>{if(e.key==='Escape')qsa('.modal:not(.hidden)').forEach(m=>closeModal(m.id));});

(async function init(){
  session=loadStoredSession(); updateAccountUI();
  if(session) await validateSession();
  currentInvoice=loadStoredInvoice();
  if(currentInvoice && currentInvoice.status!=='paid' && new Date(currentInvoice.expires_at).getTime()>Date.now()){
    pendingPlan=currentInvoice.plan_slug; pendingPlanName=currentInvoice.plan_name; renderInvoice(currentInvoice); $('selectedPlan').textContent=pendingPlanName||pendingPlan; hide('checkoutPre'); show('invoiceBox');
  }
  await loadVault();
})();