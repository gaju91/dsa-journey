"""
LeetCode #26: Remove Duplicates from Sorted Array
LeetCode #83: Remove Duplicates from Sorted List
LeetCode #80: Remove Duplicates from Sorted Array II

Difficulty: Easy
Pattern: Two Pointers (Same Direction - Fast & Slow)

Problem:
Given a sorted array/list, remove duplicates in-place such that each element
appears only once (or at most twice for variant). Return the new length.

Example 1 (Remove all duplicates):
Input: nums = [1,1,2,2,3,3,4]
Output: 4, nums = [1,2,3,4,_,_,_]

Example 2 (Keep at most 2):
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -100 <= nums[i] <= 100
- nums is sorted in non-decreasing order
"""

from typing import List, Optional


# ============================================================================
# Approach 1: Remove All Duplicates (LC #26) - OPTIMAL
# Time: O(n), Space: O(1)
# ============================================================================
def removeDuplicates(nums: List[int]) -> int:
    """
    Strategy: Fast & Slow pointers

    Analogy: "Slow pointer writes unique values, fast pointer reads all values."

    [1, 1, 2, 2, 3, 3, 4]
     ↑ ↑
     S F

    - Slow = position to write next unique value
    - Fast = reading all values
    - When nums[fast] != nums[slow], we found a new unique value
    """
    if not nums:
        return 0

    slow = 0  # Position of last unique element

    for fast in range(1, len(nums)):
        # Found a new unique value
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1  # Length of unique elements


# ============================================================================
# Approach 2: Keep At Most K Duplicates (Generalized Solution)
# Time: O(n), Space: O(1)
# ============================================================================
def removeDuplicatesKeepK(nums: List[int], k: int) -> int:
    """
    Strategy: Allow each element to appear at most k times

    Key Insight:
    - Compare current element with element k positions back
    - If different, we can safely add current element

    Why it works:
    - If nums[i] != nums[slow - k + 1], then nums[i] is either:
      1. A new value, OR
      2. Same value but we haven't reached k occurrences yet
    """
    if not nums or k <= 0:
        return 0

    slow = 0

    for fast in range(len(nums)):
        # First k elements are always valid
        # Or current element is different from k-th previous element
        if slow < k or nums[fast] != nums[slow - k]:
            nums[slow] = nums[fast]
            slow += 1

    return slow


# ============================================================================
# Approach 3: LC #80 - Keep At Most 2 Duplicates
# Time: O(n), Space: O(1)
# ============================================================================
def removeDuplicatesKeepTwo(nums: List[int]) -> int:
    """
    Strategy: Specialized version for k=2

    This is just calling the general solution with k=2
    """
    return removeDuplicatesKeepK(nums, 2)


# ============================================================================
# Approach 4: Manual Two Pointer for K=2 (More Explicit)
# Time: O(n), Space: O(1)
# ============================================================================
def removeDuplicatesKeepTwoManual(nums: List[int]) -> int:
    """
    Strategy: Track count of current element

    More intuitive but less elegant than the generalized solution.
    """
    if len(nums) <= 2:
        return len(nums)

    slow = 2  # First 2 elements are always valid

    for fast in range(2, len(nums)):
        # Can add if different from 2 positions back
        # This ensures at most 2 duplicates
        if nums[fast] != nums[slow - 2]:
            nums[slow] = nums[fast]
            slow += 1

    return slow


# ============================================================================
# Linked List Version (LC #83)
# Time: O(n), Space: O(1)
# ============================================================================
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Strategy: One pointer for linked list

    Unlike array, we can simply skip duplicate nodes by adjusting pointers.
    """
    if not head:
        return None

    current = head

    while current and current.next:
        if current.val == current.next.val:
            # Skip duplicate
            current.next = current.next.next
        else:
            # Move to next unique value
            current = current.next

    return head


# ============================================================================
# DRY RUN EXAMPLE
# ============================================================================
def dry_run_remove_duplicates() -> int:
    """
    Detailed walkthrough of fast & slow pointers
    """
    nums = [1, 1, 2, 2, 3, 3, 4]

    print("\n" + "="*60)
    print("DRY RUN: Remove All Duplicates")
    print("="*60)
    print(f"Input: {nums}\n")

    slow = 0
    print(f"Initial: slow = {slow}")
    print(f"Array:   {nums}")
    print(f"         {'↑' + ' '*(slow*4)}")
    print(f"         {'S' + ' '*(slow*4)}\n")

    for fast in range(1, len(nums)):
        print(f"Step {fast}:")
        print(f"  Fast = {fast}, nums[fast] = {nums[fast]}")
        print(f"  Slow = {slow}, nums[slow] = {nums[slow]}")

        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
            print(f"  ✓ New unique value found!")
            print(f"  Action: slow++ → {slow}, nums[{slow}] = {nums[fast]}")
        else:
            print(f"  ✗ Duplicate, skip")

        # Visualize
        arr_str = str(nums)
        print(f"  Array: {arr_str}")
        print()

    new_length = slow + 1
    print(f"Final length: {new_length}")
    print(f"Result: {nums[:new_length]}")

    return new_length


# ============================================================================
# WHY THIS PATTERN WORKS
# ============================================================================
def why_pattern_works() -> None:
    """
    Explanation of the fast & slow pointer technique
    """
    print("\n" + "="*60)
    print("WHY FAST & SLOW POINTERS WORK")
    print("="*60)

    print("""
Key Insight: SORTED array means duplicates are ADJACENT

Invariant: At any time, nums[0..slow] contains unique elements

Proof:
1. Initially: slow = 0, nums[0] is unique ✓

2. Maintenance: For each fast pointer position:
   - If nums[fast] == nums[slow]: duplicate, don't advance slow
   - If nums[fast] != nums[slow]: new unique value
     → slow++, copy nums[fast] to nums[slow]
     → nums[0..slow] still contains all unique elements ✓

3. Termination: fast reaches end
   → nums[0..slow] contains all unique elements ✓

Time Complexity: O(n) - single pass
Space Complexity: O(1) - only pointers

Pattern Name: Same Direction Two Pointers (Fast & Slow)

When to use:
✅ Array is SORTED
✅ Need to modify array IN-PLACE
✅ Removing/filtering elements based on condition
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
❌ Mistake 1: Starting fast from 0
   for fast in range(len(nums)):  # WRONG!

   ✓ Fix: Start from 1, since first element is always unique
   for fast in range(1, len(nums)):

❌ Mistake 2: Not handling empty array
   slow = 0
   for fast in range(1, len(nums)):  # Crashes if empty!

   ✓ Fix: Check first
   if not nums: return 0

❌ Mistake 3: Comparing with fast instead of slow
   if nums[fast] != nums[fast-1]:  # WRONG! Doesn't work for in-place

   ✓ Fix: Compare with slow
   if nums[fast] != nums[slow]:

❌ Mistake 4: Forgetting to return length
   return slow  # WRONG! Off by one

   ✓ Fix: Add 1
   return slow + 1

❌ Mistake 5: For k=2 variant, wrong comparison
   if nums[fast] != nums[slow - 1]:  # WRONG! Only checks 1 back

   ✓ Fix: Check k positions back
   if nums[fast] != nums[slow - k]:
    """)


# ============================================================================
# TEST CASES
# ============================================================================
def run_tests() -> None:
    test_cases = [
        # (input, expected_length, expected_array)
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        ([1, 1, 1], 1, [1]),
        ([1], 1, [1]),
        ([1, 2, 3], 3, [1, 2, 3]),
    ]

    print("\n" + "="*60)
    print("Testing: Remove All Duplicates")
    print("="*60)

    all_passed = True
    for nums, expected_len, expected_arr in test_cases:
        original = nums.copy()
        result_len = removeDuplicates(nums)
        result_arr = nums[:result_len]

        status = "✅" if result_len == expected_len and result_arr == expected_arr else "❌"
        if result_arr != expected_arr:
            all_passed = False

        print(f"{status} Input: {original}")
        print(f"   Output: length={result_len}, array={result_arr}")
        print(f"   Expected: length={expected_len}, array={expected_arr}")
        print()

    if all_passed:
        print("✅ All tests passed!")

    # Test K=2 variant
    print("\n" + "="*60)
    print("Testing: Keep At Most 2 Duplicates")
    print("="*60)

    test_cases_k2 = [
        ([1, 1, 1, 2, 2, 3], 5, [1, 1, 2, 2, 3]),
        ([0, 0, 1, 1, 1, 1, 2, 3, 3], 7, [0, 0, 1, 1, 2, 3, 3]),
    ]

    for nums, expected_len, expected_arr in test_cases_k2:
        original = nums.copy()
        result_len = removeDuplicatesKeepTwo(nums)
        result_arr = nums[:result_len]

        status = "✅" if result_len == expected_len and result_arr == expected_arr else "❌"

        print(f"{status} Input: {original}")
        print(f"   Output: length={result_len}, array={result_arr}")
        print(f"   Expected: length={expected_len}, array={expected_arr}")
        print()


if __name__ == "__main__":
    print("Remove Duplicates - Fast & Slow Pointers Pattern\n")
    print("="*60)

    # Dry run
    dry_run_remove_duplicates()

    # Run tests
    run_tests()

    # Explanation
    why_pattern_works()

    # Common mistakes
    common_mistakes()

    print("\n" + "="*60)
    print("KEY TAKEAWAYS")
    print("="*60)
    print("""
1. Fast & Slow pointers for in-place array modifications
2. Slow = write position, Fast = read position
3. SORTED array is crucial (duplicates are adjacent)
4. Pattern works for "remove if condition" problems
5. Can generalize to "keep at most k duplicates"

Decision Rule:
- nums[fast] == nums[slow] → Skip (duplicate)
- nums[fast] != nums[slow] → Write (unique)

Interview Strategy:
1. Recognize SORTED + IN-PLACE → Fast & Slow pointers
2. Explain the invariant (nums[0..slow] is answer so far)
3. Code the solution (very short!)
4. Mention time O(n) and space O(1)
5. Discuss the generalized k-duplicates solution

Related Problems:
- LC #26: Remove Duplicates from Sorted Array
- LC #80: Remove Duplicates from Sorted Array II
- LC #83: Remove Duplicates from Sorted List
- LC #27: Remove Element
- LC #283: Move Zeroes
    """)
