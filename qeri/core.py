"""QERI v0.1: signed synthetic execution receipts, NOT zero-knowledge proofs."""
from __future__ import annotations
import hashlib
import json
import uuid
from dataclasses import dataclass
from typing import Any
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey
from cryptography.hazmat.primitives import serialization

def canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")

def digest(value: Any) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()

@dataclass(frozen=True)
class Receipt:
    payload: dict
    signature_hex: str
    public_key_hex: str
    evidence: dict

    def as_dict(self) -> dict:
        return {"payload": self.payload, "signature_hex": self.signature_hex,
                "public_key_hex": self.public_key_hex, "evidence": self.evidence}

def verify_receipt(receipt: Receipt, expected_policy: str | None = None) -> bool:
    try:
        if receipt.payload["version"] != "qeri-receipt-v0.1":
            return False
        if expected_policy is not None and receipt.payload["policy"] != expected_policy:
            return False
        if receipt.payload["evidence_sha256"] != digest(receipt.evidence):
            return False
        if receipt.payload["accepted"] is not True:
            return False
        key = Ed25519PublicKey.from_public_bytes(bytes.fromhex(receipt.public_key_hex))
        key.verify(bytes.fromhex(receipt.signature_hex), canonical(receipt.payload))
        return True
    except (ValueError, KeyError, TypeError, Exception):
        return False

class Harness:
    """Local demo. Caller controls identity and signing key; no trusted external attestation."""
    def __init__(self, model: str = "synthetic", authority: str = "aion",
                 proof_policy: str = "authorized-outcome-v1", signing_key: Ed25519PrivateKey | None = None):
        self.model, self.authority, self.proof_policy = model, authority, proof_policy
        self._key = signing_key or Ed25519PrivateKey.generate()

    def execute(self, agent_id: str, action: str, inputs: dict, *, approved: bool = True) -> Receipt:
        if not agent_id or not action or not isinstance(inputs, dict):
            raise ValueError("agent_id, action, and dict inputs required")
        # Simulated only: this never invokes a tool, model, quantum service, or external action.
        evidence = {"agent_id": agent_id, "action": action, "inputs": inputs,
                    "model": self.model, "authority": self.authority, "approved": approved}
        payload = {"version": "qeri-receipt-v0.1", "receipt_id": str(uuid.uuid4()),
                   "policy": self.proof_policy, "evidence_sha256": digest(evidence),
                   "accepted": bool(approved)}
        pub = self._key.public_key().public_bytes(
            encoding=serialization.Encoding.Raw, format=serialization.PublicFormat.Raw).hex()
        return Receipt(payload, self._key.sign(canonical(payload)).hex(), pub, evidence)

    def verify(self, receipt: Receipt) -> bool:
        return verify_receipt(receipt, expected_policy=self.proof_policy)
