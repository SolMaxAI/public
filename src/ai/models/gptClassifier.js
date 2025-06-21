// Simulated GPT-based classification
module.exports = function classify(text) {
 return text.includes('rug') ? 'high risk' : 'safe';
};