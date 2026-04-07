/**
 * PROBLEM: Number of Days Between Two Dates
 * LeetCode: https://leetcode.com/problems/count-days-spent-together/
 *
 * Alice and Bob are traveling to Rome for separate business trips.
 * You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob.
 * Alice will be in the city from the dates arriveAlice to leaveAlice (inclusive),
 * while Bob will be in the city from the dates arriveBob to leaveBob (inclusive).
 * Each will be a 5-character string in the format "MM-DD", corresponding to the month and day.
 *
 * Return the total number of days that Alice and Bob are in Rome together.
 *
 * APPROACH: Interval Overlap Problem
 * Convert dates to day numbers (1-365) and find overlapping days between two intervals.
 *
 * KEY INSIGHT:
 * Two intervals [A, B] and [C, D] overlap if and only if:
 * - A <= D (Alice arrives before/when Bob leaves)
 * - C <= B (Bob arrives before/when Alice leaves)
 *
 * If they overlap, the number of overlapping days is:
 * - min(B, D) - max(A, C) + 1
 *
 * ALGORITHM:
 * 1. Pre-calculate cumulative days till each month: [31, 59, 90, 121, ...]
 * 2. Convert each date to absolute day number (1-365)
 * 3. Check if intervals overlap using the overlap condition
 * 4. Calculate overlapping days
 *
 * TIME COMPLEXITY: O(1) - Constant operations
 * SPACE COMPLEXITY: O(1) - Fixed array of 12 months
 */

// Days in each month (non-leap year)
const months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

// Cumulative days till the end of each month
// [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
const daysTillMonth = months.reduce((a, c, idx) => {
    if (idx == 0) {
        return [c]
    } else {
        const num1 = a[a.length - 1];
        const num = num1 + c;
        return [...a, num]
    }
}, []);

/**
 * @param {string} arriveAlice
 * @param {string} leaveAlice
 * @param {string} arriveBob
 * @param {string} leaveBob
 * @return {number}
 */
var countDaysTogether = function (arriveAlice, leaveAlice, arriveBob, leaveBob) {
    // Convert all dates to day numbers (1-365)
    const [
        aliceArriveDay,
        aliceLeaveDay,
        bobArriveDay,
        bobLeaveDay,
    ] = [getDay(arriveAlice), getDay(leaveAlice), getDay(arriveBob), getDay(leaveBob)];

    // Check if intervals overlap
    // Condition: Alice arrives before Bob leaves AND Bob arrives before Alice leaves
    if ((aliceArriveDay <= bobLeaveDay) && (bobArriveDay <= aliceLeaveDay)) {
        // Calculate overlap: min(end dates) - max(start dates) + 1
        const overlapStart = Math.max(aliceArriveDay, bobArriveDay);
        const overlapEnd = Math.min(aliceLeaveDay, bobLeaveDay);
        return overlapEnd - overlapStart + 1;
    }

    // No overlap
    return 0;
};

/**
 * Helper function to convert "MM-DD" to absolute day number (1-365)
 * @param {string} date - Date in "MM-DD" format
 * @return {number} - Day number from 1 to 365
 */
function getDay(date) {
    const [month, day] = date.split('-');
    const monthIndex = Number(month) - 1;

    // Days before this month + current day
    const daysBefore = monthIndex === 0 ? 0 : daysTillMonth[monthIndex - 1];
    return daysBefore + Number(day);
}

/*
DRY RUN: countDaysTogether("08-15", "08-18", "08-16", "08-19")

Step 1: Build daysTillMonth array
  months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  daysTillMonth = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
  (cumulative days till end of each month)

Step 2: Convert dates to day numbers
  Alice: "08-15" → getDay("08-15")
    month = 8, day = 15
    daysBefore = daysTillMonth[7-1] = daysTillMonth[6] = 212
    dayNumber = 212 + 15 = 227

  Alice leave: "08-18" → 212 + 18 = 230
  Bob arrive: "08-16" → 212 + 16 = 228
  Bob leave: "08-19" → 212 + 19 = 231

  aliceArriveDay = 227
  aliceLeaveDay = 230
  bobArriveDay = 228
  bobLeaveDay = 231

Step 3: Check overlap condition
  Is aliceArriveDay <= bobLeaveDay? → 227 <= 231 ✓
  Is bobArriveDay <= aliceLeaveDay? → 228 <= 230 ✓
  → Intervals overlap!

Step 4: Calculate overlap
  overlapStart = max(227, 228) = 228
  overlapEnd = min(230, 231) = 230
  overlap = 230 - 228 + 1 = 3 days

Return: 3 ✓

VISUAL REPRESENTATION:
  Alice:  [227------------230]
  Bob:           [228-----------231]
  Overlap:       [228----230] = 3 days (Aug 16, 17, 18)

EDGE CASES:
1. No overlap: "01-10" to "01-15", "01-20" to "01-25" → 0
2. Complete overlap: "01-10" to "01-20", "01-12" to "01-18" → 7
3. Same dates: "01-10" to "01-15", "01-10" to "01-15" → 6
*/
