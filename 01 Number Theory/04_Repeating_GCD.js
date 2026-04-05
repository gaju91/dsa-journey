/**
 * gfg: https://www.geeksforgeeks.org/problems/repeating-gcd4659/1
 * * Statement: 
 * Given three integers N, x and y. A number A is formed by repeating N x times 
 * and another number B is formed by repeating N y times. Find GCD(A, B).
 */

/**
 * Approach 2 (Geometric Series)
 * Concept: GCD(Repeat(N, x), Repeat(N, y)) = Repeat(N, gcd(x, y))
 * 1. Find n = gcd(x, y).
 * 2. Find d = number of digits in N.
 * 3. Calculate k = 10^d.
 * 4. Return (N * (k^n - 1)) / (k - 1).
 */
var FindGcd = (N, x, y) => {
    const gcd = (a, b) => (b === 0 ? a : gcd(b, a % b));
    return FindRepeat(N, gcd(x, y));
}

var FindRepeat = (N, n) => {
    let d = N.toString().length;
    let k = Math.pow(10, d);

    return (N * (Math.pow(k, n) - 1)) / (k - 1);
};