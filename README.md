# QERI™ — Quantum Proof Node

**Any model. Any agent. Any application. Verifiable outcomes.**

QERI is an experimental, model-agnostic agent-to-proof protocol for accountable execution, cryptographic provenance, and independently inspectable outcomes.

[QERI™ Proof-Stack Delivery Tracker](https://qeri-proof-stack.adabakadiri.chatgpt.site) · Private workspace for milestones, test evidence, decisions, and weekly briefs.

## Architecture

- **QERI:** proof-node protocol, evidence receipts, and verification.
- **DIQSION:** proposed optional tiny-model outcome intelligence adapter.
- **Quantum Harness:** proposed governed execution and quantum-service gateway.
- **AION:** proposed deterministic policy and authority integration.

## Implemented in v0.1

A local, synthetic-only Python reference for signed receipts, evidence hashes, and deterministic acceptance checks. **This is not a zero-knowledge proof, quantum computation, post-quantum cryptography, or a production-grade authorization system.**

## Run

```bash
pip install -e '.[dev]'
python examples/agent_to_proof.py
pytest -q
```

See [protocol specification](docs/protocol-v0.1.md) and [threat model](docs/threat-model.md).

## Roadmap

1. Versioned receipts and identity/policy bindings.
2. Genuine ZK circuit for a narrow outcome predicate and independent verifier.
3. DIQSION adapter with deterministic authorization boundaries.
4. Quantum simulator and calibration provenance adapter.
5. Crypto-agility, threat assessment, and independent security review.

Apache-2.0 licensed. Research/reference implementation; no patient data or real-world control actions.
