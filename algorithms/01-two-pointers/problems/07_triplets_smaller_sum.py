"""
GeeksForGeeks: Count Triplets with Sum Smaller than X
LeetCode #259: 3Sum Smaller (Premium)
Difficulty: Medium
Pattern: Two Pointers (Fixed + Opposite Direction)

Problem:
Given an array arr[] of distinct integers of size N and a value sum, the task is
to find the count of triplets (i, j, k), having (i < j < k) with the sum of
(arr[i] + arr[j] + arr[k]) smaller than the given value sum.

Example 1:
Input: N = 4, sum = 2
arr[] = {-2, 0, 1, 3}
Output:  2
Explanation: Below are triplets with sum less than 2:
(-2, 0, 1), (-2, 0, 3)

Example 2:
Input: N = 5, sum = 12
arr[] = {5, 1, 3, 4, 7}
Output: 4
Explanation: Below are triplets with sum less than 12:
(1, 3, 4), (1, 3, 5), (1, 3, 7), (1, 4, 5)

Constraints:
- 3 <= N <= 10^3
- -10^3 <= arr[i] <= 10^3
"""

from typing import List


# ============================================================================
# Approach 1: Two Pointers - Count Combinations - OPTIMAL
# Time: O(n²), Space: O(1)
# ============================================================================
def countTripletsFixed(nums: List[int], target: int) -> int:
    """
    Strategy: Fix + Two Pointers + Count combinations

    Key Insight:
    When sum < target, ALL elements between left and right are valid!

    Example:
    nums = [1, 2, 3, 4, 5], i=0 (nums[i]=1), target=12
                ↑        ↑
                L        R

    If nums[0] + nums[1] + nums[5] = 1 + 2 + 5 = 8 < 12:
    - (1, 2, 5) works ✓
    - (1, 3, 5) works ✓  (replace 2 with 3)
    - (1, 4, 5) works ✓  (replace 2 with 4)

    Number of valid combinations = R - L
    """
    nums.sort()
    n = len(nums)
    count = 0

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum < target:
                # KEY: ALL combinations with right are valid!
                # We can pair nums[i] with any element from left to right-1
                # and still get sum < target
                count += (right - left)
                left += 1
            else:
                # Sum too large, need smaller
                right -= 1

    return count


# ============================================================================
# Approach 2: Collect All Triplets (Less Efficient)
# Time: O(n²), Space: O(k) where k is number of triplets
# ============================================================================
def countTripletsCollect(nums: List[int], target: int) -> List[List[int]]:
    """
    Strategy: Actually collect all triplets (for debugging/verification)

    Returns the triplets themselves, not just count
    """
    nums.sort()
    n = len(nums)
    result: List[List[int]] = []

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum < target:
                # Add all combinations
                for k in range(left, right):
                    result.append([nums[i], nums[k], nums[right]])
                right -= 1
            else:
                right -= 1

    return result


# ============================================================================
# Approach 3: Explicit Counting (More Intuitive)
# Time: O(n²), Space: O(1)
# ============================================================================
def countTripletsExplicit(nums: List[int], target: int) -> int:
    """
    Strategy: Count each valid combination explicitly

    Less efficient but easier to understand
    """
    nums.sort()
    n = len(nums)
    count = 0

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] < target:
                    count += 1
                else:
                    break  # Since sorted, all further k will be larger

    return count


# ============================================================================
# DRY RUN EXAMPLE
# ============================================================================
def dry_run_triplets_smaller() -> int:
    """
    Detailed walkthrough showing the counting logic
    """
    nums = [-2, 0, 1, 3]
    target = 2

    print("\n" + "="*60)
    print("DRY RUN: Count Triplets with Sum < Target")
    print("="*60)
    print(f"Input: nums = {nums}, target = {target}\n")

    nums.sort()
    print(f"After sorting: {nums}\n")

    n = len(nums)
    count = 0

    for i in range(n - 2):
        print(f"{'='*50}")
        print(f"Fixed: i={i}, nums[i]={nums[i]}")

        left = i + 1
        right = n - 1

        step = 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            print(f"\nStep {step}:")
            print(f"  Pointers: left={left}, right={right}")
            print(f"  Values: nums[{i}]={nums[i]}, nums[{left}]={nums[left]}, nums[{right}]={nums[right]}")
            print(f"  Sum: {current_sum}, Target: {target}")

            if current_sum < target:
                # Count all valid combinations
                valid_count = right - left
                print(f"  ✓ Sum < target!")
                print(f"  Valid combinations with right={right}:")

                # Show all valid combinations
                for k in range(left, right):
                    triplet = [nums[i], nums[k], nums[right]]
                    triplet_sum = sum(triplet)
                    print(f"    {triplet} → sum = {triplet_sum}")

                print(f"  → Add {valid_count} to count (right - left = {right} - {left})")
                count += valid_count
                left += 1
            else:
                print(f"  ✗ Sum >= target, right--")
                right -= 1

            print(f"  Running count: {count}")
            step += 1

    print(f"\n{'='*50}")
    print(f"Final count: {count}")
    return count


# ============================================================================
# WHY THE COUNTING WORKS
# ============================================================================
def why_counting_works() -> None:
    """
    Explain the key insight behind counting
    """
    print("\n" + "="*60)
    print("WHY COUNTING (right - left) WORKS")
    print("="*60)

    print("""
The Magic Formula: count += (right - left)

Why this works:

Sorted array: [1, 2, 3, 4, 5]
Fixed i=0 (nums[i]=1), target=12

Current state:
   [1, 2, 3, 4, 5]
    ↑  ↑        ↑
    i  L        R

Sum = 1 + 2 + 5 = 8 < 12 ✓

Since array is SORTED and sum < target:
- (1, 2, 5) works ✓
- If we replace 2 with ANY element between 2 and 5, sum stays < target!
- (1, 3, 5) = 9 < 12 ✓
- (1, 4, 5) = 10 < 12 ✓

Number of such combinations = right - left = 4 - 1 = 3

Visual:
[1, 2, 3, 4, 5]
    ↑  ↑  ↑  ↑
    All these can pair with 5!

Key Insight:
- Since sorted, nums[left] ≤ nums[left+1] ≤ ... ≤ nums[right-1]
- If nums[i] + nums[left] + nums[right] < target
- Then nums[i] + nums[k] + nums[right] < target for all k in [left, right-1]
- Because nums[k] ≤ nums[right-1] < nums[right]

After counting, move left pointer:
- We've counted all combinations with current left
- Move to next left to explore new combinations

This is the KEY difference from 3Sum!
- 3Sum: Find exact matches
- 3Sum Smaller: Count ALL valid combinations
    """)


# ============================================================================
# COMPARISON WITH 3SUM
# ============================================================================
def compare_with_three_sum() -> None:
    """
    Compare with 3Sum pattern
    """
    print("\n" + "="*60)
    print("COMPARISON: 3Sum vs 3Sum Smaller")
    print("="*60)

    print("""
┌──────────────────┬─────────────────────┬──────────────────────┐
│ Aspect           │ 3Sum                │ 3Sum Smaller         │
├──────────────────┼─────────────────────┼──────────────────────┤
│ Goal             │ sum == target       │ sum < target         │
│ Return           │ Unique triplets     │ Count                │
│ When match       │ Collect and skip    │ Count combinations   │
│ Duplicates       │ Must skip           │ Don't need to skip   │
│ Counting formula │ N/A                 │ count += right-left  │
└──────────────────┴─────────────────────┴──────────────────────┘

Shared Pattern:
✓ Fix first element
✓ Two pointers on remaining
✓ Sort array first
✓ O(n²) time complexity

Key Difference:
3Sum: if sum == target: add triplet
3Sum Smaller: if sum < target: count += (right - left)

Why the difference?
- 3Sum: Looking for EXACT match (rare)
- 3Sum Smaller: Looking for range (many matches)
- When sum < target in sorted array, MANY combinations work!
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
❌ Mistake 1: Counting only one when sum < target
   if current_sum < target:
       count += 1  # WRONG! Misses many combinations
       left += 1

   ✓ Fix: Count all combinations
   count += (right - left)

❌ Mistake 2: Moving wrong pointer
   if current_sum < target:
       count += (right - left)
       right -= 1  # WRONG! Should move left

   ✓ Fix: Move left when sum < target
   left += 1

❌ Mistake 3: Forgetting to sort
   # Two pointers and counting logic requires sorted array!
   count = 0
   for i in range(n):
       # This fails without sorting

   ✓ Fix: nums.sort()

❌ Mistake 4: Wrong counting formula
   count += right  # WRONG!
   count += (right - left - 1)  # WRONG!

   ✓ Fix: count += (right - left)

❌ Mistake 5: Using >= instead of <
   if current_sum <= target:  # WRONG! Problem asks for STRICTLY less

   ✓ Fix: if current_sum < target:

❌ Mistake 6: Triple nested loop without optimization
   for i in range(n):
       for j in range(i+1, n):
           for k in range(j+1, n):  # O(n³)!

   ✓ Fix: Use two pointers (O(n²))
    """)


# ============================================================================
# TEST CASES
# ============================================================================
def run_tests() -> None:
    test_cases = [
        ([-2, 0, 1, 3], 2, 2),  # (-2,0,1), (-2,0,3)
        ([5, 1, 3, 4, 7], 12, 4),  # (1,3,4), (1,3,5), (1,3,7), (1,4,5)
        ([1, 1, 1], 4, 1),  # (1,1,1)
        ([-1, 0, 2, 3], 3, 2),  # (-1,0,2), (-1,0,3)
        ([0, -1, 2, -3, 1], 0, 5),
    ]

    print("\n" + "="*60)
    print("Testing: Count Triplets with Sum < Target")
    print("="*60)

    all_passed = True
    for nums, target, expected in test_cases:
        result = countTripletsFixed(nums.copy(), target)
        status = "✅" if result == expected else "❌"
        if result != expected:
            all_passed = False

        print(f"{status} Input: nums={nums}, target={target}")
        print(f"   Output: {result}, Expected: {expected}")

    if all_passed:
        print("\n✅ All tests passed!")


if __name__ == "__main__":
    print("Count Triplets with Sum Smaller than Target\n")
    print("⭐ Two Pointers Pattern: Fixed + Opposite Direction + Counting")
    print("="*60)

    # Dry run
    dry_run_triplets_smaller()

    # Run tests
    run_tests()

    # Explanations
    why_counting_works()
    compare_with_three_sum()

    # Common mistakes
    common_mistakes()

    print("\n" + "="*60)
    print("KEY TAKEAWAYS")
    print("="*60)
    print("""
1. Similar to 3Sum, but COUNT instead of collect
2. Key formula: count += (right - left) when sum < target
3. This counts ALL valid combinations in O(1)
4. Move left pointer after counting (not right!)
5. Must sort array first for counting logic to work

Decision Rule:
- sum < target → count += (right - left), left++
- sum >= target → right--

Why it's brilliant:
- Sorted array means ALL elements between left and right-1
  will also form valid triplets with current right
- Count them all in O(1) instead of iterating!

Interview Strategy:
1. Recognize as 3Sum variant
2. Explain the counting insight (key differentiator!)
3. Draw diagram showing why (right - left) works
4. Code carefully (easy to mess up pointer movement)
5. Test with small example to verify counting

Common Pitfalls:
❌ Counting += 1 instead of += (right - left)
❌ Moving right instead of left when sum < target
❌ Using <= instead of < for comparison
✓ Remember: sum < target → many combinations!
✓ Count them all at once with (right - left)

Related Problems:
- LC #15: 3Sum (exact match)
- LC #16: 3Sum Closest (find closest)
- LC #259: 3Sum Smaller (this problem)
- LC #611: Valid Triangle Number (similar counting)

Master this counting technique - appears in many problems!
    """)
