"""
LeetCode #41: First Missing Positive
Difficulty: Hard
Pattern: Index Marking (Advanced)

Problem:
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: Numbers in range [1,2] are all present, so answer is 3.

Example 2:
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is present but 2 is missing.

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: Smallest positive integer 1 is missing.

Constraints:
- 1 <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1
"""

from typing import List


# ============================================================================
# Approach 1: Index Marking with Preprocessing (OPTIMAL)
# Time: O(n), Space: O(1)
# ============================================================================
def firstMissingPositive(nums: List[int]) -> int:
    """
    Strategy: Modified index marking that handles out-of-range values

    Key Challenges:
    1. Values can be negative (can't use sign encoding)
    2. Values can be > n (would cause index out of bounds)
    3. Values can be <= 0 (not useful for finding missing positive)

    Solution:
    Step 1: Clean array - replace invalid values with n+1
    Step 2: Mark presence using index marking (only for valid range [1..n])
    Step 3: Find first positive index

    Analogy: "Clean your dataset first, then analyze it"
    """
    n = len(nums)

    # Step 1: Clean the array
    # Replace all invalid values (≤ 0 or > n) with n+1
    # Why n+1? It's out of range but positive (won't interfere with marking)
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1

    # Step 2: Mark presence using index marking
    # Only process values in range [1..n]
    for i in range(n):
        value = abs(nums[i])

        # Only mark if value is in valid range
        if 1 <= value <= n:
            index = value - 1
            nums[index] = -abs(nums[index])

    # Step 3: Find first positive index
    for i in range(n):
        if nums[i] > 0:
            return i + 1

    # If all [1..n] are present, answer is n+1
    return n + 1


# ============================================================================
# Approach 2: Cyclic Sort (Alternative O(1) space)
# Time: O(n), Space: O(1)
# ============================================================================
def firstMissingPositive_cyclic_sort(nums: List[int]) -> int:
    """
    Strategy: Place each valid number at its correct position

    For number x in [1..n], it should be at index x-1
    """
    n = len(nums)
    i = 0

    while i < n:
        # Only swap if:
        # 1. Value is in valid range [1..n]
        # 2. It's not already at correct position
        # 3. It's not equal to the value at its correct position (avoid infinite loop)
        correct_pos = nums[i] - 1
        if 1 <= nums[i] <= n and nums[i] != nums[correct_pos]:
            nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
        else:
            i += 1

    # Find first missing positive
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1


# ============================================================================
# Approach 3: Hash Set (Naive - O(n) space)
# Time: O(n), Space: O(n)
# ============================================================================
def firstMissingPositive_set(nums: List[int]) -> int:
    """
    Strategy: Use set for O(1) lookups

    Simple but uses extra space - not optimal for this problem
    """
    num_set = set(nums)

    # Check for smallest missing positive starting from 1
    i = 1
    while i in num_set:
        i += 1

    return i


# ============================================================================
# DRY RUN EXAMPLE
# ============================================================================
def dry_run_example():
    """
    Detailed walkthrough of index marking approach

    Input: [3, 4, -1, 1]
    Goal: Find smallest missing positive
    """
    nums = [3, 4, -1, 1]
    n = len(nums)
    print("Input:", nums)
    print(f"n = {n}\n")

    print("=== STEP 1: CLEAN ARRAY ===\n")
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            print(f"Index {i}: {nums[i]} is invalid (≤0 or >{n}), replace with {n+1}")
            nums[i] = n + 1
        else:
            print(f"Index {i}: {nums[i]} is valid, keep it")
    print(f"\nCleaned array: {nums}\n")

    print("=== STEP 2: MARK PRESENCE ===\n")
    for i in range(n):
        value = abs(nums[i])
        if 1 <= value <= n:
            index = value - 1
            print(f"Process value={value}, mark index={index}")
            nums[index] = -abs(nums[index])
            print(f"  Array: {nums}")
        else:
            print(f"Skip value={value} (out of range [1..{n}])")

    print("\n=== STEP 3: FIND FIRST POSITIVE ===\n")
    for i in range(n):
        if nums[i] > 0:
            result = i + 1
            print(f"Index {i} is positive → number {result} is missing")
            print(f"\nAnswer: {result}")
            return result

    result = n + 1
    print(f"All [1..{n}] present → Answer: {result}")
    return result


# ============================================================================
# EDGE CASES
# ============================================================================
def test_edge_cases():
    """
    Important edge cases for this problem
    """
    print("\n" + "="*60)
    print("EDGE CASES")
    print("="*60)

    edge_cases = [
        # Case 1: All negative
        ([-1, -2, -3], 1, "All negative → 1 is missing"),

        # Case 2: All out of range (too large)
        ([100, 200, 300], 1, "All > n → 1 is missing"),

        # Case 3: Perfect sequence [1..n]
        ([1, 2, 3], 4, "All [1..3] present → 4 is missing"),

        # Case 4: Single element
        ([1], 2, "Only 1 → 2 is missing"),
        ([2], 1, "Only 2 → 1 is missing"),

        # Case 5: Contains zero
        ([0, 1, 2], 3, "Zero is not positive → 3 is missing"),

        # Case 6: Large gap
        ([1, 1000], 2, "1 present, 1000 > n → 2 is missing"),

        # Case 7: Duplicates
        ([1, 1, 1], 2, "Only 1s → 2 is missing"),
    ]

    for nums, expected, description in edge_cases:
        result = firstMissingPositive(nums.copy())
        status = "✅" if result == expected else "❌"
        print(f"\n{status} {description}")
        print(f"   Input: {nums}")
        print(f"   Output: {result}, Expected: {expected}")


# ============================================================================
# WHY THIS IS HARD
# ============================================================================
def why_this_is_hard():
    """
    Explanation of what makes this problem difficult
    """
    print("\n" + "="*60)
    print("WHY THIS PROBLEM IS HARD")
    print("="*60)

    print("""
Challenges:
1. ❌ Basic index marking fails with negative numbers
   - Can't distinguish between "originally negative" and "marked negative"

2. ❌ Basic index marking fails with values > n
   - Would cause index out of bounds

3. ❌ Basic index marking fails with zeros
   - Zero maps to index -1 (invalid)

Solution:
✅ Preprocessing step to clean the array
   - Replace all invalid values with n+1
   - n+1 is safe: it's positive but out of useful range [1..n]

✅ Bounds checking during marking
   - Only mark if 1 <= value <= n

✅ Correct return value
   - If all [1..n] present, return n+1

Key Insight:
The answer MUST be in range [1..n+1]
- If any of [1..n] is missing, that's the answer
- If all [1..n] are present, answer is n+1

This is what makes it an O(1) space problem!
    """)


# ============================================================================
# TEST CASES
# ============================================================================
def run_tests():
    test_cases = [
        ([1, 2, 0], 3),
        ([3, 4, -1, 1], 2),
        ([7, 8, 9, 11, 12], 1),
        ([1], 2),
        ([2], 1),
        ([1, 2, 3, 4, 5], 6),
        ([-1, -2, -3], 1),
        ([1, 1000], 2),
    ]

    approaches = [
        ("Index Marking", firstMissingPositive),
        ("Cyclic Sort", firstMissingPositive_cyclic_sort),
        ("Hash Set", firstMissingPositive_set),
    ]

    for name, func in approaches:
        print(f"\n{'='*60}")
        print(f"Testing: {name}")
        print(f"{'='*60}")

        all_passed = True
        for nums, expected in test_cases:
            result = func(nums.copy())
            status = "✅" if result == expected else "❌"
            if result != expected:
                all_passed = False
            print(f"{status} Input: {nums}")
            print(f"   Output: {result}, Expected: {expected}")

        if all_passed:
            print("✅ All tests passed!")


if __name__ == "__main__":
    print("LeetCode #41: First Missing Positive (HARD)\n")
    print("The HARDEST index marking problem!")
    print("="*60)

    # Dry run
    print("\n" + "="*60)
    print("DRY RUN EXAMPLE")
    print("="*60)
    dry_run_example()

    # Run tests
    run_tests()

    # Test edge cases
    test_edge_cases()

    # Explain difficulty
    why_this_is_hard()

    print("\n" + "="*60)
    print("KEY TAKEAWAYS")
    print("="*60)
    print("""
1. Preprocess to handle out-of-range values
   - Replace invalid values with n+1

2. Add bounds checking before marking
   - Only mark if 1 <= value <= n

3. Remember the answer range is [1..n+1]
   - Not [1..max(nums)]!

4. This combines multiple techniques:
   - Array cleaning (preprocessing)
   - Index marking (core technique)
   - Bounds checking (defensive programming)

Interview Tip:
If asked this problem, walk through these steps:
1. "I notice the answer must be in [1..n+1]"
2. "I can clean the array first"
3. "Then use index marking on valid values"
4. "Finally find first positive index"

This shows systematic thinking, not just pattern matching!
    """)
