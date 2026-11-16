from qeri import Harness

harness = Harness(model="existing-ai-model", authority="aion", proof_policy="authorized-outcome-v1")
receipt = harness.execute(agent_id="agent-001", action="synthetic_task", inputs={"task_id": "task-123"})
print("Receipt:", receipt.payload["receipt_id"])
print("Verified:", harness.verify(receipt))
print("Note: signed receipt only; no zero-knowledge proof or quantum computation.")
