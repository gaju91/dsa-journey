"""
LeetCode #448: Find All Numbers Disappeared in an Array
Difficulty: Easy
Pattern: Index Marking (Basic)

Problem:
Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
Input: nums = [1,1]
Output: [2]

Constraints:
- n == nums.length
- 1 <= n <= 10^5
- 1 <= nums[i] <= n

Follow up: Could you do it without extra space and in O(n) runtime?
"""

from typing import List


# ============================================================================
# Approach 1: Index Marking (OPTIMAL - O(1) space)
# Time: O(n), Space: O(1)
# ============================================================================
def findDisappearedNumbers(nums: List[int]) -> List[int]:
    """
    Strategy: Mark indices as negative to indicate presence

    Analogy: "Roll call - cross out names as students answer.
              Uncrossed names are absent students."

    Key Insight:
    - If number x exists, mark index (x-1) as negative
    - After processing, positive indices indicate missing numbers
    """
    n = len(nums)

    # Phase 1: Mark presence
    for i in range(n):
        value = abs(nums[i])        # CRITICAL: Use abs() in case already negative
        index = value - 1           # Map value to index (1-indexed → 0-indexed)
        nums[index] = -abs(nums[index])  # Mark as visited

    # Phase 2: Collect missing numbers
    missing = []
    for i in range(n):
        if nums[i] > 0:            # Positive = never marked = number (i+1) is missing
            missing.append(i + 1)

    # Optional: Restore original array
    # for i in range(n):
    #     nums[i] = abs(nums[i])

    return missing


# ============================================================================
# Approach 2: Hash Set (Naive - O(n) space)
# Time: O(n), Space: O(n)
# ============================================================================
def findDisappearedNumbers_set(nums: List[int]) -> List[int]:
    """
    Strategy: Use set to track present numbers

    This is the intuitive approach but uses extra space
    """
    n = len(nums)
    present = set(nums)
    missing = []

    for i in range(1, n + 1):
        if i not in present:
            missing.append(i)

    return missing


# ============================================================================
# Approach 3: Cyclic Sort (Alternative O(1) space)
# Time: O(n), Space: O(1)
# ============================================================================
def findDisappearedNumbers_cyclic_sort(nums: List[int]) -> List[int]:
    """
    Strategy: Place each number at its correct position

    This is another O(1) space approach using the cyclic sort pattern
    """
    i = 0
    while i < len(nums):
        correct_pos = nums[i] - 1
        # Swap to correct position if not already there
        if nums[i] != nums[correct_pos]:
            nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
        else:
            i += 1

    # Find numbers not at correct position
    missing = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            missing.append(i + 1)

    return missing


# ============================================================================
# DRY RUN EXAMPLE
# ============================================================================
def dry_run_example():
    """
    Detailed walkthrough of index marking approach

    Input: [4, 3, 2, 7, 8, 2, 3, 1]
    Goal: Find missing numbers in [1..8]
    """
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print("Input:", nums)
    print("\n=== PHASE 1: MARKING ===\n")

    for i in range(len(nums)):
        value = abs(nums[i])
        index = value - 1
        print(f"Step {i+1}: Process value={value}, mark index={index}")
        nums[index] = -abs(nums[index])
        print(f"  Array: {nums}")

    print("\n=== PHASE 2: FINDING MISSING ===\n")
    missing = []
    for i in range(len(nums)):
        if nums[i] > 0:
            print(f"Index {i} is positive → number {i+1} is missing")
            missing.append(i + 1)

    print(f"\nMissing numbers: {missing}")
    return missing


# ============================================================================
# TEST CASES
# ============================================================================
def run_tests():
    test_cases = [
        ([4, 3, 2, 7, 8, 2, 3, 1], [5, 6]),
        ([1, 1], [2]),
        ([1, 2, 3, 4, 5], []),
        ([2, 2, 2, 2], [1, 3, 4]),
        ([1], []),
    ]

    approaches = [
        ("Index Marking", findDisappearedNumbers),
        ("Hash Set", findDisappearedNumbers_set),
        ("Cyclic Sort", findDisappearedNumbers_cyclic_sort),
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


# ============================================================================
# COMMON MISTAKES
# ============================================================================
def common_mistakes():
    """
    Demonstrate common bugs in index marking
    """
    print("\n" + "="*60)
    print("COMMON MISTAKES DEMONSTRATION")
    print("="*60)

    nums = [4, 3, 2, 7]

    # Mistake 1: Forgetting abs() when reading
    print("\n❌ Mistake 1: Forgetting abs() when reading")
    try:
        for i in range(len(nums)):
            idx = nums[i] - 1  # BUG: Should be abs(nums[i]) - 1
            nums[idx] = -nums[idx]
        print(f"  Result: {nums}")
        print("  This might work sometimes but will fail on certain inputs!")
    except:
        print("  Crashed due to invalid index!")

    # Mistake 2: Using -nums[idx] instead of -abs(nums[idx])
    print("\n❌ Mistake 2: Using -nums[idx] instead of -abs(nums[idx])")
    nums = [4, 3, 2, 7]
    for i in range(len(nums)):
        idx = abs(nums[i]) - 1
        nums[idx] = -nums[idx]  # BUG: Can toggle back to positive
    print(f"  After first pass: {nums}")
    # If we process duplicates, they might toggle back
    print("  If duplicate is processed, it can toggle from -X to X!")

    # Correct approach
    print("\n✅ CORRECT: Using abs() properly")
    nums = [4, 3, 2, 7]
    for i in range(len(nums)):
        idx = abs(nums[i]) - 1
        nums[idx] = -abs(nums[idx])
    print(f"  Result: {nums}")
    print("  All marked indices stay negative!")


if __name__ == "__main__":
    print("LeetCode #448: Find All Numbers Disappeared in an Array\n")

    # Run dry example
    print("\n" + "="*60)
    print("DRY RUN EXAMPLE")
    print("="*60)
    dry_run_example()

    # Run tests
    run_tests()

    # Show common mistakes
    common_mistakes()

    print("\n" + "="*60)
    print("KEY TAKEAWAYS")
    print("="*60)
    print("""
1. Always use abs() when reading values
2. Always use -abs() when marking indices
3. Map value x to index (x-1)
4. Positive index after marking = missing number

Pattern Recognition:
- See numbers in [1..n] with array length n?
- Asked to find missing/duplicate?
→ Think INDEX MARKING!
    """)
