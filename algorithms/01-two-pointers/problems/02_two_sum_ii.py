"""
LeetCode #167: Two Sum II - Input Array Is Sorted
Difficulty: Medium
Pattern: Two Pointers (Opposite Direction)

Problem:
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing
order, find two numbers such that they add up to a specific target number.

Let these two numbers be numbers[index1] and numbers[index2] where
1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an
integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use
the same element twice.

Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2.
We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]

Constraints:
- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order
- -1000 <= target <= 2 * 1000
- The tests are generated such that there is exactly one solution
"""

from typing import List


# ============================================================================
# Approach 1: Two Pointers - Opposite Direction (OPTIMAL)
# Time: O(n), Space: O(1)
# ============================================================================
def twoSum(numbers: List[int], target: int) -> List[int]:
    """
    Strategy: Start from both ends, move based on sum comparison

    Analogy: "Two people walking toward each other in a hallway.
              If their sum is too small, the person at the start walks forward.
              If their sum is too large, the person at the end walks backward."

    Why it works:
    - Array is SORTED
    - If sum < target: left value too small, need larger → left++
    - If sum > target: right value too large, need smaller → right--
    - We never miss the answer because we eliminate one side each step

    Returns 1-indexed positions!
    """
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            # Return 1-indexed (problem requirement)
            return [left + 1, right + 1]

        elif current_sum < target:
            # Sum too small, need larger value
            left += 1  # Move to larger value

        else:  # current_sum > target
            # Sum too large, need smaller value
            right -= 1  # Move to smaller value

    return []  # No solution (won't happen per constraints)


# ============================================================================
# Approach 2: Binary Search (Alternative O(n log n))
# Time: O(n log n), Space: O(1)
# ============================================================================
def twoSum_binary_search(numbers: List[int], target: int) -> List[int]:
    """
    Strategy: Fix first number, binary search for complement

    This works but is slower than two pointers!
    Shown for educational purposes.
    """
    for i in range(len(numbers)):
        complement = target - numbers[i]

        # Binary search for complement in numbers[i+1:]
        left, right = i + 1, len(numbers) - 1

        while left <= right:
            mid = (left + right) // 2

            if numbers[mid] == complement:
                return [i + 1, mid + 1]  # 1-indexed
            elif numbers[mid] < complement:
                left = mid + 1
            else:
                right = mid - 1

    return []


# ============================================================================
# Approach 3: Hash Map (Not optimal for this problem)
# Time: O(n), Space: O(n)
# ============================================================================
def twoSum_hash_map(numbers: List[int], target: int) -> List[int]:
    """
    Strategy: Same as regular Two Sum

    This works but violates the constant space requirement!
    """
    seen = {}

    for i, num in enumerate(numbers):
        complement = target - num

        if complement in seen:
            return [seen[complement] + 1, i + 1]  # 1-indexed

        seen[num] = i

    return []


# ============================================================================
# DRY RUN EXAMPLE
# ============================================================================
def dry_run_two_pointers() -> List[int]:
    """
    Detailed walkthrough of two pointers approach
    """
    numbers = [2, 7, 11, 15]
    target = 9

    print("\n" + "="*60)
    print("DRY RUN: Two Pointers Approach")
    print("="*60)
    print(f"Input: numbers = {numbers}, target = {target}\n")

    left, right = 0, len(numbers) - 1
    step = 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        print(f"Step {step}:")
        print(f"  Pointers: left={left}, right={right}")
        print(f"  Values: numbers[{left}]={numbers[left]}, "
              f"numbers[{right}]={numbers[right]}")
        print(f"  Sum: {numbers[left]} + {numbers[right]} = {current_sum}")

        if current_sum == target:
            result = [left + 1, right + 1]
            print(f"  ✓ Found! Sum equals target")
            print(f"  Answer (1-indexed): {result}")
            return result

        elif current_sum < target:
            print(f"  {current_sum} < {target} → Need larger sum")
            print(f"  Action: Move left pointer right (left++)")
            left += 1

        else:
            print(f"  {current_sum} > {target} → Need smaller sum")
            print(f"  Action: Move right pointer left (right--)")
            right -= 1

        print()
        step += 1

    print("No solution found")
    return []


# ============================================================================
# WHY TWO POINTERS IS OPTIMAL HERE
# ============================================================================
def why_two_pointers_optimal() -> None:
    """
    Explanation of why two pointers is the best choice
    """
    print("\n" + "="*60)
    print("WHY TWO POINTERS IS OPTIMAL FOR TWO SUM II")
    print("="*60)

    print("""
Key Differences from Two Sum I:

1. Array is SORTED
   ✅ Enables intelligent pointer movement
   ✅ Can decide which pointer to move

2. Constant space required
   ✅ Two pointers uses O(1) space
   ❌ Hash map uses O(n) space

3. Guaranteed solution
   ✅ Can use while loop without extra checks

Comparison of Approaches:

┌──────────────────┬──────────┬─────────┬────────────────┐
│   Approach       │   Time   │  Space  │   Best for     │
├──────────────────┼──────────┼─────────┼────────────────┤
│ Two Pointers     │   O(n)   │  O(1)   │ ✓ This problem │
│ Binary Search    │ O(n log n)│ O(1)   │   Slower       │
│ Hash Map         │   O(n)   │  O(n)   │   Violates req │
│ Brute Force      │   O(n²)  │  O(1)   │   Too slow     │
└──────────────────┴──────────┴─────────┴────────────────┘

Why Two Pointers Wins:
✓ Fastest possible (O(n))
✓ Meets space requirement (O(1))
✓ Simple to implement
✓ Easy to explain in interview

This is THE CANONICAL two pointers problem!
    """)


# ============================================================================
# CORRECTNESS PROOF
# ============================================================================
def correctness_proof() -> None:
    """
    Proof that two pointers finds the solution if it exists
    """
    print("\n" + "="*60)
    print("CORRECTNESS PROOF")
    print("="*60)

    print("""
Claim: Two pointers algorithm finds the solution if it exists.

Proof:

Assume solution is (i, j) where i < j and numbers[i] + numbers[j] = target.

We'll prove we never skip both i and j.

Case 1: Left pointer skips position i
- This happens when left moves from k to k+1 where k < i
- Move occurs when numbers[k] + numbers[right] < target
- Let's call the right pointer position r at this time

Sub-case 1a: r > j
  numbers[k] + numbers[r] ≥ numbers[k] + numbers[j]  (sorted array)
                           > numbers[i] + numbers[j]  (k < i, sorted)
                           = target
  But we said numbers[k] + numbers[r] < target
  CONTRADICTION ✗

Sub-case 1b: r = j
  numbers[k] + numbers[j] < target
  But numbers[i] + numbers[j] = target and k < i
  So numbers[k] < numbers[i]  (sorted array)
  Thus numbers[k] + numbers[j] < numbers[i] + numbers[j] = target ✓
  So we correctly skip k

Sub-case 1c: r < j
  Will be caught when right pointer reaches j

Case 2: Right pointer skips position j
- Similar symmetric analysis

Conclusion: We never skip both i and j simultaneously.
Therefore, we MUST encounter the solution. QED ✓

Key Insight: The sorted property guarantees correctness!
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
        # (array, target, expected, description)
        ([2, 7, 11, 15], 9, [1, 2], "Basic case"),
        ([2, 3, 4], 6, [1, 3], "Skip middle element"),
        ([-1, 0], -1, [1, 2], "Negative numbers"),
        ([1, 2], 3, [1, 2], "Minimum size array"),
        ([1, 1, 1, 1, 1, 1], 2, [1, 2], "All duplicates"),
        ([-5, -3, -2, 0, 1, 3], -5, [1, 4], "Negative + zero"),
        ([0, 0, 3, 4], 0, [1, 2], "Target is zero"),
        ([5, 25, 75], 100, [2, 3], "Large gap"),
    ]

    for numbers, target, expected, desc in edge_cases:
        result = twoSum(numbers, target)
        status = "✅" if result == expected else "❌"
        print(f"{status} {desc}")
        print(f"   Input: {numbers}, target={target}")
        print(f"   Output: {result}, Expected: {expected}")


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
❌ Mistake 1: Using <= instead of <
   while left <= right:  # WRONG!
   Allows same element twice

   ✓ Fix: while left < right

❌ Mistake 2: Forgetting 1-indexed return
   return [left, right]  # WRONG!
   Should return [left + 1, right + 1]

❌ Mistake 3: Moving both pointers
   if current_sum == target:
       left += 1    # WRONG!
       right -= 1   # WRONG!
       # Should return immediately!

   ✓ Fix: return [left + 1, right + 1]

❌ Mistake 4: Not handling duplicates properly
   # This problem guarantees unique solution
   # But if there were duplicates, we'd need to skip them

❌ Mistake 5: Wrong initial positions
   left = 1   # WRONG! Should be 0
   right = len(numbers)  # WRONG! Should be len(numbers) - 1
    """)


# ============================================================================
# TEST CASES
# ============================================================================
def run_tests() -> None:
    test_cases = [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([1, 2, 3, 4, 5], 9, [4, 5]),
        ([5, 25, 75], 100, [2, 3]),
    ]

    approaches = [
        ("Two Pointers", twoSum),
        ("Binary Search", twoSum_binary_search),
        ("Hash Map", twoSum_hash_map),
    ]

    for name, func in approaches:
        print(f"\n{'='*60}")
        print(f"Testing: {name}")
        print(f"{'='*60}")

        all_passed = True
        for numbers, target, expected in test_cases:
            result = func(numbers.copy(), target)
            status = "✅" if result == expected else "❌"
            if result != expected:
                all_passed = False

            print(f"{status} Input: numbers={numbers}, target={target}")
            print(f"   Output: {result}, Expected: {expected}")

        if all_passed:
            print("✅ All tests passed!")


# ============================================================================
# PERFORMANCE COMPARISON
# ============================================================================
def compare_performance() -> None:
    """
    Compare performance of different approaches
    """
    import timeit

    numbers = list(range(1, 10001))  # Sorted array [1..10000]
    target = 19999  # Sum of last two elements

    approaches = [
        ("Two Pointers", "twoSum(numbers, target)"),
        ("Binary Search", "twoSum_binary_search(numbers, target)"),
        ("Hash Map", "twoSum_hash_map(numbers, target)"),
    ]

    print("\n" + "="*60)
    print("PERFORMANCE COMPARISON")
    print("="*60)
    print(f"Array size: {len(numbers)}")
    print(f"Target: {target}\n")

    for name, code in approaches:
        time = timeit.timeit(code, globals=globals(), number=1000)
        print(f"{name:20} {time:.4f} seconds")


if __name__ == "__main__":
    print("LeetCode #167: Two Sum II - Input Array Is Sorted\n")
    print("⭐ THE CANONICAL Two Pointers Problem!")
    print("="*60)

    # Dry run
    dry_run_two_pointers()

    # Run tests
    run_tests()

    # Test edge cases
    test_edge_cases()

    # Why optimal
    why_two_pointers_optimal()

    # Correctness proof
    correctness_proof()

    # Common mistakes
    common_mistakes()

    # Performance comparison
    compare_performance()

    print("\n" + "="*60)
    print("KEY TAKEAWAYS")
    print("="*60)
    print("""
1. Two Sum II is THE classic two pointers problem
2. Sorted array enables intelligent pointer movement
3. O(n) time, O(1) space - optimal solution
4. Always check: left < right (not <=)
5. Remember to return 1-indexed positions!

Decision Rule:
- sum < target → need larger → left++
- sum > target → need smaller → right--
- sum == target → found!

Interview Strategy:
1. Recognize it's sorted → think two pointers
2. Explain why two pointers works (sorted property)
3. Code the solution (it's short!)
4. Mention the correctness guarantee
5. Discuss why it's better than hash map (space)

This is a MUST-KNOW problem for interviews!
    """)
