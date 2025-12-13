"""
LeetCode #645: Set Mismatch
Difficulty: Easy

Problem:
You have a set of integers s, which originally contains all the numbers from 1 to n.
Unfortunately, due to some error, one of the numbers in s got duplicated to another
number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.
Find the number that occurs twice and the number that is missing and return them in the
form of an array [duplicate, missing].

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Explanation: 2 occurs twice and 3 is missing.

Example 2:
Input: nums = [1,1]
Output: [1,2]

Example 3:
Input: nums = [3,2,3,4,6,5]
Output: [3,1]

Constraints:
- 2 <= nums.length <= 10^4
- 1 <= nums[i] <= 10^4
"""

from typing import List, Any, Set
from collections import Counter

# ============================================================================
# Approach 1: Sorting (Your Solution - CLEANED)
# Time: O(n log n), Space: O(1) or O(n) depending on sort implementation
# ============================================================================
def find_error_sorting(nums: List[int]) -> List[int]:
    """
    Strategy: Sort array, find duplicate and gap

    Analogy: "Line up students by number - duplicate stands next to clone,
              missing number creates a gap"
    """
    nums.sort()
    n = len(nums)
    duplicate = missing = -1

    # Find duplicate and gap
    for i in range(1, n):
        if nums[i] == nums[i - 1]:
            duplicate = nums[i]
        elif nums[i] > nums[i - 1] + 1:
            missing = nums[i - 1] + 1

    # Handle edge cases: missing is at start or end
    if missing == -1:
        missing = 1 if nums[0] != 1 else n

    return [duplicate, missing]


# ============================================================================
# Approach 2: Hash Set (INTUITIVE & FAST)
# Time: O(n), Space: O(n)
# ============================================================================
def find_error_set(nums: List[int]) -> List[int]:
    """
    Strategy: Use set to detect duplicate, sum to find missing

    Analogy: "Roll call - someone answers twice (duplicate),
              one person doesn't answer (missing)"
    """
    n = len(nums)
    num_set: Set[int] = set()
    duplicate = -1

    # Find duplicate
    for num in nums:
        if num in num_set:
            duplicate = num
        num_set.add(num)

    # Find missing: sum of 1..n minus sum of unique numbers
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(num_set)
    missing = expected_sum - actual_sum

    return [duplicate, missing]


# ============================================================================
# Approach 3: Counter (PYTHONIC!)
# Time: O(n), Space: O(n)
# ============================================================================
def find_error_counter(nums: List[int]) -> List[int]:
    """
    Strategy: Use Counter to count frequencies
    Most Pythonic and readable
    """
    n = len(nums)
    count = Counter(nums)

    duplicate = missing = -1
    for i in range(1, n + 1):
        if count[i] == 2:
            duplicate = i
        elif count[i] == 0:
            missing = i

    return [duplicate, missing]


# ============================================================================
# Approach 4: Math - Sum & Square Sum (CLEVER!)
# Time: O(n), Space: O(1)
# ============================================================================
def find_error_math(nums: List[int]) -> List[int]:
    """
    Strategy: Use sum and sum of squares to solve equations

    Let duplicate = d, missing = m
    Equation 1: sum(nums) - sum(1..n) = d - m
    Equation 2: sum(nums²) - sum(1²..n²) = d² - m²

    From these: d² - m² = (d + m)(d - m)
    Solve for d and m

    Analogy: "Two equations, two unknowns - algebra to the rescue!"
    """
    n = len(nums)

    # Expected values
    expected_sum = n * (n + 1) // 2
    expected_square_sum = n * (n + 1) * (2 * n + 1) // 6

    # Actual values
    actual_sum = sum(nums)
    actual_square_sum = sum(x * x for x in nums)

    # d - m = actual_sum - expected_sum
    diff = actual_sum - expected_sum

    # d² - m² = actual_square_sum - expected_square_sum
    # (d + m)(d - m) = square_diff
    square_diff = actual_square_sum - expected_square_sum

    # d + m = square_diff / diff
    sum_dm = square_diff // diff

    # Solve: d = (sum + diff) / 2, m = (sum - diff) / 2
    duplicate = (sum_dm + diff) // 2
    missing = (sum_dm - diff) // 2

    return [duplicate, missing]


# ============================================================================
# Approach 5: In-Place Marking (SPACE OPTIMIZED!)
# Time: O(n), Space: O(1)
# ============================================================================
def find_error_inplace(nums: List[int]) -> List[int]:
    """
    Strategy: Mark visited indices by negating values

    Analogy: "Use the array itself as a checklist - cross out (negate)
              numbers as you see them"

    When we see duplicate, that index is already negative
    """
    duplicate = missing = -1

    # Find duplicate by marking
    for num in nums:
        index = abs(num) - 1
        if nums[index] < 0:
            duplicate = abs(num)
        else:
            nums[index] = -nums[index]

    # Find missing (positive value means never visited)
    for i in range(len(nums)):
        if nums[i] > 0:
            missing = i + 1
            break

    # Restore array (optional - good practice)
    for i in range(len(nums)):
        nums[i] = abs(nums[i])

    return [duplicate, missing]


# ============================================================================
# Approach 6: XOR Bit Manipulation (ADVANCED!)
# Time: O(n), Space: O(1)
# ============================================================================
def find_error_xor(nums: List[int]) -> List[int]:
    """
    Strategy: XOR properties - a ^ a = 0, a ^ 0 = a

    XOR all numbers and all indices to find xor of duplicate and missing
    Then separate them using rightmost set bit

    Analogy: "XOR is like a light switch - flip twice returns to original"
    """
    n = len(nums)
    xor_all = 0

    # XOR all array elements and all numbers from 1 to n
    for i in range(n):
        xor_all ^= nums[i]
        xor_all ^= (i + 1)

    # xor_all now contains: duplicate ^ missing
    # Find rightmost set bit
    rightmost_bit = xor_all & -xor_all

    # Separate numbers into two groups based on rightmost bit
    group1 = group2 = 0
    for num in nums:
        if num & rightmost_bit:
            group1 ^= num
        else:
            group2 ^= num

    for i in range(1, n + 1):
        if i & rightmost_bit:
            group1 ^= i
        else:
            group2 ^= i

    # One of group1/group2 is duplicate, other is missing
    # Check which one appears in array
    for num in nums:
        if num == group1:
            return [group1, group2]

    return [group2, group1]


# ============================================================================
# Approach 7: Frequency Array (SIMPLE & FAST)
# Time: O(n), Space: O(n)
# ============================================================================
def find_error_frequency(nums: List[int]) -> List[int]:
    """
    Strategy: Create frequency array, check counts
    Simple and efficient
    """
    n = len(nums)
    freq = [0] * (n + 1)

    for num in nums:
        freq[num] += 1

    duplicate = missing = -1
    for i in range(1, n + 1):
        if freq[i] == 2:
            duplicate = i
        elif freq[i] == 0:
            missing = i

    return [duplicate, missing]


# ============================================================================
# Approach 8: Cyclic Sort Pattern (INTERVIEW PATTERN!)
# Time: O(n), Space: O(1)
# ============================================================================
def find_error_cyclic_sort(nums: List[int]) -> List[int]:
    """
    Strategy: Place each number at its correct index (nums[i] = i+1)

    Analogy: "Assign each student to their numbered seat - duplicate
              takes someone's seat, one seat stays empty"

    This is a classic pattern for problems with numbers in range [1, n]
    """
    i = 0
    while i < len(nums):
        correct_pos = nums[i] - 1
        # If number is not at correct position and not a duplicate
        if nums[i] != nums[correct_pos]:
            nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
        else:
            i += 1

    # After cyclic sort, find the mismatch
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return [nums[i], i + 1]

    return [-1, -1]


# ============================================================================
# TEST CASES
# ============================================================================
def run_tests() -> None:
    test_cases = [
        ([1, 2, 2, 4], [2, 3]),
        ([1, 1], [1, 2]),
        ([3, 2, 3, 4, 6, 5], [3, 1]),
        ([2, 2], [2, 1]),
        ([1, 2, 3, 4, 4], [4, 5]),
        ([1, 5, 3, 2, 2, 7, 6, 4, 8, 9], [2, 10]),
        ([3, 3, 1], [3, 2]),
    ]

    approaches = [
        ("Sorting", find_error_sorting),
        ("Hash Set", find_error_set),
        ("Counter", find_error_counter),
        ("Math (Sum & Squares)", find_error_math),
        ("In-Place Marking", find_error_inplace),
        ("XOR Bit Manipulation", find_error_xor),
        ("Frequency Array", find_error_frequency),
        ("Cyclic Sort", find_error_cyclic_sort),
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
# PERFORMANCE COMPARISON
# ============================================================================
def compare_performance() -> None:
    """Compare execution time of different approaches"""
    import timeit

    # Large test case
    test_input = list(range(1, 1001))
    test_input[500] = 499  # Create duplicate

    test_globals: dict[str, Any] = {
        **globals(),
        'test_input': test_input
    }

    approaches = [
        ("Sorting", "find_error_sorting(test_input.copy())"),
        ("Hash Set", "find_error_set(test_input.copy())"),
        ("Counter", "find_error_counter(test_input.copy())"),
        ("Math", "find_error_math(test_input.copy())"),
        ("In-Place", "find_error_inplace(test_input.copy())"),
        ("XOR", "find_error_xor(test_input.copy())"),
        ("Frequency", "find_error_frequency(test_input.copy())"),
        ("Cyclic Sort", "find_error_cyclic_sort(test_input.copy())"),
    ]

    print(f"\n{'='*60}")
    print(f"PERFORMANCE COMPARISON (1000 iterations)")
    print(f"Array size: {len(test_input)} elements")
    print(f"{'='*60}")

    for name, code in approaches:
        time = timeit.timeit(code, globals=test_globals, number=1000)
        print(f"{name:25} {time:.4f} seconds")


if __name__ == "__main__":
    print("LeetCode #645: Set Mismatch\n")
    run_tests()

    print("\n" + "="*60)
    print("RECOMMENDATION")
    print("="*60)
    print("""
For interviews, use: find_error_counter() or find_error_set()
- Counter: Most Pythonic and readable
- Set: Clean logic, easy to explain
- Both are O(n) time, O(n) space

To impress interviewers:
- Start with Counter/Set approach
- If asked to optimize space: show in-place marking or cyclic sort
- For advanced discussion: explain XOR bit manipulation or math approach

Space-optimized approaches (O(1) space):
- find_error_inplace() - marks visited indices
- find_error_cyclic_sort() - classic pattern for [1,n] problems
- find_error_math() - pure mathematics

Avoid: find_error_sorting()
- O(n log n) time complexity
- Not optimal when O(n) solutions exist
- Use only if asked to solve without extra space and can't use in-place tricks

Interview Pattern Recognition:
This problem fits the "Cyclic Sort" pattern - whenever you see:
- Numbers in range [1, n]
- Array of length n
- Find missing/duplicate
→ Think: Cyclic Sort or In-Place Marking!
    """)

    # Uncomment to see performance comparison
    # compare_performance()