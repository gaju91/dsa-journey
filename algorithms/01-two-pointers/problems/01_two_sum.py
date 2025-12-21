"""
LeetCode #1: Two Sum
Difficulty: Easy
Pattern: Hash Map (NOT Two Pointers for unsorted)

Problem:
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists

Follow-up: Can you come up with an algorithm that is less than O(n²) time complexity?
"""

from typing import List


# ============================================================================
# ⚠️ IMPORTANT NOTE
# ============================================================================
# This is NOT a two-pointers problem because the array is UNSORTED!
# Two pointers requires sorted array to work correctly.
#
# For sorted version, see: LC #167 - Two Sum II
# ============================================================================


# ============================================================================
# Approach 1: Hash Map (OPTIMAL for unsorted)
# Time: O(n), Space: O(n)
# ============================================================================
def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Strategy: Use hash map to store complements

    Analogy: "Looking for a partner - remember everyone you've met.
              When you meet someone new, check if their perfect match
              (complement) is in your memory."

    Key Insight:
    - For each num, its complement is (target - num)
    - Store seen numbers with their indices
    - Check if complement exists before adding current number
    """
    seen = {}  # num -> index

    for i, num in enumerate(nums):
        complement = target - num

        # Check if complement exists
        if complement in seen:
            return [seen[complement], i]

        # Store current number
        seen[num] = i

    return []  # No solution (shouldn't happen per constraints)


# ============================================================================
# Approach 2: Brute Force (For understanding)
# Time: O(n²), Space: O(1)
# ============================================================================
def twoSum_brute_force(nums: List[int], target: int) -> List[int]:
    """
    Strategy: Check all possible pairs

    This is what we're trying to avoid with hash map!
    """
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []


# ============================================================================
# Approach 3: Two Pointers (WRONG for this problem!)
# Time: O(n log n), Space: O(n)
# ============================================================================
def twoSum_two_pointers_WRONG(nums: List[int], target: int) -> List[int]:
    """
    ⚠️ WARNING: This is INCORRECT for original Two Sum problem!

    Why it fails:
    - Sorting changes the original indices
    - We need to return original indices, not sorted indices
    - Even if we store original indices, it's more complex than hash map

    This approach is shown to demonstrate why two pointers
    doesn't work well here.
    """
    # Create list of (value, original_index) pairs
    indexed_nums = [(num, i) for i, num in enumerate(nums)]

    # Sort by value
    indexed_nums.sort()

    left, right = 0, len(indexed_nums) - 1

    while left < right:
        current_sum = indexed_nums[left][0] + indexed_nums[right][0]

        if current_sum == target:
            # Return original indices
            return sorted([indexed_nums[left][1], indexed_nums[right][1]])
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []


# ============================================================================
# WHY TWO POINTERS DOESN'T WORK HERE
# ============================================================================
def why_two_pointers_fails() -> None:
    """
    Explanation of why two pointers is not ideal for Two Sum
    """
    print("="*60)
    print("WHY TWO POINTERS FAILS FOR TWO SUM")
    print("="*60)

    print("""
Problem Requirements:
1. Array is UNSORTED
2. Need to return ORIGINAL INDICES
3. One-time query (not multiple queries)

Hash Map Approach:
✅ Works on unsorted array
✅ Returns original indices directly
✅ O(n) time, O(n) space
✅ Single pass through array

Two Pointers Approach:
❌ Requires sorting (O(n log n))
❌ Must track original indices (extra complexity)
❌ Still O(n log n) time due to sorting
❌ More code, more error-prone

Conclusion:
For unsorted Two Sum → Use Hash Map
For sorted Two Sum (LC #167) → Use Two Pointers

This is a classic example of choosing the right pattern!
    """)


# ============================================================================
# DRY RUN EXAMPLE
# ============================================================================
def dry_run_hash_map() -> List[int]:
    """
    Walkthrough of hash map approach
    """
    nums = [2, 7, 11, 15]
    target = 9

    print("\n" + "="*60)
    print("DRY RUN: Hash Map Approach")
    print("="*60)
    print(f"Input: nums = {nums}, target = {target}\n")

    seen: dict[int, int] = {}

    for i, num in enumerate(nums):
        complement = target - num
        print(f"Step {i+1}:")
        print(f"  Current: nums[{i}] = {num}")
        print(f"  Need complement: {target} - {num} = {complement}")
        print(f"  Seen so far: {seen}")

        if complement in seen:
            print(f"  ✓ Found! complement {complement} at index {seen[complement]}")
            print(f"  Answer: [{seen[complement]}, {i}]")
            return [seen[complement], i]

        seen[num] = i
        print(f"  Store {num} at index {i}")
        print()

    print("No solution found")
    return []


# ============================================================================
# COMPARISON: Hash Map vs Two Pointers
# ============================================================================
def compare_approaches() -> None:
    """
    Compare performance of different approaches
    """
    import timeit

    # Test case
    nums = list(range(1000))
    target = 1997  # Sum of last two elements

    print("\n" + "="*60)
    print("PERFORMANCE COMPARISON")
    print("="*60)
    print(f"Array size: {len(nums)}")
    print(f"Target: {target}\n")

    # Hash Map
    time_hash = timeit.timeit(
        lambda: twoSum(nums[:], target),
        number=1000
    )
    print(f"Hash Map:        {time_hash:.4f} seconds")

    # Brute Force (only 10 iterations - it's slow!)
    time_brute = timeit.timeit(
        lambda: twoSum_brute_force(nums[:], target),
        number=10
    ) / 10  # Normalize to per-iteration
    print(f"Brute Force:     {time_brute:.4f} seconds (extrapolated)")

    # Two Pointers (with sorting overhead)
    time_two_ptr = timeit.timeit(
        lambda: twoSum_two_pointers_WRONG(nums[:], target),
        number=1000
    )
    print(f"Two Pointers:    {time_two_ptr:.4f} seconds")

    print(f"\nSpeedup (Hash vs Brute): {time_brute/time_hash:.1f}x faster")


# ============================================================================
# TEST CASES
# ============================================================================
def run_tests() -> None:
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 5, 3, 7, 9], 10, [1, 4]),  # Multiple valid but return any
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
    ]

    approaches = [
        ("Hash Map", twoSum),
        ("Brute Force", twoSum_brute_force),
    ]

    for name, func in approaches:
        print(f"\n{'='*60}")
        print(f"Testing: {name}")
        print(f"{'='*60}")

        all_passed = True
        for nums, target, _expected in test_cases:  # _expected not used (validation is different)
            result = func(nums.copy(), target)

            # Check if result is valid (not necessarily same as expected)
            is_valid = (
                len(result) == 2 and
                result[0] != result[1] and
                nums[result[0]] + nums[result[1]] == target
            )

            status = "✅" if is_valid else "❌"
            if not is_valid:
                all_passed = False

            print(f"{status} Input: nums={nums}, target={target}")
            print(f"   Output: {result}, Valid: {is_valid}")

        if all_passed:
            print("✅ All tests passed!")


# ============================================================================
# PATTERN RECOGNITION GUIDE
# ============================================================================
def pattern_recognition_guide() -> None:
    """
    How to recognize when to use which approach
    """
    print("\n" + "="*60)
    print("PATTERN RECOGNITION: WHEN TO USE WHAT")
    print("="*60)

    print("""
TWO SUM - Family of Problems:

1. LC #1: Two Sum (Unsorted Array)
   Array: UNSORTED
   Return: Original indices
   → Use: HASH MAP
   → Time: O(n), Space: O(n)

2. LC #167: Two Sum II (Sorted Array)
   Array: SORTED
   Return: Indices
   → Use: TWO POINTERS (Opposite Direction)
   → Time: O(n), Space: O(1)

3. LC #170: Two Sum III (Data Structure Design)
   Operation: Multiple queries
   → Use: HASH MAP for storage
   → Time: O(1) add, O(n) find

4. LC #653: Two Sum IV (Binary Search Tree)
   Data Structure: BST
   → Use: TWO POINTERS on inorder traversal
   → OR: Hash set during traversal

Pattern Recognition Rules:
┌────────────────┬──────────────┬─────────────────┐
│  Condition     │  Sorted?     │  Best Approach  │
├────────────────┼──────────────┼─────────────────┤
│ One query      │ No           │ Hash Map        │
│ One query      │ Yes          │ Two Pointers    │
│ Multiple query │ No           │ Hash Map        │
│ Multiple query │ Yes          │ Two Pointers    │
│ Return indices │ No (values)  │ Either works    │
└────────────────┴──────────────┴─────────────────┘

Memory Constraint:
- Can use O(n) space? → Hash Map (faster to code)
- Must use O(1) space? → Two Pointers (need sorted)
    """)


if __name__ == "__main__":
    print("LeetCode #1: Two Sum\n")
    print("⚠️  NOTE: This is NOT a two-pointers problem!")
    print("=" * 60)

    # Dry run
    dry_run_hash_map()

    # Run tests
    run_tests()

    # Explain why two pointers doesn't work
    why_two_pointers_fails()

    # Pattern recognition
    pattern_recognition_guide()

    # Performance comparison
    compare_approaches()

    print("\n" + "="*60)
    print("KEY TAKEAWAYS")
    print("="*60)
    print("""
1. Two Sum (unsorted) → Hash Map, not Two Pointers
2. Two Sum II (sorted) → Two Pointers is optimal
3. Always check if array is sorted before choosing approach
4. Hash map trades space for time (O(n) space for O(n) time)
5. Two pointers needs sorted array to guarantee correctness

Interview Tip:
When interviewer asks "Two Sum":
1. First question: "Is the array sorted?"
2. If sorted → Two Pointers
3. If unsorted → Hash Map
4. Explain why you chose each approach

This shows you understand the trade-offs!
    """)
