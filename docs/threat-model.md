# QERI Threat Model — Initial Draft

Trust boundary: the v0.1 local caller supplies identity, policy outcome, evidence, and a self-generated signing key. Verification proves only internal consistency and possession of the corresponding key, not real-world truth.

Risks: fabricated evidence, key substitution, replay, malicious policy selection, compromised model/tool outputs, prompt injection, stale measurements, unauthorized actions, and private-data leakage.

Required before production: trusted agent identities, signed policy registry, key lifecycle, external authorization, anti-replay, timestamps, evidence source attestation, privacy review, adversarial testing, and independent cryptographic audit.

Do not submit PHI or other sensitive production data to the demo.
