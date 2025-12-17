# src/logger.py

import json
import os
import uuid
from datetime import datetime

# Path to the JSON log file
LOG_FILE = os.path.join(os.path.dirname(__file__), "../decisions/logs.json")

def log_decision(transaction: dict, evaluation: dict) -> str:
    """
    Logs a transaction evaluation to a JSON file.
    
    Args:
        transaction (dict): The original transaction.
        evaluation (dict): The result from engine.evaluate().
    
    Returns:
        decision_id (str): Unique ID of this logged decision.
    """
    # Ensure the directory exists
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    # Create the decision record
    decision_id = str(uuid.uuid4())
    decision_record = {
        "decision_id": decision_id,
        "timestamp": datetime.utcnow().isoformat(),
        "inputs": transaction,
        "rules_triggered": evaluation.get("rules_triggered", []),
        "result": evaluation.get("result")
    }

    # Load existing logs or create new list
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            try:
                logs = json.load(f)
            except json.JSONDecodeError:
                logs = []
    else:
        logs = []

    # Append new record and save
    logs.append(decision_record)
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)

    return decision_id


# Example usage
if __name__ == "__main__":
    from engine import evaluate

    transaction = {
        "transaction_id": "TX1001",
        "amount": 4500,
        "country": "Kenya",
        "user_age": 25,
        "time_of_day": "23:15",
        "transaction_type": "online",
        "previous_fraud_flag": False
    }

    evaluation = evaluate(transaction)
    decision_id = log_decision(transaction, evaluation)
    print(f"Transaction logged with decision ID: {decision_id}")
