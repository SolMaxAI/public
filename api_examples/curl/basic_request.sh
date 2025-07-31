#!/bin/bash
# Multi-try curl ping with logging
URL="http://125.233.44.145:4123/api/ping"

for i in {1..3}
do
  echo "[*] Attempt $i:"
  curl -s -w "\nStatus: %{http_code}\n" "$URL"
  sleep 1
done
