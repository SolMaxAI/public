
class RiskModel:
    def __init__(self):
        self.weights = {
            "holders": 0.3,
            "liquidity": 0.3,
            "community": 0.4
        }

    def predict(self, features):
        score = (
            features["holders"] * self.weights["holders"] +
            features["liquidity"] * self.weights["liquidity"] +
            features["community"] * self.weights["community"]
        )
        if score > 75:
            return "low"
        elif score > 50:
            return "medium"
        return "high"
