/**
 * PROBLEM: Count Good Numbers - Calculate permutations of specific digits
 * LeetCode: https://leetcode.com/problems/count-good-numbers/
 *
 * A digit string is good if the digits (0-indexed) at even indices are even
 * and the digits at odd indices are prime (2, 3, 5, or 7).
 * Given an integer n, return the total number of good digit strings of length n.
 * Since the answer may be large, return it modulo 10^9 + 7.
 *
 */

/**
 * Approach 1: Binary Exponentiation with Modulo Arithmetic
 * Instead of iterating n times (O(n)), we count the total even/odd slots
 * and compute (5^even_slots * 4^odd_slots) % (10^9 + 7) in O(log n).
 *
 * KEY INSIGHT:
 * - Even indices (0, 2, 4...) have 5 valid choices: 0, 2, 4, 6, 8.
 * - Odd indices (1, 3, 5...) have 4 valid choices: 2, 3, 5, 7.
 * - n can be up to 10^15, requiring BigInt to avoid integer overflow.
 * - Modulo must be applied at every step of multiplication to prevent memory crash.
 *
 * ALGORITHM:
 * 1. Set MOD = 1000000007n.
 * 2. Convert n to BigInt.
 * 3. Calculate oddCount = n / 2n (BigInt division automatically floors).
 * 4. Calculate evenCount = (n + 1n) / 2n (simulates ceiling).
 * 5. Use binary exponentiation to compute 5^evenCount and 4^oddCount under MOD:
 * - If pow is odd: multiply ans by current num and apply MOD.
 * - Square num (to get next power of 2) and apply MOD.
 * - Divide pow by 2 (shift to next bit).
 * 6. Multiply the results, apply MOD one last time, and cast to standard Number.
 *
 * TIME COMPLEXITY: O(log n) - Only log₂(n) iterations for the powers.
 * SPACE COMPLEXITY: O(1) - Constant auxiliary space.
 *
 * COMPARISON WITH NAIVE APPROACH:
 * Naive: Iterate n times, multiplying choices sequentially = O(n) time (Times out for 10^15).
 * Binary: Halves the exponent each step, taking at most ~50 steps = O(log n) time.
 *
 * Example: n = 4
 * - even slots = 2 (indices 0, 2), odd slots = 2 (indices 1, 3)
 * - ans = (5^2 * 4^2) % 1000000007 = (25 * 16) % 1000000007 = 400
 */

/**
 * @param {number} n
 * @return {number}
 */
const MOD = 1000000007n;

var countGoodNumbers = function(n) {
    const bigN = BigInt(n);
    
    const oddCount = bigN / 2n;
    const evenCount = (bigN + 1n) / 2n;
    
    const oddChances = moduloPow(4n, oddCount);
    const evenChances = moduloPow(5n, evenCount);
    
    return Number(((oddChances % MOD) * (evenChances % MOD)) % MOD);
};

function moduloPow(num, pow) {
    let ans = 1n;
    
    while (pow > 0n) {
        if (pow % 2n === 1n) {  // If pow is odd, multiply ans by current base
            ans = (ans * num) % MOD;
        }
        
        num = (num * num) % MOD; // Square the base for next iteration
        pow = pow / 2n;          // Divide pow by 2 (binary shift right)
    }
    
    return ans % MOD;
}