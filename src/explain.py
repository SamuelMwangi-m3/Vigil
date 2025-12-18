EXPLANATIONS = {
    "amount_high": "Transaction amount exceeds normal limits.",
    "high_risk_country": "Transaction originated from a high-risk country.",
    "previous_fraud_flag": "User has a history of fraudulent activity.",
    "high_risk_time": "Transaction occurred during high-risk hours."
}

def generate_explanation(rules_triggered: list) -> str:
    if not rules_triggered:
        return "Transaction approved. No risk indicators detected."

    return " ".join(
        EXPLANATIONS.get(rule, rule)
        for rule in rules_triggered
    )
