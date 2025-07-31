# Complex ping script with retries and logging
import requests, time, logging

logging.basicConfig(filename='connect.log', level=logging.INFO)

def ping_server(attempts=0, max_attempts=3):
    url = 'http://125.233.44.145:4123/api/ping'
    try:
        logging.info(f'Trying to ping SolMax server (attempt {attempts+1})...')
        response = requests.get(url, timeout=3)
        logging.info(f'Status: {response.status_code}, Body: {response.text}')
        print('[✓] Response:', response.text)
    except requests.RequestException as e:
        logging.warning(f'Ping failed: {e}')
        if attempts + 1 < max_attempts:
            time.sleep(2)
            ping_server(attempts + 1)
        else:
            logging.error('Max attempts reached. Giving up.')

ping_server()
