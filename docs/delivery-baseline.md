# QERI™ proof-stack delivery baseline

November 22, 2026. This snapshot covers the [public v0.1 reference commit](https://github.com/E2kk111/QERI-quantum-proof-node/commit/bc316a8e88a3c65b2f24d52cb091e6941053d254). Owners can maintain current assignments, blockers, decisions, sources and weekly briefs in the [private delivery tracker](https://qeri-proof-stack.adabakadiri.chatgpt.site).

| Workstream | Evidence at baseline | Next milestone |
| --- | --- | --- |
| QERI™ protocol | The [specification](protocol-v0.1.md) describes a signed receipt and evidence commitment. The [synthetic example](../examples/agent_to_proof.py) calls the local harness and verifier. | Record a reproducible verification run against a pinned commit, including rejection of tampered evidence. |
| Testing | The [CI workflow](../.github/workflows/ci.yml) invokes pytest. GitHub returned no workflow runs for the baseline commit during this review. | Attach the test result, commit, environment and covered cases. |
| DIQSION™ | Proposed integration layer. The v0.1 README describes an optional outcome-intelligence adapter. | Document the adapter contract and exercise it with a synthetic fixture. |
| Quantum Harness™ | Governed execution, security controls and the quantum-service gateway are proposed. The Python example demonstrates local receipt handling. | Define the execution boundary and capture a reproducible receipt before adding a simulator integration. |
| AION™ | The example supplies an authority label. Verification against a trusted issuer and its policy remains a delivery milestone. | Specify issuer trust, expiry and denial cases. |

## Reference-application decision

| Proposed path | First reviewable result |
| --- | --- |
| Protocol first | An independent verifier accepts a valid receipt and rejects a modified receipt. |
| Verified Recovery first | A synthetic restoration exercise produces signed evidence for a defined recovery predicate (PoR). |
| Private eligibility first | A synthetic case exercises a defined authority predicate (PoA). A privacy claim requires a specified and tested proof construction. |

The planning register also tracks PoD and PoP. For each proof type, record the issuer, statement, verifier inputs, acceptance conditions and supporting artifact. A test result applies only to its recorded scope. Research outreach and prospective partnerships remain planning items until an interaction is documented.
