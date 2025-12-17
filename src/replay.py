import json
import os
from .engine import evaluate

# Path to the JSON log file
LOG_FILE = os.path.join(os.path.dirname(__file__), "../decisions/logs.json")

def replay_decision(decision_id: str) -> dict:
    """
    Replays a decision by ID:
    1. Loads the original transaction from logs.json
    2. Runs engine.evaluate() again
    3. Returns the new evaluation for comparison
    """
    if not os.path.exists(LOG_FILE):
        raise FileNotFoundError("Log file does not exist.")

    with open(LOG_FILE, "r") as f:
        try:
            logs = json.load(f)
        except json.JSONDecodeError:
            logs = []

    # Find the transaction with this decision_id
    transaction_record = next((log for log in logs if log["decision_id"] == decision_id), None)

    if transaction_record is None:
        raise ValueError(f"No transaction found with decision ID: {decision_id}")

    original_transaction = transaction_record["inputs"]
    new_evaluation = evaluate(original_transaction)

    return new_evaluation

# Example usage
if __name__ == "__main__":
    test_id = input("Enter a decision ID to replay: ")
    result = replay_decision(test_id)
    print("Replayed Evaluation:", result)
