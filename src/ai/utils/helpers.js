function cleanText(input) {
 return input.replace(/[^a-zA-Z0-9]/g, '');
}
module.exports = cleanText;