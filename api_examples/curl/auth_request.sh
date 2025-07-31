#!/bin/bash
# Advanced curl request with dynamic headers and dump on error
API_KEY="YOUR_API_KEY"
URL="http://125.233.44.145:4123/api/wallet-insights"
HEADER="Authorization: Bearer $API_KEY"

echo "[*] Fetching data from wallet-insights endpoint..."
curl -s -H "$HEADER" -H "X-Request-ID: $RANDOM" -H "User-Agent: CurlClient/1.0" "$URL" || {
  echo "[x] Request failed, dumping..."
  curl -v "$URL" -H "$HEADER" > error_curl_dump.txt
}
