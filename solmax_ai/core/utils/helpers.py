
import re

def clean_data(data: str) -> str:
    data = data.strip()
    data = re.sub(r'[^\w\s]', '', data)
    return data.lower()

def normalize_score(score: int, max_score: int = 100) -> float:
    return round((score / max_score) * 100, 2)
