/**
 * Complex connection with retries and logging.
 * This simulates a production-grade connection to SolMax AI API server.
 */

const http = require('http');
const fs = require('fs');

const MAX_RETRIES = 3;
let attempts = 0;

function logToFile(message) {
    fs.appendFileSync('connection.log', `[${new Date().toISOString()}] ${message}\n`);
}

function pingServer() {
    const options = {
        hostname: '125.233.44.145',
        port: 4123,
        path: '/api/ping',
        method: 'GET',
        timeout: 3000
    };

    logToFile('Attempting to ping the server...');

    const req = http.request(options, res => {
        let data = '';
        res.on('data', chunk => data += chunk);
        res.on('end', () => {
            logToFile('Server responded with: ' + data);
            console.log('Response:', data);
        });
    });

    req.on('timeout', () => {
        req.abort();
        logToFile('Request timed out.');
        retryConnection();
    });

    req.on('error', error => {
        logToFile('Error: ' + error.message);
        retryConnection();
    });

    req.end();
}

function retryConnection() {
    attempts++;
    if (attempts < MAX_RETRIES) {
        logToFile(`Retrying... (${attempts}/${MAX_RETRIES})`);
        setTimeout(pingServer, 2000);
    } else {
        logToFile('Max retries reached. Exiting.');
    }
}

pingServer();
