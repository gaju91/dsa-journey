"""
LeetCode #16: 3Sum Closest
Difficulty: Medium
Pattern: Two Pointers (Fixed + Opposite Direction)

Problem:
Given an integer array nums of length n and an integer target, find three
integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

Constraints:
- 3 <= nums.length <= 500
- -1000 <= nums[i] <= 1000
- -10^4 <= target <= 10^4
"""

from typing import List


# ============================================================================
# Approach 1: Fixed + Two Pointers - OPTIMAL
# Time: O(n²), Space: O(1)
# ============================================================================
def threeSumClosest(nums: List[int], target: int) -> int:
    """
    Strategy: Same as 3Sum, but track closest sum instead of exact match

    Key Differences from 3Sum:
    - Don't need to avoid duplicates (only one solution)
    - Track minimum difference from target
    - Update closest_sum when we find closer sum

    Analogy: "Try all triplets, remember the one closest to bullseye."
    """
    nums.sort()  # CRITICAL: Must sort first
    n = len(nums)
    closest_sum = float('inf')
    min_diff = float('inf')

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            current_diff = abs(current_sum - target)

            # Update closest if this is closer
            if current_diff < min_diff:
                min_diff = current_diff
                closest_sum = current_sum

            # Early termination: exact match
            if current_sum == target:
                return target

            # Move pointers based on comparison
            if current_sum < target:
                # Sum too small, need larger
                left += 1
            else:
                # Sum too large, need smaller
                right -= 1

    return closest_sum


# ============================================================================
# Approach 2: With Early Termination Optimization
# Time: O(n²), Space: O(1)
# ============================================================================
def threeSumClosestOptimized(nums: List[int], target: int) -> int:
    """
    Strategy: Add early termination when we can't get closer

    Additional optimizations:
    1. If nums[i] is too large, all subsequent will be larger
    2. If current triplet is farther than previous best, skip
    """
    nums.sort()
    n = len(nums)
    closest_sum = nums[0] + nums[1] + nums[2]  # Initialize with first triplet
    min_diff = abs(closest_sum - target)

    for i in range(n - 2):
        # Early termination: if smallest possible is larger than current best
        if i > 0:
            min_possible = nums[i] + nums[i + 1] + nums[i + 2]
            if abs(min_possible - target) > min_diff:
                # Can't do better with this i or larger
                if min_possible > target:
                    break

        left = i + 1
        right = n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            # Exact match - can't get closer!
            if current_sum == target:
                return target

            current_diff = abs(current_sum - target)

            # Update if closer
            if current_diff < min_diff:
                min_diff = current_diff
                closest_sum = current_sum

            # Standard two pointers movement
            if current_sum < target:
                left += 1
            else:
                right -= 1

    return closest_sum


# ============================================================================
# DRY RUN EXAMPLE
# ============================================================================
def dry_run_three_sum_closest() -> int:
    """
    Detailed walkthrough
    """
    nums = [-1, 2, 1, -4]
    target = 1

    print("\n" + "="*60)
    print("DRY RUN: 3Sum Closest")
    print("="*60)
    print(f"Input: nums = {nums}, target = {target}\n")

    # Step 1: Sort
    nums.sort()
    print(f"After sorting: {nums}\n")

    n = len(nums)
    closest_sum = float('inf')
    min_diff = float('inf')

    for i in range(n - 2):
        print(f"{'='*50}")
        print(f"Iteration i={i}, nums[i]={nums[i]}")

        left = i + 1
        right = n - 1

        step = 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            current_diff = abs(current_sum - target)

            print(f"\nStep {step}:")
            print(f"  Triplet: [{nums[i]}, {nums[left]}, {nums[right]}]")
            print(f"  Sum: {current_sum}, Target: {target}")
            print(f"  Difference: |{current_sum} - {target}| = {current_diff}")

            if current_diff < min_diff:
                min_diff = current_diff
                closest_sum = current_sum
                print(f"  ✓ New closest sum: {closest_sum} (diff={min_diff})")

            if current_sum == target:
                print(f"  ✓✓ Exact match found!")
                return target

            if current_sum < target:
                print(f"  → Sum < target, left++")
                left += 1
            else:
                print(f"  → Sum > target, right--")
                right -= 1

            step += 1

    print(f"\n{'='*50}")
    print(f"Final closest sum: {closest_sum}")
    return closest_sum


# ============================================================================
# WHY THIS WORKS
# ============================================================================
def why_this_works() -> None:
    """
    Explanation of algorithm correctness
    """
    print("\n" + "="*60)
    print("WHY THIS ALGORITHM WORKS")
    print("="*60)

    print("""
Same Foundation as 3Sum:
- Fix first element nums[i]
- Use two pointers for remaining elements
- Explore all possible triplet combinations

Key Difference:
- 3Sum: Looking for exact sum == 0
- 3Sum Closest: Looking for sum closest to target

Greedy Tracking:
- Keep track of closest_sum seen so far
- Update whenever we find closer sum
- No need to store all triplets, just the closest

Why We Don't Miss the Answer:
- For each fixed i, two pointers explores ALL valid pairs
- We compare EVERY triplet sum with target
- We ALWAYS update if closer sum is found
- Therefore, we MUST find the closest sum

Optimization - Early Termination:
- If current_sum == target: Can't get closer, return immediately
- If all remaining sums are farther: Can break early

Time Complexity:
- Sort: O(n log n)
- Nested loops: O(n²)
- Total: O(n²)

Space: O(1) - only variables

Pattern: Same as 3Sum, but:
- Track minimum instead of collecting all
- Don't need duplicate handling
- Can terminate early on exact match
    """)


# ============================================================================
# COMPARISON: 3Sum vs 3Sum Closest
# ============================================================================
def compare_with_three_sum() -> None:
    """
    Compare with regular 3Sum
    """
    print("\n" + "="*60)
    print("COMPARISON: 3Sum vs 3Sum Closest")
    print("="*60)

    print("""
Similarities:
✓ Both use fixed + two pointers pattern
✓ Both require sorting first
✓ Both O(n²) time complexity
✓ Both use same pointer movement logic

Differences:

┌─────────────────┬──────────────────┬─────────────────────┐
│ Aspect          │ 3Sum             │ 3Sum Closest        │
├─────────────────┼──────────────────┼─────────────────────┤
│ Goal            │ Find sum == 0    │ Find sum ≈ target   │
│ Return          │ List of triplets │ Single sum value    │
│ Duplicates      │ Must skip        │ Don't need to skip  │
│ Early exit      │ No               │ Yes (if exact)      │
│ Tracking        │ Collect all      │ Track min diff      │
└─────────────────┴──────────────────┴─────────────────────┘

Code Similarity: ~90% the same!

The main logic is identical, just:
- 3Sum: if sum == 0: add to result
- 3Sum Closest: track closest sum to target
    """)


# ============================================================================
# COMMON MISTAKES
# ============================================================================
def common_mistakes() -> None:
    """
    Demonstrate common bugs
    """
    print("\n" + "="*60)
    print("COMMON MISTAKES")
    print("="*60)

    print("""
❌ Mistake 1: Not sorting first
   # Two pointers requires sorted array!
   closest_sum = float('inf')
   for i in range(n-2):
       # Won't work correctly without sorting

   ✓ Fix: nums.sort()

❌ Mistake 2: Wrong initialization
   closest_sum = 0  # WRONG! What if all sums are far from 0?

   ✓ Fix: Initialize with first valid triplet
   closest_sum = nums[0] + nums[1] + nums[2]

   OR use float('inf') and update on first iteration

❌ Mistake 3: Comparing absolute differences incorrectly
   if current_sum - target < min_diff:  # WRONG! Not absolute value

   ✓ Fix: Use absolute value
   if abs(current_sum - target) < min_diff:

❌ Mistake 4: Returning difference instead of sum
   return min_diff  # WRONG! Return the SUM, not difference

   ✓ Fix: return closest_sum

❌ Mistake 5: Not handling exact match optimization
   # Keep searching even after finding exact match

   ✓ Fix: Return immediately
   if current_sum == target:
       return target

❌ Mistake 6: Skipping duplicates (unnecessary here)
   if i > 0 and nums[i] == nums[i-1]:  # Not needed!
       continue

   ✓ Note: Unlike 3Sum, duplicates don't matter here
   We want THE closest, duplicates are fine
    """)


# ============================================================================
# TEST CASES
# ============================================================================
def run_tests() -> None:
    test_cases = [
        ([-1, 2, 1, -4], 1, 2),
        ([0, 0, 0], 1, 0),
        ([1, 1, 1, 0], -100, 2),
        ([1, 1, -1, -1, 3], -1, -1),
        ([-1, 0, 1, 1, 55], 3, 2),
    ]

    approaches = [
        ("Basic", threeSumClosest),
        ("Optimized", threeSumClosestOptimized),
    ]

    for name, func in approaches:
        print(f"\n{'='*60}")
        print(f"Testing: {name}")
        print(f"{'='*60}")

        all_passed = True
        for nums, target, expected in test_cases:
            result = func(nums.copy(), target)
            status = "✅" if result == expected else "❌"
            if result != expected:
                all_passed = False

            print(f"{status} Input: nums={nums}, target={target}")
            print(f"   Output: {result}, Expected: {expected}")

        if all_passed:
            print("✅ All tests passed!")


if __name__ == "__main__":
    print("LeetCode #16: 3Sum Closest\n")
    print("⭐ Two Pointers Pattern: Fixed + Opposite Direction")
    print("="*60)

    # Dry run
    dry_run_three_sum_closest()

    # Run tests
    run_tests()

    # Explanations
    why_this_works()
    compare_with_three_sum()

    # Common mistakes
    common_mistakes()

    print("\n" + "="*60)
    print("KEY TAKEAWAYS")
    print("="*60)
    print("""
1. Almost identical to 3Sum, but track closest instead of collecting
2. Initialize closest_sum with first triplet (not 0!)
3. No need to skip duplicates (only one answer)
4. Early termination: return immediately if exact match
5. Track minimum absolute difference

Decision Rule:
- current_sum < target → left++ (need larger sum)
- current_sum > target → right-- (need smaller sum)
- Always update closest if current is closer

Interview Strategy:
1. Mention similarity to 3Sum
2. Explain tracking minimum difference
3. Code with proper initialization
4. Add early termination optimization
5. Test with target far from any sum
6. Mention O(n²) time complexity

Common Pitfalls:
❌ Returning min_diff instead of closest_sum
❌ Not using abs() for difference
❌ Initializing closest_sum to 0
✓ Initialize with first triplet or inf
✓ Return sum, not difference
✓ Early exit on exact match

Related Problems:
- LC #15: 3Sum (find exact sum)
- LC #18: 4Sum (extend to 4 numbers)
- LC #259: 3Sum Smaller (count triplets)

This is easier than 3Sum - no duplicate handling!
    """)
