# Node.js API Examples for SolMax AI

This directory contains advanced Node.js examples for connecting to the SolMax AI backend at `125.233.44.145:4123`.

## Files

### `connect.js`
A robust connection handler with retries, logging, and timeout logic. It pings the `/api/ping` endpoint and writes logs to `connection.log`.

### `fetch_data.js`
A complete implementation to fetch multiple endpoints using a bearer token. This includes:

- Dynamic headers (with `X-Correlation-ID`)
- Response validation
- JSON parsing
- Error fallback to `error_dump.json`

## Getting Started

Install Node.js if you haven't:
```bash
brew install node
# or
sudo apt install nodejs npm
```

Run:
```bash
node connect.js
node fetch_data.js
```

## Tip

Set your token in an `.env` file and use `dotenv` for production security.
