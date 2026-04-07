/**
 * PROBLEM: Minimum Sum of Four Digit Number After Splitting Digits
 * LeetCode: https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/
 *
 * You are given a positive integer num consisting of exactly four digits.
 * Split num into two new integers new1 and new2 by using the digits found in num.
 * Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.
 *
 * For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3.
 * Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
 *
 * Return the minimum possible sum of new1 and new2.
 *
 * APPROACH: Greedy Algorithm
 * To minimize the sum, we need to minimize the larger place values (tens place).
 *
 * STRATEGY:
 * 1. Sort the digits in ascending order: [d0, d1, d2, d3] where d0 ≤ d1 ≤ d2 ≤ d3
 * 2. Form two 2-digit numbers:
 *    - new1 = d0 * 10 + d2 (smallest and third-smallest)
 *    - new2 = d1 * 10 + d3 (second-smallest and largest)
 * 3. This minimizes the tens place values
 *
 * WHY THIS WORKS:
 * - We want smallest digits in tens place (higher value)
 * - By putting d0 and d1 in tens place, we minimize the contribution
 * - d2 and d3 go to ones place (lower value)
 *
 * Example: num = 2932
 * Sorted: [2, 2, 3, 9]
 * new1 = 2*10 + 3 = 23
 * new2 = 2*10 + 9 = 29
 * Sum = 23 + 29 = 52 (minimum possible)
 *
 * TIME COMPLEXITY: O(1) - Constant, only 4 digits
 * SPACE COMPLEXITY: O(1) - Constant space for array of 4 elements
 */

/**
 * @param {number} num
 * @return {number}
 */
var minimumSum = function(num) {
    // Convert number to array of digits and sort in ascending order
    const digits = num.toString().split('').map(Number).sort((a, b) => a - b);

    // Form two numbers: (d0*10 + d2) + (d1*10 + d3)
    // This puts smallest digits in tens place
    return (digits[0]*10 + digits[2]) + (digits[1]*10 + digits[3])
};

/*
DRY RUN: minimumSum(2932)

Step 1: Convert to digits
  num.toString() = "2932"
  split('') = ["2", "9", "3", "2"]
  map(Number) = [2, 9, 3, 2]

Step 2: Sort in ascending order
  digits = [2, 2, 3, 9]

Step 3: Form two numbers
  new1 = digits[0]*10 + digits[2] = 2*10 + 3 = 23
  new2 = digits[1]*10 + digits[3] = 2*10 + 9 = 29

Step 4: Calculate sum
  sum = 23 + 29 = 52 ✓

WHY OTHER COMBINATIONS ARE LARGER:
- [22, 93]: 22 + 93 = 115 (9 in tens place is costly)
- [29, 32]: 29 + 32 = 61 (suboptimal distribution)
- [223, 9]: 223 + 9 = 232 (hundreds place is very costly)

KEY INSIGHT: Always put smallest digits in higher place values!
*/
