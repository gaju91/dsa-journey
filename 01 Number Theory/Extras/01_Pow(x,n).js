/**
 * PROBLEM: Pow(x, n) - Calculate x raised to the power n
 * LeetCode: https://leetcode.com/problems/powx-n/
 *
 * Given two numbers x and n, calculate x^n efficiently.
 * Handle both positive and negative exponents.
 *
 */



/**
 * Approach 1: Binary Exponentiation (Exponentiation by Squaring)
 * Instead of multiplying x by itself n times (O(n)), we use the
 * binary representation of n to reduce operations to O(log n).
 *
 * KEY INSIGHT:
 * - If n is even: x^n = (x^2)^(n/2)
 * - If n is odd:  x^n = x * (x^2)^(n/2)
 *
 * ALGORITHM:
 * 1. Handle negative exponent: if n < 0, compute x^|n| then take reciprocal
 * 2. Start with ans = 1
 * 3. While n > 0:
 *    - If n is odd: multiply ans by current x
 *    - Square x (to get next power of 2)
 *    - Divide n by 2 (shift to next bit)
 *
 * TIME COMPLEXITY: O(log n) - Only log₂(n) iterations
 * SPACE COMPLEXITY: O(1) - Constant space
 *
 * COMPARISON WITH NAIVE APPROACH:
 * Naive: x * x * x * ... (n times) = O(n) time
 * Binary: Uses binary representation = O(log n) time
 *
 * Example: 2^10
 * - Naive: 10 multiplications
 * - Binary: 4 multiplications (10 in binary is 1010)
 */

/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function(x, n) {
    let isNegative = n < 0;
    n = Math.abs(n);

    let ans = 1;
    while (n > 0) {
        if(n % 2 !== 0) {  // If n is odd, multiply ans by current x
            ans *= x
        }

        x *= x;  // Square x for next iteration
        n = Math.floor(n/2)  // Divide n by 2 (binary shift right)
    }

    return isNegative ? 1/ans : ans;
};