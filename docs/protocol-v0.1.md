# QERI Protocol v0.1 — Experimental

QERI = Quantum Proof Node. The protocol aims to connect AI models, agents, software, and physical systems to governed execution and independently inspectable evidence.

## Reference receipt

A receipt includes: version, random receipt ID, policy identifier, SHA-256 evidence commitment, acceptance boolean, Ed25519 signature, and public verification key. JSON is canonicalized with sorted keys and compact separators.

The demo verifies signature integrity, evidence commitment, accepted flag, and optional policy equality. It **does not** prove identity ownership, execution authenticity, correct AI reasoning, actual policy authorization, quantum computation, or any zero-knowledge claim.

## Proposed QERI-ZK extension

Public inputs: policy/version identifiers, evidence commitment, acceptance predicate identifier.
Private witness: selected sensitive evidence fields.
Circuit: check the commitment and a narrow deterministic acceptance predicate.
Verifier: independently check the proof against the approved verification key and public inputs.

Select and threat-model a real ZK proof system before claiming ZK capability. Quantum-resistant properties must be evaluated separately.
