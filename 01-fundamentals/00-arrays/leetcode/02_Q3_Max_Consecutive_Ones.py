"""
LeetCode #485: Max Consecutive Ones
Difficulty: Easy

Problem:
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1
"""

from typing import List, Any
import re
from itertools import groupby

# ============================================================================
# Approach 1: Basic Loop with Counter (Your Solution - CLEANED)
# Time: O(n), Space: O(1)
# ============================================================================
def max_consecutive_basic(nums: List[int]) -> int:
    """
    Strategy: Track current streak and max streak
    Most straightforward and interview-friendly
    """
    max_count = 0
    current_count = 0

    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count


# ============================================================================
# Approach 2: String Conversion + Split (PYTHONIC!)
# Time: O(n), Space: O(n)
# ============================================================================
def max_consecutive_string(nums: List[int]) -> int:
    """
    Strategy: Convert to string, split on '0', find longest '1' sequence
    Very Pythonic and clever!

    Analogy: "Finding longest word in a sentence separated by spaces"
    """
    # Convert [1,1,0,1,1,1] -> "110111" -> split by '0' -> ["11", "111"]
    return max((segment.count('1') for segment in ''.join(map(str, nums)).split('0')), default=0)


# ============================================================================
# Approach 3: itertools.groupby (FUNCTIONAL STYLE)
# Time: O(n), Space: O(1) for iterator
# ============================================================================
def max_consecutive_groupby(nums: List[int]) -> int:
    """
    Strategy: Group consecutive equal elements, count length of '1' groups
    Functional programming approach

    Analogy: "Group similar items together, count largest group of ones"
    """
    return max((sum(1 for _ in group) for key, group in groupby(nums) if key == 1), default=0)


# ============================================================================
# Approach 4: List Comprehension with Sliding Window
# Time: O(n), Space: O(n)
# ============================================================================
def max_consecutive_comprehension(nums: List[int]) -> int:
    """
    Strategy: Split array on zeros, count ones in each segment
    Clean and readable
    """
    # Split on zeros by converting to string
    segments = ''.join(map(str, nums)).split('0')
    return max(len(seg) for seg in segments)


# ============================================================================
# Approach 5: Regex Approach (CREATIVE!)
# Time: O(n), Space: O(n)
# ============================================================================
def max_consecutive_regex(nums: List[int]) -> int:
    """
    Strategy: Use regex to find all consecutive 1s
    Shows regex knowledge (useful for string problems)

    Analogy: "Find all sequences of 1s using pattern matching"
    """
    binary_string = ''.join(map(str, nums))
    matches = re.findall(r'1+', binary_string)
    return max((len(match) for match in matches), default=0)


# ============================================================================
# Approach 6: Reset Counter Pattern (INTERVIEW CLASSIC)
# Time: O(n), Space: O(1)
# ============================================================================
def max_consecutive_reset(nums: List[int]) -> int:
    """
    Strategy: Multiply counter by num (resets to 0 when num=0)
    Math trick that's elegant but less readable
    """
    max_count = current = 0
    for num in nums:
        current = (current + 1) * num  # Resets to 0 when num=0
        max_count = max(max_count, current)
    return max_count


# ============================================================================
# Approach 7: Generator Expression (MEMORY EFFICIENT)
# Time: O(n), Space: O(1)
# ============================================================================
def max_consecutive_generator(nums: List[int]) -> int:
    """
    Strategy: Generate consecutive counts on-the-fly
    Memory efficient for large arrays
    """
    def generate_streaks():
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                if count > 0:
                    yield count
                count = 0
        if count > 0:
            yield count

    return max(generate_streaks(), default=0)


# ============================================================================
# Approach 8: One-Liner (CODE GOLF!)
# Time: O(n), Space: O(n)
# ============================================================================
def max_consecutive_oneliner(nums: List[int]) -> int:
    """
    Strategy: Ultimate Python one-liner
    Impressive but less maintainable
    """
    return max(map(len, ''.join(map(str, nums)).split('0')))


# ============================================================================
# BONUS: Using reduce (FUNCTIONAL PROGRAMMING)
# Time: O(n), Space: O(1)
# ============================================================================
def max_consecutive_reduce(nums: List[int]) -> int:
    """
    Strategy: Use functools.reduce to track state
    Shows functional programming knowledge
    """
    from functools import reduce

    def update(state: tuple[int, int], num: int) -> tuple[int, int]:
        max_count, current_count = state
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
        return (max_count, current_count)

    return reduce(update, nums, (0, 0))[0]


# ============================================================================
# TEST CASES
# ============================================================================
def run_tests() -> None:
    test_cases = [
        ([1, 1, 0, 1, 1, 1], 3),
        ([1, 0, 1, 1, 0, 1], 2),
        ([0, 0, 0], 0),
        ([1, 1, 1, 1], 4),
        ([0, 1, 0], 1),
        ([1], 1),
        ([0], 0),
        ([1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1], 4),
    ]

    approaches = [
        ("Basic Loop", max_consecutive_basic),
        ("String Split", max_consecutive_string),
        ("itertools.groupby", max_consecutive_groupby),
        ("List Comprehension", max_consecutive_comprehension),
        ("Regex", max_consecutive_regex),
        ("Reset Counter", max_consecutive_reset),
        ("Generator", max_consecutive_generator),
        ("One-Liner", max_consecutive_oneliner),
        ("Reduce (Functional)", max_consecutive_reduce),
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
            print(f"{status} Input: {nums[:15]}{'...' if len(nums) > 15 else ''}")
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
    test_input = [1, 1, 0, 1, 1, 1] * 1000

    test_globals: dict[str, Any] = {
        **globals(),
        'test_input': test_input
    }

    approaches = [
        ("Basic Loop", "max_consecutive_basic(test_input)"),
        ("String Split", "max_consecutive_string(test_input)"),
        ("groupby", "max_consecutive_groupby(test_input)"),
        ("List Comprehension", "max_consecutive_comprehension(test_input)"),
        ("Regex", "max_consecutive_regex(test_input)"),
        ("Reset Counter", "max_consecutive_reset(test_input)"),
        ("Generator", "max_consecutive_generator(test_input)"),
        ("Reduce", "max_consecutive_reduce(test_input)"),
    ]

    print(f"\n{'='*60}")
    print(f"PERFORMANCE COMPARISON (1000 iterations)")
    print(f"Array size: {len(test_input)} elements")
    print(f"{'='*60}")

    for name, code in approaches:
        time = timeit.timeit(code, globals=test_globals, number=1000)
        print(f"{name:25} {time:.4f} seconds")


if __name__ == "__main__":
    print("LeetCode #485: Max Consecutive Ones\n")
    run_tests()

    print("\n" + "="*60)
    print("RECOMMENDATION")
    print("="*60)
    print("""
For interviews, use: max_consecutive_basic() or max_consecutive_groupby()
- Basic: Most clear and easy to explain
- groupby: Shows Python standard library knowledge
- Both are O(n) time, O(1) space (for iteration)

To impress interviewers:
- Start with basic approach
- Mention string split approach as clever alternative
- Discuss trade-offs: readability vs cleverness

Avoid in interviews: max_consecutive_oneliner()
- Too clever, hard to debug
- Interviewer might think you're showing off
- Use only if explicitly asked to optimize for code length

Performance winner: max_consecutive_basic() or max_consecutive_reset()
- Minimal overhead, no string conversions
- O(1) space complexity
- Reset counter is elegant but less readable
    """)

    # Uncomment to see performance comparison
    # compare_performance()