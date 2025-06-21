const analyze = require('../analysis');
test('should return score', () => {
 expect(analyze('123')).toHaveProperty('score');
});