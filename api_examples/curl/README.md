# CURL Scripts for SolMax AI API

Minimal but powerful examples of using curl to connect and fetch data from the SolMax AI backend.

## Files

### `basic_request.sh`
Sends 3 ping attempts to `/api/ping`, showing HTTP status codes.

### `auth_request.sh`
Authenticated request using a bearer token. If failed, it dumps verbose output to a file.

## Running

```bash
sh basic_request.sh
sh auth_request.sh
```

Make sure to replace `YOUR_API_KEY` in the script with a valid token.

## Debugging

You can enable full trace:
```bash
curl -v -H "Authorization: Bearer ..." http://125.233.44.145:4123/api/wallet-insights
```
