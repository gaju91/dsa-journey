"""
04. Array Searching
===================

ANALOGY: Finding a name in a phone book.
- LINEAR SEARCH: Check every page (slow but works on unsorted)
- BINARY SEARCH: Open middle, decide left/right (fast but needs sorted)

INTERVIEW GOLD: Binary search variations are EXTREMELY common!
Master the template!
"""

# ============================================
# LINEAR SEARCH - O(n)
# ============================================

def linear_search(arr, target):
    """
    Search by checking each element

    ANALOGY: Looking for a book by checking every shelf one by one

    Time: O(n) - might check all elements
    Space: O(1)

    WHEN TO USE:
    - Array is unsorted
    - Array is small
    - Searching once (not repeatedly)
    """
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1


def linear_search_all(arr, target):
    """
    Find ALL occurrences

    Time: O(n) - must check all
    Space: O(k) where k = number of occurrences
    """
    indices = []
    for i, element in enumerate(arr):
        if element == target:
            indices.append(i)
    return indices


# ============================================
# BINARY SEARCH - O(log n)
# ============================================

def binary_search(arr, target):
    """
    Search in SORTED array by repeatedly halving

    ANALOGY: Looking up a word in dictionary - open middle,
    decide if word is before or after, repeat

    Time: O(log n) - halves search space each time!
    Space: O(1)

    REQUIREMENTS: Array MUST be sorted!

    This is the STANDARD TEMPLATE - memorize it!
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return -1  # Not found


def binary_search_recursive(arr, target, left=None, right=None):
    """
    Binary search using recursion

    Time: O(log n)
    Space: O(log n) - recursion stack

    Less common in interviews, but good to know
    """
    if left is None:
        left, right = 0, len(arr) - 1

    if left > right:
        return -1

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


# ============================================
# BINARY SEARCH VARIATIONS (INTERVIEW GOLD!)
# ============================================

def binary_search_leftmost(arr, target):
    """
    Find FIRST (leftmost) occurrence

    ANALOGY: Find first person with name "Alice" in sorted list

    Time: O(log n)

    INTERVIEW: LeetCode #34 - Find First and Last Position
    """
    left, right = 0, len(arr)
    result = -1

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid
        else:
            result = mid
            right = mid  # Keep searching left

    return result


def binary_search_rightmost(arr, target):
    """
    Find LAST (rightmost) occurrence

    Time: O(log n)
    """
    left, right = 0, len(arr)
    result = -1

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid
        else:
            result = mid
            left = mid + 1  # Keep searching right

    return result


def binary_search_insert_position(arr, target):
    """
    Find position where target should be inserted

    ANALOGY: Where to insert a card in sorted hand

    Time: O(log n)

    INTERVIEW: LeetCode #35 - Search Insert Position
    This is the LOWER BOUND problem!
    """
    left, right = 0, len(arr)

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


def binary_search_range(arr, target):
    """
    Find range [start, end] of target occurrences

    Time: O(log n)

    INTERVIEW: LeetCode #34
    """
    if not arr:
        return [-1, -1]

    left = binary_search_leftmost(arr, target)
    if left == -1:
        return [-1, -1]

    right = binary_search_rightmost(arr, target)
    return [left, right]


# ============================================
# BINARY SEARCH ON ANSWER (ADVANCED)
# ============================================

def binary_search_minimum_capacity(arr, days):
    """
    Example: Ship packages within D days
    Find minimum capacity needed

    ANALOGY: Finding minimum truck size to deliver all packages

    Pattern: "Minimize maximum" or "Maximize minimum"

    Time: O(n log(sum-max))

    INTERVIEW: Very common pattern!
    - Koko Eating Bananas
    - Capacity To Ship Packages
    - Split Array Largest Sum
    """
    def can_ship(capacity):
        days_needed = 1
        current_load = 0

        for weight in arr:
            if current_load + weight > capacity:
                days_needed += 1
                current_load = weight
            else:
                current_load += weight

        return days_needed <= days

    left = max(arr)  # At least max element
    right = sum(arr)  # At most sum of all

    while left < right:
        mid = left + (right - left) // 2
        if can_ship(mid):
            right = mid  # Try smaller capacity
        else:
            left = mid + 1  # Need larger capacity

    return left


# ============================================
# SEARCH IN ROTATED SORTED ARRAY
# ============================================

def search_rotated(arr, target):
    """
    Search in rotated sorted array

    ANALOGY: Phone book with pages shuffled but each section still sorted

    Example: [4,5,6,7,0,1,2] rotated at index 4

    Time: O(log n)

    INTERVIEW: LeetCode #33 - Very popular!
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        # Determine which half is sorted
        if arr[left] <= arr[mid]:  # Left half sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1  # Target in left half
            else:
                left = mid + 1  # Target in right half
        else:  # Right half sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1  # Target in right half
            else:
                right = mid - 1  # Target in left half

    return -1


# ============================================
# INTERPOLATION SEARCH (BONUS)
# ============================================

def interpolation_search(arr, target):
    """
    Better than binary for uniformly distributed data

    ANALOGY: Looking up a name - you know "Smith" is near end,
    so you start there instead of middle

    Time: O(log log n) average, O(n) worst case
    Space: O(1)

    WHEN: Data is uniformly distributed
    """
    left, right = 0, len(arr) - 1

    while left <= right and arr[left] <= target <= arr[right]:
        if left == right:
            if arr[left] == target:
                return left
            return -1

        # Interpolation formula
        pos = left + ((target - arr[left]) * (right - left) //
                     (arr[right] - arr[left]))

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1

    return -1


# ============================================
# JUMP SEARCH (BONUS)
# ============================================

def jump_search(arr, target):
    """
    Jump ahead by blocks, then linear search

    ANALOGY: Looking for a page - jump by chapters first,
    then scan pages

    Time: O(√n)
    Space: O(1)

    WHEN: Array is sorted but binary search overhead is high
    """
    import math

    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    # Jump to find block containing target
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Linear search in block
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1

    if arr[prev] == target:
        return prev

    return -1


# ============================================
# COMPLEXITY COMPARISON
# ============================================

"""
Algorithm          | Time        | Space | When to Use
-------------------|-------------|-------|------------------------
Linear Search      | O(n)        | O(1)  | Unsorted, small arrays
Binary Search      | O(log n)    | O(1)  | Sorted arrays (BEST)
Interpolation      | O(log log n)| O(1)  | Uniform distribution
Jump Search        | O(√n)       | O(1)  | Sorted, no random access

BINARY SEARCH WINS for sorted arrays!

Why O(log n) is fast:
Array size | Max comparisons
-----------|----------------
       100 |              7
     1,000 |             10
 1,000,000 |             20
 1,000,000,000 |         30

That's why "sorted" is so powerful!
"""


if __name__ == "__main__":
    print("=" * 60)
    print("ARRAY SEARCHING DEMO")
    print("=" * 60)

    # Demo 1: Linear Search
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"\n1. Unsorted: {arr}")
    target = 22
    idx = linear_search(arr, target)
    print(f"   Linear search for {target}: index {idx}")

    # Demo 2: Binary Search
    arr = [11, 12, 22, 25, 34, 64, 90]
    print(f"\n2. Sorted: {arr}")
    target = 25
    idx = binary_search(arr, target)
    print(f"   Binary search for {target}: index {idx}")

    # Demo 3: Binary Search (not found)
    target = 50
    idx = binary_search(arr, target)
    print(f"   Binary search for {target}: index {idx}")

    # Demo 4: Find range
    arr = [5, 7, 7, 8, 8, 8, 10]
    print(f"\n3. With duplicates: {arr}")
    target = 8
    range_indices = binary_search_range(arr, target)
    print(f"   Range of {target}: {range_indices}")

    # Demo 5: Insert position
    arr = [1, 3, 5, 6]
    print(f"\n4. Array: {arr}")
    target = 5
    pos = binary_search_insert_position(arr, target)
    print(f"   Insert position for {target}: {pos}")
    target = 2
    pos = binary_search_insert_position(arr, target)
    print(f"   Insert position for {target}: {pos}")

    # Demo 6: Rotated array
    arr = [4, 5, 6, 7, 0, 1, 2]
    print(f"\n5. Rotated sorted: {arr}")
    target = 0
    idx = search_rotated(arr, target)
    print(f"   Search {target}: index {idx}")

    print("\n" + "=" * 60)
    print("✅ All searching methods demonstrated!")
    print("\nKEY TAKEAWAYS:")
    print("- Linear: O(n) - works on any array")
    print("- Binary: O(log n) - requires sorted, VERY fast! ⚡")
    print("- Binary search template is GOLD - memorize it!")
