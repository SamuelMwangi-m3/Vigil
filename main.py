# main.py

from src.engine import evaluate
from src.logger import log_decision
from src.replay import replay_decision
from src.explain import generate_explanation

def run_transaction(transaction: dict):
    """
    Runs the full VIGIL workflow:
    1. Evaluate transaction
    2. Log decision
    3. Generate explanation
    """
    # Step 1: Evaluate
    evaluation = evaluate(transaction)
    print("Evaluation Result:", evaluation)

    # Step 2: Log decision
    decision_id = log_decision(transaction, evaluation)
    print(f"Transaction logged with decision ID: {decision_id}")

    # Step 3: Replay check
    replay_result = replay_decision(decision_id)
    print(f"Replay Result for {decision_id}:", replay_result)

    # Step 4: Generate explanation
    explanation = generate_explanation(evaluation["rules_triggered"])
    print("Explanation:", explanation)

    return decision_id

if __name__ == "__main__":
    # Sample transaction
    transaction = {
        "transaction_id": "TX1001",
        "amount": 4500,
        "country": "Kenya",
        "user_age": 25,
        "time_of_day": "23:15",
        "transaction_type": "online",
        "previous_fraud_flag": False
    }

    run_transaction(transaction)