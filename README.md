# VIGIL — Fraud Decision Trace Logger

## Overview
VIGIL is a Python system designed to **monitor, evaluate, and log financial transactions** for potential fraud.  
It provides a **transparent audit trail**, allowing decisions to be reproduced and explained in plain English.

---

## Features

1. **Transaction Evaluation**
   - Processes transactions against defined rules
   - Outputs: APPROVED, FLAGGED_FOR_REVIEW, REJECTED

2. **Decision Logging**
   - Assigns a unique ID and timestamp
   - Stores inputs, rules triggered, and final decision
   - Logs stored persistently in JSON or SQLite

3. **Replay Engine**
   - Re-run decisions for verification
   - Ensures reproducibility

4. **Explanation Generator**
   - Human-readable reasons for decisions
   - Bridges technical rules with user understanding

---

## Sample Input

```json
{
  "transaction_id": "TX1001",
  "amount": 4500,
  "country": "Kenya",
  "user_age": 25,
  "time_of_day": "23:15",
  "transaction_type": "online",
  "previous_fraud_flag": false
}
