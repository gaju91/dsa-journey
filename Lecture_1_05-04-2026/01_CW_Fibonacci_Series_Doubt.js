/**
 * DOCUMENTATION FOR DOUBT CLASS: Fibonacci "Off-By-One" Analysis
 * * Target: Calculate the 3rd Fibonacci Number (n = 3)
 * Expected Sequence: F(0)=0, F(1)=1, F(2)=1, F(3)=2
 * Expected Output for n=3: 2
 * 
 * leetcode: https://leetcode.com/problems/fibonacci-number/
 */

// ---------------------------------------------------------
// VERSION 1: THE "WHITEBOARD" LOGIC (Failing on LeetCode)
// ---------------------------------------------------------
function arunWhiteboardWay(n) {
    if (n <= 1) return n;

    let a = 0;
    let b = 1;

    // ISSUE: Loop range (1 to n-2)
    // For n=3: loop runs from i=1 to i=1 (Exactly 1 iteration)
    for (let i = 1; i <= n - 2; i++) {
        let c = a + b;
        a = b;
        b = c;
    }

    return b; 
}

/* DRY RUN (n = 3):
  1. Start: a=0, b=1
  2. i=1: c = 0+1 (1), a=1, b=1
  3. Loop ends (i=2 is not <= 1)
  4. Returns b = 1 
  ❌ FAILURE: Result is 1, but F(3) should be 2.
*/


// ---------------------------------------------------------
// VERSION 2: THE "ACCEPTED" LOGIC (Correct on LeetCode)
// ---------------------------------------------------------
function leetCodeAcceptedWay(n) {
    if (n <= 1) return n;

    let a = 0;
    let b = 1;

    // FIX: Loop range (2 to n) 
    // For n=3: loop runs for i=2 and i=3 (Exactly 2 iterations)
    for (let i = 2; i <= n; i++) { // 0r i = 0 to n - 2
        b = a + b; // Additive swap logic
        a = b - a;
    }

    return b;
}

/* DRY RUN (n = 3):
  1. Start: a=0, b=1
  2. i=2: b = 0+1 (1), a = 1-0 (1)
  3. i=3: b = 1+1 (2), a = 2-1 (1)
  4. Loop ends
  5. Returns b = 2 
  ✅ SUCCESS: Matches the Fibonacci sequence.
*/


// ---------------------------------------------------------
// SUMMARY OF DISCREPANCIES TO ASK IN CLASS:
// ---------------------------------------------------------
/*
  1. LOOP COUNT: 
     To reach F(n), we need to perform the addition (n-1) times. 
     Whiteboard way (1 to n-2) performs it (n-2) times. 
     Accepted way (2 to n) performs it (n-1) times.

  2. SWAP PLACEMENT:
     In the failing LeetCode screenshot, 'a = b - a' was outside 
     the loop. Does the swap MUST happen inside the loop to 
     prepare the values for the next iteration? (Answer: Yes).

  3. STARTING POINT:
     If we start the whiteboard loop at i = 0 instead of i = 1, 
     would that fix the result for n = 3?
*/