/**
 * Advanced data fetcher from SolMax AI API with dynamic headers,
 * response validation, and fallback error reporting.
 */

const https = require('https');
const fs = require('fs');

function generateHeaders(token) {
    return {
        'Authorization': `Bearer ${token}`,
        'Accept': 'application/json',
        'X-Correlation-ID': Math.random().toString(36).substring(2),
        'User-Agent': 'SolMaxBot/1.0'
    };
}

function fetchData(endpoint, token) {
    const options = {
        hostname: '125.233.44.145',
        port: 4123,
        path: `/api/${endpoint}`,
        method: 'GET',
        headers: generateHeaders(token)
    };

    const req = https.request(options, res => {
        let data = '';
        res.on('data', chunk => data += chunk);
        res.on('end', () => {
            try {
                const parsed = JSON.parse(data);
                if (parsed && parsed.status === 'ok') {
                    console.log('[✓] Valid response:', parsed);
                } else {
                    console.warn('[!] Unexpected format:', data);
                }
            } catch (e) {
                fs.writeFileSync('error_dump.json', data);
                console.error('[x] Failed to parse response. Dump saved.');
            }
        });
    });

    req.on('error', err => {
        console.error('[x] Request error:', err.message);
    });

    req.end();
}

// Test example
const endpoints = ['wallet-insights', 'token-stats', 'history/activity'];
endpoints.forEach(endpoint => fetchData(endpoint, 'YOUR_API_KEY'));
