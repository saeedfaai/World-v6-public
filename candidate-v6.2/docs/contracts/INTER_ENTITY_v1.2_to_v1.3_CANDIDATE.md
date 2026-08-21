# Inter-Entity Communication v1.3 Candidate Overlay
Resolution metadata is an additive envelope extension. Desired/minimum/effective
are scoped to exact Profile id/version/hash, potentially as a multi-segment
vector. Receiver chooses effective detail only within its own declared exact
capability/policy. Sender/recipient authorization, sender epoch/sequence,
payload integrity and ACK semantics remain unchanged.
