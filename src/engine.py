from datetime import datetime

# Define high-risk countries for example
HIGH_RISK_COUNTRIES = ["North Korea", "Iran", "Syria"]

def evaluate(transaction: dict) -> dict:
    """
    Evaluates a transaction for potential fraud.

    Returns a dictionary:
    {
        "result": "APPROVED" | "FLAGGED_FOR_REVIEW" | "REJECTED",
        "rules_triggered": [list of rules]
    }
    """
    rules_triggered = []

    # Rule 1: Amount too high
    if transaction["amount"] > 6000:
        rules_triggered.append("amount_high")
    
    # Rule 2: High-risk country
    if transaction["country"] in HIGH_RISK_COUNTRIES:
        rules_triggered.append("high_risk_country")
    
    # Rule 3: Previous fraud flag
    if transaction["previous_fraud_flag"]:
        rules_triggered.append("previous_fraud_flag")
    
    # Rule 4: Risky transaction time (00:00–05:00)
    hour = int(transaction["time_of_day"].split(":")[0])
    if 0 <= hour < 5 and transaction["amount"] > 1000:
        rules_triggered.append("high_risk_time")
    
    # Determine final decision
    if "previous_fraud_flag" in rules_triggered:
        result = "REJECTED"
    elif rules_triggered:
        result = "FLAGGED_FOR_REVIEW"
    else:
        result = "APPROVED"

    return {
        "result": result,
        "rules_triggered": rules_triggered
    }

# Example usage
if __name__ == "__main__":
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
    print("Transaction Evaluation:", evaluation)
