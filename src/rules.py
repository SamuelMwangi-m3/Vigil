HIGH_RISK_COUNTRIES = {
    "North Korea",
    "Iran",
    "Syria"
}

def check_amount(transaction):
    if transaction["amount"] > 5000:
        return "amount_high"
    return None

def check_country(transaction):
    if transaction["country"] in HIGH_RISK_COUNTRIES:
        return "high_risk_country"
    return None

def check_previous_fraud(transaction):
    if transaction["previous_fraud_flag"]:
        return "previous_fraud_flag"
    return None

def check_time(transaction):
    hour = int(transaction["time_of_day"].split(":")[0])
    if 0 <= hour < 5 and transaction["amount"] > 1000:
        return "high_risk_time"
    return None

RULES = [
    check_amount,
    check_country,
    check_previous_fraud,
    check_time
]
