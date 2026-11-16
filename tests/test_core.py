from dataclasses import replace
from qeri import Harness, verify_receipt

def test_valid():
    h = Harness()
    assert h.verify(h.execute("agent", "task", {"x": 1}))

def test_tampered_evidence():
    h = Harness()
    r = h.execute("agent", "task", {"x": 1})
    assert not h.verify(replace(r, evidence={**r.evidence, "inputs": {"x": 2}}))

def test_rejected():
    h = Harness()
    assert not h.verify(h.execute("agent", "task", {}, approved=False))

def test_wrong_policy():
    h = Harness()
    r = h.execute("agent", "task", {})
    assert not verify_receipt(r, expected_policy="different-policy")
