"""
LeetCode #75: Sort Colors (Dutch National Flag Problem)
Difficulty: Medium
Pattern: Three Pointers (Partitioning)

Problem:
Given an array nums with n objects colored red, white, or blue, sort them
in-place so that objects of the same color are adjacent, with the colors in
the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and
blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:
- n == nums.length
- 1 <= n <= 300
- nums[i] is either 0, 1, or 2

Follow-up: Could you come up with a one-pass algorithm using only O(1) space?
"""

from typing import List


# ============================================================================
# Approach 1: Three Pointers (Dutch National Flag) - OPTIMAL
# Time: O(n), Space: O(1)
# ============================================================================
def sortColors(nums: List[int]) -> None:
    """
    Strategy: Three pointers to partition into 3 groups

    Pointers:
    - low: boundary for 0s (everything before low is 0)
    - mid: current element being examined
    - high: boundary for 2s (everything after high is 2)

    Invariant:
    [0, 0, ..., 0, 1, 1, ..., 1, ?, ?, ..., ?, 2, 2, ..., 2]
     ^             ^             ^             ^
     0            low           mid           high    n-1

    Regions:
    - [0, low): all 0s
    - [low, mid): all 1s
    - [mid, high]: unknown (being processed)
    - (high, n-1]: all 2s
    """
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            # Swap with low, both low and mid move forward
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            # Already in correct position, just move mid
            mid += 1

        else:  # nums[mid] == 2
            # Swap with high, only high moves backward
            # Don't move mid! We need to examine the swapped element
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


# ============================================================================
# Approach 2: Two Pass (Count and Fill)
# Time: O(n), Space: O(1)
# ============================================================================
def sortColorsTwoPass(nums: List[int]) -> None:
    """
    Strategy: Count each color, then overwrite array

    Simple but requires two passes
    """
    count0 = count1 = count2 = 0

    # First pass: count
    for num in nums:
        if num == 0:
            count0 += 1
        elif num == 1:
            count1 += 1
        else:
            count2 += 1

    # Second pass: fill
    idx = 0
    for _ in range(count0):
        nums[idx] = 0
        idx += 1
    for _ in range(count1):
        nums[idx] = 1
        idx += 1
    for _ in range(count2):
        nums[idx] = 2
        idx += 1


# ============================================================================
# DRY RUN EXAMPLE
# ============================================================================
def dry_run_sort_colors() -> None:
    """
    Detailed walkthrough of Dutch National Flag algorithm
    """
    nums = [2, 0, 2, 1, 1, 0]

    print("\n" + "="*60)
    print("DRY RUN: Dutch National Flag (Sort Colors)")
    print("="*60)
    print(f"Input: {nums}\n")

    print("Invariant:")
    print("[0's | 1's | unknown | 2's]")
    print(" ^     ^      ^        ^")
    print(" 0    low    mid     high  n-1\n")

    low = 0
    mid = 0
    high = len(nums) - 1

    step = 1
    while mid <= high:
        print(f"Step {step}:")
        print(f"  Array: {nums}")
        print(f"  Pointers: low={low}, mid={mid}, high={high}")
        print(f"  nums[mid] = {nums[mid]}")

        if nums[mid] == 0:
            print(f"  ✓ Found 0 at mid")
            print(f"  Action: Swap nums[{mid}] and nums[{low}], low++, mid++")
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            print(f"  ✓ Found 1 at mid (already correct)")
            print(f"  Action: mid++")
            mid += 1

        else:  # nums[mid] == 2
            print(f"  ✓ Found 2 at mid")
            print(f"  Action: Swap nums[{mid}] and nums[{high}], high--")
            print(f"  Note: Don't move mid! Need to check swapped element")
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

        print(f"  Result: {nums}")
        print()
        step += 1

    print(f"Final result: {nums}")


# ============================================================================
# WHY THIS WORKS
# ============================================================================
def why_this_works() -> None:
    """
    Explanation of the algorithm correctness
    """
    print("\n" + "="*60)
    print("WHY DUTCH NATIONAL FLAG WORKS")
    print("="*60)

    print("""
The Invariant (maintained at all times):

[0, 0, ..., 0, 1, 1, ..., 1, ?, ?, ..., ?, 2, 2, ..., 2]
 ↑             ↑             ↑             ↑
 0            low           mid           high    n-1

Regions:
1. [0, low): All 0s ✓
2. [low, mid): All 1s ✓
3. [mid, high]: Unknown (being processed)
4. (high, n-1]: All 2s ✓

Decision Rules:

Case 1: nums[mid] == 0
- Belongs in region 1
- Swap with low boundary
- Expand 0s region: low++
- We know nums[low] was 1, so mid can advance: mid++

Case 2: nums[mid] == 1
- Already in correct position (region 2)
- Just advance: mid++

Case 3: nums[mid] == 2
- Belongs in region 4
- Swap with high boundary
- Expand 2s region: high--
- CRITICAL: Don't move mid!
  Why? We don't know what nums[high] was!
  It could be 0, 1, or 2. Must examine it next iteration.

Termination:
- When mid > high, no unknown region left
- All elements are partitioned

Time: O(n) - single pass, each element visited once
Space: O(1) - only three pointers

This is called "Dutch National Flag" because:
- Netherlands flag has 3 horizontal stripes (red, white, blue)
- This algorithm partitions into 3 groups
- Invented by Edsger Dijkstra (Dutch computer scientist)
    """)


# ============================================================================
# KEY INSIGHT: WHY mid DOESN'T ADVANCE WITH 2
# ============================================================================
def why_mid_doesnt_advance() -> None:
    """
    Critical explanation of asymmetric pointer movement
    """
    print("\n" + "="*60)
    print("CRITICAL: WHY mid DOESN'T ADVANCE WHEN SWAPPING WITH high")
    print("="*60)

    print("""
This is the #1 source of bugs!

When nums[mid] == 0:
  - Swap with nums[low]
  - We KNOW nums[low] is in [low, mid) region
  - [low, mid) region contains only 1s (by invariant)
  - So nums[low] was definitely 1
  - After swap: nums[mid] = 1 (correct position)
  - Safe to advance mid++

When nums[mid] == 2:
  - Swap with nums[high]
  - We DON'T KNOW what nums[high] is!
  - nums[high] is in unknown region
  - It could be 0, 1, or 2
  - After swap: nums[mid] = ??? (need to check)
  - NOT safe to advance mid!
  - Must examine it in next iteration

Example showing the bug:
nums = [2, 0, 1]
         ↑  ↑
        m/h

If we advance mid after swapping with high:
- Swap nums[0] and nums[2]: [1, 0, 2]
- mid++ → mid = 1
- But nums[1] = 0, we never examined it!
- Final: [1, 0, 2] ✗ WRONG!

Correct behavior:
- Swap nums[0] and nums[2]: [1, 0, 2]
- high-- → high = 1
- Don't advance mid!
- Next iteration: nums[mid]=1, mid++
- Next iteration: nums[mid]=0, swap with low
- Final: [0, 1, 2] ✓ CORRECT!
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
❌ Mistake 1: Advancing mid when swapping with high
   if nums[mid] == 2:
       nums[mid], nums[high] = nums[high], nums[mid]
       high -= 1
       mid += 1  # WRONG! Don't advance mid!

   ✓ Fix: Only move high
   high -= 1  # mid stays!

❌ Mistake 2: Using mid < high instead of mid <= high
   while mid < high:  # WRONG! Misses element at high

   ✓ Fix: while mid <= high

❌ Mistake 3: Swapping with wrong pointers
   if nums[mid] == 0:
       nums[mid], nums[high] = nums[high], nums[mid]  # WRONG!

   ✓ Fix: Swap 0 with low, not high
   nums[mid], nums[low] = nums[low], nums[mid]

❌ Mistake 4: Not advancing low when swapping 0
   if nums[mid] == 0:
       nums[mid], nums[low] = nums[low], nums[mid]
       mid += 1  # WRONG! Forgot low++

   ✓ Fix: Advance both
   low += 1
   mid += 1

❌ Mistake 5: Initializing high to len(nums)
   high = len(nums)  # WRONG! Out of bounds

   ✓ Fix: high = len(nums) - 1

❌ Mistake 6: Using if-elif-elif instead of if-elif-else
   # Minor but if-elif-else is clearer
   # Shows exhaustive cases: 0, 1, 2

   ✓ Use: if-elif-else
    """)


# ============================================================================
# PATTERN EXTENSION
# ============================================================================
def pattern_extension() -> None:
    """
    How to extend to k colors
    """
    print("\n" + "="*60)
    print("EXTENSION: Sorting K Colors")
    print("="*60)

    print("""
This problem: k = 3 (colors 0, 1, 2)

General approach for k colors:
1. Use counting sort (two passes)
2. Or generalized partitioning (more complex)

For k = 2 (0s and 1s):
- Only need one partition point
- Same as "Segregate 0s and 1s"
- Even simpler than k=3

For k = 3 (this problem):
- Dutch National Flag (optimal)
- Three regions, three pointers

For k > 3:
- Dutch National Flag becomes complex
- Better to use counting sort or quicksort partitioning
- Or bucket sort if range is known

This problem is special because k=3 is perfect for three pointers!
    """)


# ============================================================================
# TEST CASES
# ============================================================================
def run_tests() -> None:
    test_cases = [
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2]),
        ([0], [0]),
        ([1], [1]),
        ([2, 1, 0], [0, 1, 2]),
        ([1, 1, 1], [1, 1, 1]),
        ([2, 2, 0, 0, 1, 1], [0, 0, 1, 1, 2, 2]),
    ]

    approaches = [
        ("Dutch National Flag", sortColors),
        ("Two Pass", sortColorsTwoPass),
    ]

    for name, func in approaches:
        print(f"\n{'='*60}")
        print(f"Testing: {name}")
        print(f"{'='*60}")

        all_passed = True
        for nums, expected in test_cases:
            nums_copy = nums.copy()
            func(nums_copy)

            status = "✅" if nums_copy == expected else "❌"
            if nums_copy != expected:
                all_passed = False

            print(f"{status} Input: {nums}")
            print(f"   Output: {nums_copy}, Expected: {expected}")

        if all_passed:
            print("✅ All tests passed!")


if __name__ == "__main__":
    print("LeetCode #75: Sort Colors (Dutch National Flag)\n")
    print("⭐ Three Pointers Pattern: Partitioning")
    print("="*60)

    # Dry run
    dry_run_sort_colors()

    # Run tests
    run_tests()

    # Explanations
    why_this_works()
    why_mid_doesnt_advance()
    pattern_extension()

    # Common mistakes
    common_mistakes()

    print("\n" + "="*60)
    print("KEY TAKEAWAYS")
    print("="*60)
    print("""
1. Three pointers for 3-way partitioning (0s, 1s, 2s)
2. Maintain invariant: [0s | 1s | unknown | 2s]
3. CRITICAL: Don't advance mid when swapping with high!
4. One pass O(n), constant space O(1)
5. Named after Dutch flag (3 horizontal stripes)

Pointer Movement Rules:
- nums[mid] == 0: swap with low, low++, mid++ ✓
- nums[mid] == 1: just mid++ ✓
- nums[mid] == 2: swap with high, high-- (mid stays!) ✓

Why mid doesn't advance with 2:
- nums[low] is known (always 1 from invariant)
- nums[high] is unknown (could be 0, 1, or 2)
- Must examine swapped element!

Interview Strategy:
1. Explain the 3-way partition invariant
2. Draw the regions diagram
3. Explain why mid doesn't advance with 2 (critical!)
4. Code carefully (easy to mess up)
5. Test with [2, 0, 1] to verify correctness
6. Mention it's O(n) one-pass with O(1) space

Common Pitfalls:
❌ Advancing mid when swapping with high
❌ Using mid < high instead of mid <= high
❌ Swapping 0 with high instead of low
✓ Remember: only high moves when swapping 2!
✓ mid must examine the swapped element

Related Problems:
- LC #283: Move Zeroes (2-way partition)
- LC #partition-list: Partition List
- LC #86: Partition LinkedList
- Quicksort partitioning (similar idea)

This is a CLASSIC algorithm - master it!
Dutch National Flag is named after inventor Edsger Dijkstra.
    """)
