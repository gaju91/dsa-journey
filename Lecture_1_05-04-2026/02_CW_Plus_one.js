/**
 * leetcode: https://leetcode.com/problems/plus-one/
 * 
 * Statement: 
 * You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
 * The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
 * Increment the large integer by one and return the resulting array of digits.
 */

/**
 * Approach 1
 * 1. Array is like this [ 1, 2, 9, 3]
 * 2. Itr from end till i >= 0
 * 3. if digits[i] != 9 just add 1 and return
 *      - digits[i] = 3 = 3 + 1 = 4
 *      - return [ 1, 2, 9, 4]
 * 4. if digits[i] == 9
 *      - digits[i] = 0
 *      - in next itr anyway we are trying to add 1 (means check if digit != 9 then add 1 and return)
 * 5. if loop end without return that is our worst case and all digits were nine [ 9, 9, 9 ]
 *      - unshift 1 to start and return
 */
var plusOne = function(digits) {
    for(let i = digits.length - 1; i >= 0; i--) {
        if(digits[i] != 9) {
            digits[i]++;
            return digits;
        }

        digits[i] = 0;
    }

    // if loop is ran completed every bit was 9
    digits.unshift(1);
    return digits;
};

