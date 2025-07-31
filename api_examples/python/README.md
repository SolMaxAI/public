# Python API Examples for SolMax AI

This folder demonstrates connecting to the SolMax AI API server with Python.

## Files

### `connect.py`
- Logs attempts and handles retries on timeout.
- Uses the `requests` and `logging` libraries.
- Writes logs to `connect.log`.

### `fetch_data.py`
- Fetches and parses multiple endpoints.
- Validates JSON and dumps failed responses to disk.
- Can be extended for multi-threading or queuing.

## Requirements

```bash
pip install requests
```

## Running

```bash
python3 connect.py
python3 fetch_data.py
```

Consider using `schedule` or `APScheduler` for periodic polling in production.
