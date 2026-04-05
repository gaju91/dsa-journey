/**
 * leetcode: https://leetcode.com/problems/add-two-integers/description/
 *      - Normal sum a + b
 * leetcode: https://leetcode.com/problems/sum-of-two-integers/description/
 *      - Sum without + sign
 * 
 * Statement: 
 * Given two integers a and b, return the sum of the two integers without using the operators + and -.
 */


/**
 * Approach 1 (Specific to leetcode 2235)
 * 1. return a + b
 */
var sum = function (a, b) {
    return a + b;
};

/**
 * Approach 2 (with bit manipulation)
 * 1. need to represent or think the number a and b in terms of bits
 *      - a = 7  = 4 2 1   = 1 1 1 
 *      - b = 11 = 8 4 2 1 = 1 0 1 1
 * 
 * 2. Now what we want
 *      - 1 + 1 = sum = 0 and carry 1
 *      - 1 + 0 = sum = 1 and carry 0
 *      - 0 + 0 = sum = 0 and carry 0
 * 
 *      - Sum condition can be satisfied with xor
 *          - Because  1^1           = 0
 *          - Rest of  0^0 and 1^0   = 0 or 1
 *              - as 0 don't affect the xor
 * 
 *      - No remainder/carry can be handled by and 
 *          - because 1 & 1             = 1
 *          - Rest of 0 & 1 and 0 & 0   = 0
 * 
 * 3. Now we got sum and carry in one itr, next would be shift the carry by 1 place for next itr
 *      - carry(a&b) << 1
 * 
 * 4. Iterate till carry = 0 and return sum
 */
var getSum = function (a, b) {
    while (b) {
        [a, b] = [a ^ b, (a & b) << 1]
    }
    return a;
};

