/**
 * leetcode: https://leetcode.com/problems/number-of-common-factors/
 * 
 * Statement: 
 *  Given two positive integers a and b, return the number of common factors of a and b.
 *  An integer x is a common factor of a and b if x divides both a and b.
 */


/**
 * Approach 1 (Brute Force)
 * find the all i such that
 *  - a % i == b % i == 0
 * 
 * Algorithm
 * 1. Find smallest number (just to avoid useless itr), even you go till big number that is fine
 * 2. from i = 1 to i <= smallest number
 *      - If a % i == 0 and b % i == 0
 *          - record a solution
 * 3. return solution
 */

var commonFactors = function(a, b) {
    let count = 0;
    for(let i = 1; i <= a; i++) {
        if(a % i == 0 && b % i == 0) {
            count += 1
        }
    }

    return count;
};

/**
 * Approach 2 (gcd)
 * all the factors of a and b would be the factor of gcd(a, b)
 * 
 * 1. Find gcd of a and b | gcd(a, b) = gcd(a % b, b), given a > b
 * 2. find divisors of gcd number 
 *      - More optimized to go till sqrt(gcd)
 */
var commonFactors = function(a, b) {
    return getDivisors(getGCD(a, b))
};

function getGCD(a, b) {
    while (b !== 0) {
        [a, b] = [b, a % b]
    }
    return a;
}

function getDivisors(n) {
    let count = 0;
    for(let i = 1; i*i <= n; i++) {
        if(n % i == 0) {
            count += 1

            if(i != n/i) {
                count += 1
            }
        }
    }

    return count;
}

