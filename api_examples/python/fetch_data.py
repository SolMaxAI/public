# Full example with header builder, multi-endpoint and error dump
import requests
import json
import time

def build_headers(api_key):
    return {
        "Authorization": f"Bearer {api_key}",
        "User-Agent": "SolMaxClient/1.0",
        "X-Client": "PythonScript"
    }

def fetch(endpoint, api_key):
    url = f"http://125.233.44.145:4123/api/{endpoint}"
    try:
        print(f"[*] Fetching {endpoint}...")
        response = requests.get(url, headers=build_headers(api_key), timeout=5)
        if response.ok:
            print("[✓] Data:", response.json())
        else:
            print("[x] Server error:", response.status_code)
            with open("error_response.txt", "w") as f:
                f.write(response.text)
    except Exception as e:
        print("[x] Exception:", str(e))

if __name__ == "__main__":
    endpoints = ["wallet-insights", "token-stats", "activity/feed"]
    for ep in endpoints:
        fetch(ep, "YOUR_API_KEY")
        time.sleep(1)
