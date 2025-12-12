"""
LeetCode #1470: Shuffle the Array
Difficulty: Easy

Problem:
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Example 1:
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

Example 2:
Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]
"""

from typing import List

# ============================================================================
# Approach 1: Basic Loop with Extend (Your Solution - CORRECTED)
# Time: O(n), Space: O(n)
# ============================================================================
def shuffle_basic(nums: List[int], n: int) -> List[int]:
    """
    Strategy: Iterate through first half, pair with second half elements
    """
    result: List[int] = []
    for i in range(n):
        result.extend([nums[i], nums[n + i]])
    return result


# ============================================================================
# Approach 2: List Comprehension with Unpacking (MOST PYTHONIC!)
# Time: O(n), Space: O(n)
# ============================================================================
def shuffle_comprehension(nums: List[int], n: int) -> List[int]:
    """
    Strategy: Flatten pairs using list comprehension
    Most readable and Pythonic approach
    """
    return [num for i in range(n) for num in (nums[i], nums[n + i])]


# ============================================================================
# Approach 3: Zip + Chain (FUNCTIONAL STYLE)
# Time: O(n), Space: O(n)
# ============================================================================
def shuffle_zip_chain(nums: List[int], n: int) -> List[int]:
    """
    Strategy: Zip first and second halves, then flatten with chain
    Very Pythonic using itertools
    """
    from itertools import chain
    return list(chain.from_iterable(zip(nums[:n], nums[n:])))


# ============================================================================
# Approach 4: Zip + Double Unpacking (ONE-LINER!)
# Time: O(n), Space: O(n)
# ============================================================================
def shuffle_zip_unpack(nums: List[int], n: int) -> List[int]:
    """
    Strategy: Zip and unpack pairs directly into list
    Clever one-liner using * unpacking
    """
    return [num for pair in zip(nums[:n], nums[n:]) for num in pair]


# ============================================================================
# Approach 5: Enumerate with Conditional (INDEX-BASED)
# Time: O(n), Space: O(n)
# ============================================================================
def shuffle_enumerate(nums: List[int], n: int) -> List[int]:
    """
    Strategy: Pre-allocate result, fill based on index parity
    Good when you want to avoid extending lists
    """
    result = [0] * (2 * n)
    for i in range(n):
        result[2 * i] = nums[i]
        result[2 * i + 1] = nums[n + i]
    return result


# ============================================================================
# Approach 6: Deque for Efficient Append (COLLECTIONS)
# Time: O(n), Space: O(n)
# ============================================================================
def shuffle_deque(nums: List[int], n: int) -> List[int]:
    """
    Strategy: Use deque for O(1) append operations (though list extend is also O(1) amortized)
    Shows knowledge of collections module
    """
    from collections import deque
    result: deque[int] = deque()
    for i in range(n):
        result.extend([nums[i], nums[n + i]])
    return list(result)


# ============================================================================
# Approach 7: Generator Expression (MEMORY EFFICIENT)
# Time: O(n), Space: O(n) for final list, but generator is O(1)
# ============================================================================
def shuffle_generator(nums: List[int], n: int) -> List[int]:
    """
    Strategy: Use generator to lazily produce pairs
    Good for very large inputs if you don't need all at once
    """
    def gen_shuffle():
        for i in range(n):
            yield nums[i]
            yield nums[n + i]

    return list(gen_shuffle())

# ============================================================================
# BONUS: In-Place Using Index Encoding (ADVANCED - O(1) SPACE!)
# Time: O(n), Space: O(1) - SPACE OPTIMIZED!
# ============================================================================
def shuffle_in_place(nums: List[int], n: int) -> List[int]:
    """
    Strategy: Encode final position info in-place using mathematical trick
    Works when nums[i] <= 1000 (LeetCode constraint)

    We use the formula: nums[i] = nums[i] + (nums[target] % 1001) * 1001
    This stores both old value (% 1001) and new value (// 1001)

    Interview Gold: Shows advanced understanding!
    """
    # Step 1: Encode - store shuffled values in upper part
    for i in range(2 * n):
        # Determine where value at position i should come from
        if i % 2 == 0:
            # Even positions get from first half
            source = i // 2
        else:
            # Odd positions get from second half
            source = n + i // 2

        # Encode: current_value + (new_value * 1001)
        nums[i] = nums[i] + (nums[source] % 1001) * 1001

    # Step 2: Decode - extract the shuffled values
    for i in range(2 * n):
        nums[i] = nums[i] // 1001

    return nums


# ============================================================================
# TEST CASES
# ============================================================================
def run_tests() -> None:
    test_cases = [
        ([2, 5, 1, 3, 4, 7], 3, [2, 3, 5, 4, 1, 7]),
        ([1, 2, 3, 4, 4, 3, 2, 1], 4, [1, 4, 2, 3, 3, 2, 4, 1]),
        ([1, 1, 2, 2], 2, [1, 2, 1, 2]),
    ]

    approaches = [
        ("Basic Loop", shuffle_basic),
        ("List Comprehension", shuffle_comprehension),
        ("Zip + Chain", shuffle_zip_chain),
        ("Zip + Unpack", shuffle_zip_unpack),
        ("Enumerate", shuffle_enumerate),
        ("Deque", shuffle_deque),
        ("Generator", shuffle_generator),
        ("In-Place (Advanced)", shuffle_in_place),
    ]

    for name, func in approaches:
        print(f"\n{'='*60}")
        print(f"Testing: {name}")
        print(f"{'='*60}")

        for nums, n, expected in test_cases:
            result = func(nums.copy(), n)  # Copy to avoid mutation affecting other tests
            status = "✅" if result == expected else "❌"
            print(f"{status} Input: {nums[:2*n]}, n={n}")
            print(f"   Output:   {result}")
            print(f"   Expected: {expected}")


# ============================================================================
# PERFORMANCE COMPARISON
# ============================================================================
def compare_performance() -> None:
    """Compare execution time of different approaches"""
    import timeit
    from typing import Any

    test_input = list(range(1000)) + list(range(1000, 2000))
    n = 1000

    # Create local scope with test data
    test_globals: dict[str, Any] = {**globals(), 'test_input': test_input, 'n': n}

    approaches = [
        ("Basic Loop", "shuffle_basic(test_input.copy(), n)"),
        ("List Comprehension", "shuffle_comprehension(test_input.copy(), n)"),
        ("Zip + Chain", "shuffle_zip_chain(test_input.copy(), n)"),
        ("Zip + Unpack", "shuffle_zip_unpack(test_input.copy(), n)"),
        ("Enumerate", "shuffle_enumerate(test_input.copy(), n)"),
        ("In-Place", "shuffle_in_place(test_input.copy(), n)"),
    ]

    print(f"\n{'='*60}")
    print(f"PERFORMANCE COMPARISON (1000 iterations)")
    print(f"{'='*60}")

    for name, code in approaches:
        time = timeit.timeit(code, globals=test_globals, number=1000)
        print(f"{name:25} {time:.4f} seconds")


if __name__ == "__main__":
    print("LeetCode #1470: Shuffle the Array\n")
    run_tests()

    print("\n" + "="*60)
    print("RECOMMENDATION")
    print("="*60)
    print("""
For interviews, use: shuffle_comprehension() or shuffle_zip_unpack()
- Most Pythonic and readable
- One-liner that's easy to explain
- Shows Python mastery

For optimization discussions: shuffle_in_place()
- O(1) space complexity
- Shows advanced bit manipulation knowledge
- Great follow-up when interviewer asks "can you optimize space?"

Avoid: shuffle_deque()
- No real benefit over list in this problem
- Adds unnecessary import
    """)

    # Uncomment to see performance comparison
    # compare_performance()
