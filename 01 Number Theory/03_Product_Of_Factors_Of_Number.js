/**
 * gfg: https://www.geeksforgeeks.org/problems/product-of-factors-of-number4757/1
 * 
 * Statement: 
 *  Given a number N. Calculate the product of all factors of N. Since Answer can be very large,compute the answer modulo 109+7.
 */


/**
 * Approach 1 (Modulo at every step)
 * Concept: (num1 * num2) % MOD = (num1 % MOD) * (num2 % MOD)
 * 1. Let base prod = 1;
 * 2. Loop till sqrt of N;
 * 3. For every factor i and N/i (!= i) record a modulo solution
 *      - prod = (prod * solution) % MOD
 * 4. return the prod;
 */
var factorProduct = (N) => {
    const MOD = 10 ** 9 + 7;

    let prod = 1;
    for (let i = 1; i * i <= N; i++) {
        if (N % i == 0) {
            prod = (prod * i) % MOD;

            if (i != Math.trunc(N / i)) {
                prod = (prod * Math.trunc(N / i)) % MOD;
            }
        }
    }

    return prod
}