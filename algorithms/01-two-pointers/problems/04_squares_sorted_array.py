"""
LeetCode #977: Squares of a Sorted Array
Difficulty: Easy
Pattern: Two Pointers (Opposite Direction)

Problem:
Given an integer array nums sorted in non-decreasing order, return an array
of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, [16,1,0,9,100]. After sorting, [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums is sorted in non-decreasing order

Follow-up: Can you solve it in O(n) time?
"""

from typing import List


# ============================================================================
# Approach 1: Two Pointers (Opposite Direction) - OPTIMAL
# Time: O(n), Space: O(n) for output
# ============================================================================
def sortedSquares(nums: List[int]) -> List[int]:
    """
    Strategy: Compare absolute values from both ends

    Key Insight:
    - After squaring, largest values come from BOTH ENDS (not middle!)
    - Negative numbers with large absolute value give large squares
    - Positive numbers with large value give large squares
    - Smallest squares are near 0 (middle of original array)

    Analogy: "Two mountains (negative and positive), merge from peaks down."

    [-4, -1, 0, 3, 10]
      ↑           ↑
      L           R

    Compare |-4| vs |10|:
    - 10 is larger → result[end] = 10²
    - R--
    """
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    write_pos = n - 1  # Fill result from right to left (largest first)

    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        if left_square > right_square:
            result[write_pos] = left_square
            left += 1
        else:
            result[write_pos] = right_square
            right -= 1

        write_pos -= 1

    return result


# ============================================================================
# Approach 2: Find Pivot + Merge (Alternative O(n))
# Time: O(n), Space: O(n)
# ============================================================================
def sortedSquaresPivot(nums: List[int]) -> List[int]:
    """
    Strategy: Find the pivot (closest to 0), then merge like merge sort

    Steps:
    1. Find index where value changes from negative to positive
    2. Use two pointers to merge negatives (reverse) and positives

    This is more complex but shows the merge pattern clearly.
    """
    n = len(nums)

    # Find pivot - first non-negative number
    pivot = 0
    while pivot < n and nums[pivot] < 0:
        pivot += 1

    # Two pointers: neg goes left (negatives), pos goes right (positives)
    neg = pivot - 1
    pos = pivot
    result = []

    # Merge two sorted lists (negatives squared, positives squared)
    while neg >= 0 and pos < n:
        neg_square = nums[neg] ** 2
        pos_square = nums[pos] ** 2

        if neg_square < pos_square:
            result.append(neg_square)
            neg -= 1
        else:
            result.append(pos_square)
            pos += 1

    # Add remaining negatives
    while neg >= 0:
        result.append(nums[neg] ** 2)
        neg -= 1

    # Add remaining positives
    while pos < n:
        result.append(nums[pos] ** 2)
        pos += 1

    return result


# ============================================================================
# Approach 3: Brute Force (Baseline)
# Time: O(n log n), Space: O(n)
# ============================================================================
def sortedSquaresBrute(nums: List[int]) -> List[int]:
    """
    Strategy: Square all, then sort

    Simple but doesn't leverage the fact that input is already sorted.
    """
    return sorted(num ** 2 for num in nums)


# ============================================================================
# DRY RUN EXAMPLE
# ============================================================================
def dry_run_sorted_squares() -> List[int]:
    """
    Detailed walkthrough of two pointers approach
    """
    nums = [-4, -1, 0, 3, 10]

    print("\n" + "="*60)
    print("DRY RUN: Squares of Sorted Array")
    print("="*60)
    print(f"Input: {nums}\n")

    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    write_pos = n - 1

    print(f"Strategy: Fill from right to left (largest squares first)\n")

    step = 1
    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        print(f"Step {step}:")
        print(f"  Left: nums[{left}] = {nums[left]}, square = {left_square}")
        print(f"  Right: nums[{right}] = {nums[right]}, square = {right_square}")

        if left_square > right_square:
            result[write_pos] = left_square
            print(f"  ✓ Left square is larger")
            print(f"  Action: result[{write_pos}] = {left_square}, left++")
            left += 1
        else:
            result[write_pos] = right_square
            print(f"  ✓ Right square is larger or equal")
            print(f"  Action: result[{write_pos}] = {right_square}, right--")
            right -= 1

        write_pos -= 1
        print(f"  Result so far: {result}")
        print()
        step += 1

    print(f"Final result: {result}")
    return result


# ============================================================================
# WHY THIS WORKS
# ============================================================================
def why_this_works() -> None:
    """
    Explanation of why we fill from right to left
    """
    print("\n" + "="*60)
    print("WHY FILL FROM RIGHT TO LEFT?")
    print("="*60)

    print("""
Key Observation: Largest squares come from ENDS, not middle!

Example: [-4, -1, 0, 3, 10]
         Squares: [16, 1, 0, 9, 100]

After squaring (unsorted): [16, 1, 0, 9, 100]
                            ↑              ↑
                         Large          Large

Smallest value (0) is in the MIDDLE!

Why ends have largest?
- Array is sorted: smallest...largest
- Negative numbers: more negative → larger square
  Example: -10 → 100, -1 → 1
- Positive numbers: larger → larger square
  Example: 10 → 100, 1 → 1

Greedy Choice:
- At each step, pick the larger square from ends
- Place it at the END of result array
- This builds result in descending order from right

Invariant:
- result[write_pos+1..n-1] contains largest squares in sorted order
- One of nums[left] or nums[right] has next largest square

Time: O(n) - single pass
Space: O(n) - result array

Pattern: Opposite Direction Two Pointers + Fill from End
    """)


# ============================================================================
# COMPARISON WITH MERGE APPROACH
# ============================================================================
def compare_approaches() -> None:
    """
    Compare the two O(n) approaches
    """
    print("\n" + "="*60)
    print("APPROACH COMPARISON")
    print("="*60)

    print("""
Approach 1: Fill from Right (Recommended)
Pros:
✅ More intuitive (largest from ends)
✅ Simpler code (one loop)
✅ Direct construction

Cons:
❌ None significant

Approach 2: Pivot + Merge
Pros:
✅ Shows merge pattern clearly
✅ Good for understanding merge technique

Cons:
❌ More complex (find pivot + merge)
❌ More code
❌ Two separate loops

Both are O(n) time and O(n) space!

Choose Approach 1 for interviews - simpler and cleaner.
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
❌ Mistake 1: Filling from left to right
   write_pos = 0  # WRONG!
   while left <= right:
       # Pick larger, put at write_pos
       write_pos += 1

   Problem: We know LARGEST squares are at ends, not smallest!
   ✓ Fix: Fill from right to left (write_pos = n-1, write_pos--)

❌ Mistake 2: Using < instead of <=
   while left < right:  # WRONG! Misses middle element

   ✓ Fix: while left <= right

❌ Mistake 3: Not handling all negatives or all positives
   # Works when both negative and positive exist
   # Fails when all negative: [-5, -3, -1]

   ✓ Fix: Use <= not <, handles all cases

❌ Mistake 4: Comparing values instead of squares
   if abs(nums[left]) > abs(nums[right]):  # Works but unnecessary

   ✓ Better: Compare squares directly
   if left_square > right_square:

❌ Mistake 5: Modifying input array
   nums[i] = nums[i] ** 2  # WRONG! Loses original values needed for comparison

   ✓ Fix: Create new result array
    """)


# ============================================================================
# EDGE CASES
# ============================================================================
def test_edge_cases() -> None:
    """
    Important edge cases to consider
    """
    print("\n" + "="*60)
    print("EDGE CASES")
    print("="*60)

    edge_cases = [
        # (input, expected, description)
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100], "Mix of negative and positive"),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121], "Duplicates after squaring"),
        ([-5, -3, -2, -1], [1, 4, 9, 25], "All negative"),
        ([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], "All positive"),
        ([0], [0], "Single zero"),
        ([-1], [1], "Single negative"),
        ([5], [25], "Single positive"),
        ([-2, 0, 2], [0, 4, 4], "Symmetric around zero"),
    ]

    for nums, expected, desc in edge_cases:
        result = sortedSquares(nums)
        status = "✅" if result == expected else "❌"
        print(f"{status} {desc}")
        print(f"   Input: {nums}")
        print(f"   Output: {result}, Expected: {expected}")
        print()


# ============================================================================
# TEST CASES
# ============================================================================
def run_tests() -> None:
    test_cases = [
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
        ([-5, -3, -2, -1], [1, 4, 9, 25]),
        ([1, 2, 3, 4, 5], [1, 4, 9, 16, 25]),
    ]

    approaches = [
        ("Two Pointers (Fill Right)", sortedSquares),
        ("Pivot + Merge", sortedSquaresPivot),
        ("Brute Force", sortedSquaresBrute),
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
    print("LeetCode #977: Squares of a Sorted Array\n")
    print("⭐ Two Pointers Pattern: Opposite Direction")
    print("="*60)

    # Dry run
    dry_run_sorted_squares()

    # Run tests
    run_tests()

    # Test edge cases
    test_edge_cases()

    # Why it works
    why_this_works()

    # Compare approaches
    compare_approaches()

    # Common mistakes
    common_mistakes()

    print("\n" + "="*60)
    print("KEY TAKEAWAYS")
    print("="*60)
    print("""
1. Largest squares come from ENDS (negative or positive extremes)
2. Fill result from RIGHT TO LEFT (largest first)
3. Greedy choice: pick larger square from ends each step
4. Use two pointers from opposite ends
5. O(n) time using two pointers vs O(n log n) sorting

Decision Rule:
- Compare squares from both ends
- Pick larger square
- Move that pointer inward
- Fill result from right

Interview Strategy:
1. Observe that largest squares are at ENDS
2. Explain greedy approach (fill from right)
3. Code two pointers solution
4. Mention time O(n) vs naive O(n log n)
5. Test with all negative, all positive, mixed

Related Problems:
- LC #88: Merge Sorted Array (similar fill from right)
- LC #349: Intersection of Two Arrays
- LC #986: Interval List Intersections
    """)
