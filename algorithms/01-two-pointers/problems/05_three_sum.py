"""
LeetCode #15: 3Sum
Difficulty: Medium
Pattern: Two Pointers (Fixed + Opposite Direction)

Problem:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:
Input: nums = [0,1,1]
Output: []

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]

Constraints:
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5
"""

from typing import List


# ============================================================================
# Approach 1: Fixed + Two Pointers - OPTIMAL
# Time: O(n²), Space: O(1) excluding output
# ============================================================================
def threeSum(nums: List[int]) -> List[List[int]]:
    """
    Strategy: Fix one element, use two pointers for the rest

    Key Steps:
    1. SORT the array (critical for two pointers)
    2. Fix first element (i)
    3. Use two pointers (left, right) to find pair that sums to -nums[i]
    4. Skip duplicates to avoid duplicate triplets

    Analogy: "Fix one person, two others search for balance."

    [-4, -1, -1, 0, 1, 2]
      ↑   ↑           ↑
      i   L           R

    For i=0 (nums[i]=-4):
    - Need L + R = 4
    - Use two pointers on remaining array
    """
    nums.sort()  # CRITICAL: Must sort first!
    result: List[List[int]] = []
    n = len(nums)

    for i in range(n - 2):  # Need at least 3 elements
        # Skip duplicate values for first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Two pointers for remaining array
        left = i + 1
        right = n - 1
        target = -nums[i]  # We want left + right = target

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                # Found a triplet!
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                # Skip duplicates for right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Move both pointers
                left += 1
                right -= 1

            elif current_sum < target:
                # Sum too small, need larger values
                left += 1
            else:
                # Sum too large, need smaller values
                right -= 1

    return result


# ============================================================================
# Approach 2: With Explicit Duplicate Handling (More Readable)
# Time: O(n²), Space: O(1)
# ============================================================================
def threeSumExplicit(nums: List[int]) -> List[List[int]]:
    """
    Same algorithm but with more explicit duplicate handling
    Easier to understand for beginners
    """
    nums.sort()
    result: List[List[int]] = []
    n = len(nums)

    for i in range(n - 2):
        # Early termination: if smallest is positive, sum can't be 0
        if nums[i] > 0:
            break

        # Skip duplicates for first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Move left forward, skipping duplicates
                left_val = nums[left]
                while left < right and nums[left] == left_val:
                    left += 1

                # Move right backward, skipping duplicates
                right_val = nums[right]
                while left < right and nums[right] == right_val:
                    right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


# ============================================================================
# Approach 3: Using Set (Not Optimal but Shows Alternative)
# Time: O(n²), Space: O(n) for set
# ============================================================================
def threeSumWithSet(nums: List[int]) -> List[List[int]]:
    """
    Strategy: Use set to track seen pairs

    This is less efficient than pure two pointers but shows
    how to use hash set for pair detection.
    """
    nums.sort()
    result: List[List[int]] = []
    n = len(nums)

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        seen = set()
        for j in range(i + 1, n):
            complement = -nums[i] - nums[j]

            if complement in seen:
                result.append([nums[i], complement, nums[j]])

                # Skip duplicates for j
                while j + 1 < n and nums[j] == nums[j + 1]:
                    j += 1

            seen.add(nums[j])

    return result


# ============================================================================
# DRY RUN EXAMPLE
# ============================================================================
def dry_run_three_sum() -> List[List[int]]:
    """
    Detailed walkthrough of 3Sum
    """
    nums = [-1, 0, 1, 2, -1, -4]

    print("\n" + "="*60)
    print("DRY RUN: 3Sum")
    print("="*60)
    print(f"Input: {nums}\n")

    # Step 1: Sort
    nums.sort()
    print(f"After sorting: {nums}\n")

    result: List[List[int]] = []
    n = len(nums)

    for i in range(n - 2):
        print(f"{'='*50}")
        print(f"Iteration i={i}, nums[i]={nums[i]}")

        # Skip duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            print(f"  ⏭ Skip duplicate: nums[{i}]={nums[i]} == nums[{i-1}]={nums[i-1]}")
            continue

        left = i + 1
        right = n - 1
        target = -nums[i]

        print(f"  Target for two pointers: {target}")
        print(f"  Searching in: {nums[left:right+1]}")

        step = 1
        while left < right:
            current_sum = nums[left] + nums[right]

            print(f"\n  Step {step}:")
            print(f"    Pointers: left={left}, right={right}")
            print(f"    Values: nums[{left}]={nums[left]}, nums[{right}]={nums[right]}")
            print(f"    Sum: {nums[left]} + {nums[right]} = {current_sum}, target={target}")

            if current_sum == target:
                triplet = [nums[i], nums[left], nums[right]]
                result.append(triplet)
                print(f"    ✓ Found triplet: {triplet}")

                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif current_sum < target:
                print(f"    → Sum too small, left++")
                left += 1
            else:
                print(f"    → Sum too large, right--")
                right -= 1

            step += 1

        print()

    print(f"{'='*50}")
    print(f"Final result: {result}")
    return result


# ============================================================================
# WHY THIS WORKS
# ============================================================================
def why_this_works() -> None:
    """
    Explanation of why fix + two pointers works
    """
    print("\n" + "="*60)
    print("WHY FIX + TWO POINTERS WORKS")
    print("="*60)

    print("""
Problem: Find three numbers that sum to 0

Reduction to Two Sum:
- Fix first number: nums[i]
- Need to find two numbers that sum to -nums[i]
- This is just Two Sum II on sorted array!

Why we need to sort:
- Two pointers only works on SORTED arrays
- Allows us to decide which pointer to move

Why O(n²):
- Outer loop: O(n) iterations (fix first element)
- Inner loop: O(n) two pointers for each outer iteration
- Total: O(n) × O(n) = O(n²)

Why skip duplicates:
- Without skipping: [-1, -1, 2] appears twice
- Solution set must not have duplicates
- Skip duplicate i values
- Skip duplicate left/right values after finding triplet

Key Invariant:
- For fixed nums[i], we've checked all valid pairs (left, right)
- No triplet is missed because two pointers explores all combinations

Complexity:
Time: O(n²) - sort O(n log n) + nested loops O(n²)
Space: O(1) - only pointers (excluding output array)

Pattern: Fixed Element + Two Pointers
- Fix one dimension
- Use two pointers on remaining dimension
- Extends to 4Sum, 5Sum, etc (with more nesting)
    """)


# ============================================================================
# DUPLICATE HANDLING DEEP DIVE
# ============================================================================
def duplicate_handling_explained() -> None:
    """
    Critical explanation of how to handle duplicates
    """
    print("\n" + "="*60)
    print("DUPLICATE HANDLING (CRITICAL!)")
    print("="*60)

    print("""
Why duplicates are tricky:
Array: [-2, -1, -1, -1, 3, 3, 3]

Without skipping duplicates:
- [-2, -1, 3] appears MULTIPLE times
- Wrong! Solution set must be unique

Three places to skip duplicates:

1. Skip duplicate i (outer loop):
   ✓ Correct:
   if i > 0 and nums[i] == nums[i-1]:
       continue

   ❌ Wrong:
   if i < n-1 and nums[i] == nums[i+1]:  # Skips too early!

2. Skip duplicate left (after finding triplet):
   while left < right and nums[left] == nums[left+1]:
       left += 1

3. Skip duplicate right (after finding triplet):
   while left < right and nums[right] == nums[right-1]:
       right -= 1

Visual Example:
[-2, -1, -1, -1, 3, 3, 3]
  ↑   ↑           ↑
  i   L           R

Found triplet: [-2, -1, 3]

Now skip all duplicate -1's and 3's:
[-2, -1, -1, -1, 3, 3, 3]
  ↑          ↑   ↑
  i          L   R (after skipping)

IMPORTANT: Must move BOTH pointers after finding triplet!
If you only move one, you might find the same triplet again.
    """)


# ============================================================================
# COMMON MISTAKES
# ============================================================================
def common_mistakes() -> None:
    """
    Demonstrate common bugs in 3Sum
    """
    print("\n" + "="*60)
    print("COMMON MISTAKES")
    print("="*60)

    print("""
❌ Mistake 1: Forgetting to sort
   # Without sorting, two pointers won't work!
   result = []
   for i in range(n):
       left, right = i+1, n-1
       # This fails on unsorted array!

   ✓ Fix: nums.sort() FIRST!

❌ Mistake 2: Wrong duplicate check for i
   if i < n-1 and nums[i] == nums[i+1]:  # WRONG! Skips first occurrence
       continue

   ✓ Fix: Check previous, not next
   if i > 0 and nums[i] == nums[i-1]:

❌ Mistake 3: Not skipping duplicates for left/right
   if current_sum == target:
       result.append([nums[i], nums[left], nums[right]])
       left += 1  # WRONG! Might add duplicate triplets
       right -= 1

   ✓ Fix: Skip all duplicates
   while left < right and nums[left] == nums[left+1]:
       left += 1
   while left < right and nums[right] == nums[right-1]:
       right -= 1
   left += 1
   right -= 1

❌ Mistake 4: Not moving both pointers
   if current_sum == target:
       # ... skip duplicates ...
       left += 1  # WRONG! Only moving one

   ✓ Fix: Move BOTH after finding triplet
   left += 1
   right -= 1

❌ Mistake 5: Using left <= right
   while left <= right:  # WRONG! Can use same element twice

   ✓ Fix: Use strict inequality
   while left < right:

❌ Mistake 6: Range error in outer loop
   for i in range(n):  # WRONG! Need 3 elements

   ✓ Fix: Leave room for left and right
   for i in range(n - 2):
    """)


# ============================================================================
# TEST CASES
# ============================================================================
def run_tests() -> None:
    test_cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
        ([1, 2, -2, -1], []),
    ]

    print("\n" + "="*60)
    print("Testing: 3Sum")
    print("="*60)

    all_passed = True
    for nums, expected in test_cases:
        result = threeSum(nums.copy())

        # Sort for comparison (order doesn't matter)
        result_sorted = sorted([sorted(triplet) for triplet in result])
        expected_sorted = sorted([sorted(triplet) for triplet in expected])

        status = "✅" if result_sorted == expected_sorted else "❌"
        if result_sorted != expected_sorted:
            all_passed = False

        print(f"{status} Input: {nums}")
        print(f"   Output: {result}")
        print(f"   Expected: {expected}")
        print()

    if all_passed:
        print("✅ All tests passed!")


if __name__ == "__main__":
    print("LeetCode #15: 3Sum\n")
    print("⭐ Two Pointers Pattern: Fixed + Opposite Direction")
    print("="*60)

    # Dry run
    dry_run_three_sum()

    # Run tests
    run_tests()

    # Explanations
    why_this_works()
    duplicate_handling_explained()

    # Common mistakes
    common_mistakes()

    print("\n" + "="*60)
    print("KEY TAKEAWAYS")
    print("="*60)
    print("""
1. 3Sum = Fix one + Two Sum II on rest
2. MUST sort array first (critical for two pointers!)
3. Skip duplicates in THREE places (i, left, right)
4. Move BOTH pointers after finding triplet
5. Time O(n²) - best possible without using hash map

Decision Tree:
- Fix nums[i]
- For each nums[i]:
  - Use two pointers to find pair summing to -nums[i]
  - Skip duplicates at all levels

Interview Strategy:
1. Explain reduction to Two Sum
2. Emphasize sorting is critical
3. Walk through duplicate handling carefully
4. Code with clear duplicate skipping
5. Test with duplicate-heavy case: [-1,-1,-1,0,1,1,1]
6. Mention O(n²) is optimal without extra space

Related Problems:
- LC #1: Two Sum (hash map)
- LC #167: Two Sum II (sorted, two pointers)
- LC #16: 3Sum Closest (same pattern, track closest)
- LC #18: 4Sum (triple nested)
- LC #259: 3Sum Smaller (count instead of collect)

This is a TOP interview question - master it!
    """)
