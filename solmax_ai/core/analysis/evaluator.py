
import json
import random

def fetch_token_data(hash):
    # Simulate token data retrieval
    return {
        "holders": random.randint(100, 5000),
        "liquidity": round(random.uniform(1.0, 10.0), 2),
        "community_score": random.randint(50, 100)
    }

def evaluate_token(hash):
    data = fetch_token_data(hash)
    score = 0
    if data["holders"] > 1000:
        score += 30
    if data["liquidity"] > 5.0:
        score += 30
    score += int(data["community_score"] * 0.4)

    risk = "low" if score > 70 else "medium" if score > 40 else "high"
    result = {
        "hash": hash,
        "score": score,
        "risk": risk,
        "details": data
    }
    return result
