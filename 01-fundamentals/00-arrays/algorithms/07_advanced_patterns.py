"""
07. Advanced Array Patterns
============================

More sophisticated algorithms that appear in medium/hard problems.
These separate good candidates from great ones!
"""

# ============================================
# 1. DUTCH NATIONAL FLAG (3-Way Partition)
# ============================================

def sort_colors(arr):
    """
    Sort array of 0s, 1s, and 2s in-place

    ANALOGY: Sorting balls - red left, white middle, blue right
    (Dutch flag colors)

    Time: O(n) - single pass ⭐
    Space: O(1)

    INTERVIEW: LeetCode #75 - Classic!

    KEY PATTERN: Three pointers
    - low: boundary for 0s
    - mid: current element
    - high: boundary for 2s
    """
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr


def partition_around_pivot(arr, pivot):
    """
    Partition array: smaller | equal | larger

    ANALOGY: Organizing books by price around $20

    Time: O(n)
    Space: O(1)

    Used in: QuickSort, QuickSelect
    """
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] < pivot:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == pivot:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr


# ============================================
# 2. MOORE'S VOTING ALGORITHM
# ============================================

def majority_element(arr):
    """
    Find element appearing more than n/2 times

    ANALOGY: Election - candidate getting > 50% votes wins
    Like a battle - winner survives if they outnumber others

    Time: O(n) ⭐
    Space: O(1)

    INTERVIEW: LeetCode #169 - Brilliant algorithm!

    KEY INSIGHT: Majority element cancels out all others
    """
    candidate = None
    count = 0

    # Phase 1: Find candidate
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Phase 2: Verify (optional if majority guaranteed)
    if arr.count(candidate) > len(arr) // 2:
        return candidate
    return -1


def majority_element_n_3(arr):
    """
    Find all elements appearing more than n/3 times

    ANALOGY: Top 2 candidates in election (max 2 can have > n/3)

    Time: O(n) ⭐
    Space: O(1)

    INTERVIEW: LeetCode #229 - Harder version!
    """
    if not arr:
        return []

    # At most 2 elements can appear > n/3 times
    candidate1, candidate2 = None, None
    count1, count2 = 0, 0

    # Find candidates
    for num in arr:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1 = num
            count1 = 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1

    # Verify candidates
    result = []
    threshold = len(arr) // 3

    if arr.count(candidate1) > threshold:
        result.append(candidate1)
    if candidate2 != candidate1 and arr.count(candidate2) > threshold:
        result.append(candidate2)

    return result


# ============================================
# 3. NEXT GREATER/SMALLER ELEMENT
# ============================================

def next_greater_element(arr):
    """
    For each element, find next greater element to the right

    ANALOGY: Stack of plates - keep removing shorter ones

    Time: O(n) ⭐
    Space: O(n)

    INTERVIEW: Very common pattern! Monotonic stack

    Example: [4,5,2,25] → [5,25,25,-1]
    """
    n = len(arr)
    result = [-1] * n
    stack = []  # Stores indices

    # Traverse from right to left
    for i in range(n - 1, -1, -1):
        # Pop smaller elements
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()

        # Top of stack is next greater
        if stack:
            result[i] = arr[stack[-1]]

        stack.append(i)

    return result


def next_smaller_element(arr):
    """
    For each element, find next smaller element

    Time: O(n)
    Space: O(n)
    """
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()

        if stack:
            result[i] = arr[stack[-1]]

        stack.append(i)

    return result


# ============================================
# 4. MERGE SORTED ARRAYS
# ============================================

def merge_sorted_arrays(arr1, arr2):
    """
    Merge two sorted arrays

    ANALOGY: Merging two sorted decks of cards

    Time: O(m + n) ⭐
    Space: O(m + n) for result

    INTERVIEW: Foundation of merge sort, LeetCode #88
    """
    result = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # Append remaining
    result.extend(arr1[i:])
    result.extend(arr2[j:])

    return result


def merge_in_place(arr1, m, arr2, n):
    """
    Merge arr2 into arr1 (arr1 has extra space at end)

    ANALOGY: Packing suitcase from back to front

    Time: O(m + n) ⭐
    Space: O(1)

    INTERVIEW: LeetCode #88 - Work backwards!
    """
    i, j, k = m - 1, n - 1, m + n - 1

    # Fill from back
    while i >= 0 and j >= 0:
        if arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1
        k -= 1

    # Copy remaining from arr2 (if any)
    while j >= 0:
        arr1[k] = arr2[j]
        j -= 1
        k -= 1

    return arr1


# ============================================
# 5. TRAPPING RAIN WATER
# ============================================

def trap_rain_water(heights):
    """
    Calculate trapped rainwater between bars

    ANALOGY: Water fills to height of shorter boundary

    Time: O(n) ⭐
    Space: O(1) using two pointers

    INTERVIEW: LeetCode #42 - Hard but common!

    KEY INSIGHT: Water at position = min(left_max, right_max) - height
    """
    if not heights:
        return 0

    left, right = 0, len(heights) - 1
    left_max, right_max = 0, 0
    water = 0

    while left < right:
        if heights[left] < heights[right]:
            if heights[left] >= left_max:
                left_max = heights[left]
            else:
                water += left_max - heights[left]
            left += 1
        else:
            if heights[right] >= right_max:
                right_max = heights[right]
            else:
                water += right_max - heights[right]
            right -= 1

    return water


# ============================================
# 6. CONTAINER WITH MOST WATER
# ============================================

def max_area(heights):
    """
    Find two lines that with x-axis form container with most water

    ANALOGY: Two poles forming a bucket - maximize area

    Time: O(n) ⭐
    Space: O(1)

    INTERVIEW: LeetCode #11 - Two pointers!

    KEY INSIGHT: Move pointer at shorter height (bottleneck)
    """
    left, right = 0, len(heights) - 1
    max_water = 0

    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        water = width * height
        max_water = max(max_water, water)

        # Move pointer at shorter side
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_water


# ============================================
# 7. FIRST MISSING POSITIVE
# ============================================

def first_missing_positive(arr):
    """
    Find smallest missing positive integer

    ANALOGY: Finding first empty seat in theater

    Time: O(n) ⭐
    Space: O(1)

    INTERVIEW: LeetCode #41 - Hard! Cyclic sort pattern

    KEY TRICK: Use array itself as hash table
    Put each number in its "correct" position
    """
    n = len(arr)

    # Phase 1: Place numbers in correct positions
    # Number k should be at index k-1
    for i in range(n):
        while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
            # Swap arr[i] to its correct position
            correct_idx = arr[i] - 1
            arr[i], arr[correct_idx] = arr[correct_idx], arr[i]

    # Phase 2: Find first missing
    for i in range(n):
        if arr[i] != i + 1:
            return i + 1

    return n + 1


# ============================================
# 8. INTERVAL MERGING
# ============================================

def merge_intervals(intervals):
    """
    Merge overlapping intervals

    ANALOGY: Combining overlapping meeting times

    Time: O(n log n) - sorting ⭐
    Space: O(n)

    INTERVIEW: LeetCode #56 - Very common!
    """
    if not intervals:
        return []

    # Sort by start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]

        if current[0] <= last[1]:  # Overlap
            # Merge by extending end
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)

    return merged


# ============================================
# 9. SET MATRIX ZEROS
# ============================================

def set_matrix_zeros(matrix):
    """
    If element is 0, set entire row and column to 0

    ANALOGY: Marking which rows/columns to destroy

    Time: O(m * n) ⭐
    Space: O(1) using first row/col as markers

    INTERVIEW: LeetCode #73 - Clever!
    """
    if not matrix:
        return

    rows, cols = len(matrix), len(matrix[0])
    first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
    first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

    # Use first row/col as markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Set zeros based on markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Handle first row and column
    if first_row_zero:
        for j in range(cols):
            matrix[0][j] = 0

    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0

    return matrix


# ============================================
# COMPLEXITY SUMMARY
# ============================================

"""
Algorithm                  | Time       | Space | Difficulty
---------------------------|------------|-------|------------
Dutch National Flag        | O(n)       | O(1)  | Medium
Moore's Voting             | O(n)       | O(1)  | Medium
Next Greater Element       | O(n)       | O(n)  | Medium
Merge Sorted Arrays        | O(m+n)     | O(1)* | Easy
Trapping Rain Water        | O(n)       | O(1)  | Hard ⭐
Container Water            | O(n)       | O(1)  | Medium
First Missing Positive     | O(n)       | O(1)  | Hard ⭐
Merge Intervals            | O(n log n) | O(n)  | Medium
Set Matrix Zeros           | O(m*n)     | O(1)  | Medium

*Can be done in-place

PATTERNS TO MASTER:
1. Three-way partition (Dutch flag)
2. Voting algorithm (majority finding)
3. Monotonic stack (next greater/smaller)
4. Two pointers (water problems)
5. Cyclic sort (first missing positive)
"""


if __name__ == "__main__":
    print("=" * 60)
    print("ADVANCED ARRAY PATTERNS DEMO")
    print("=" * 60)

    # 1. Dutch National Flag
    arr = [2, 0, 2, 1, 1, 0]
    print(f"\n1. Sort Colors: {arr}")
    print(f"   After sorting: {sort_colors(arr.copy())}")

    # 2. Majority Element
    arr = [3, 2, 3]
    print(f"\n2. Majority Element: {arr}")
    print(f"   Result: {majority_element(arr)}")

    # 3. Next Greater
    arr = [4, 5, 2, 25]
    print(f"\n3. Next Greater: {arr}")
    print(f"   Result: {next_greater_element(arr)}")

    # 4. Merge Sorted
    arr1, arr2 = [1, 3, 5], [2, 4, 6]
    print(f"\n4. Merge: {arr1} and {arr2}")
    print(f"   Result: {merge_sorted_arrays(arr1, arr2)}")

    # 5. Trap Water
    heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(f"\n5. Trap Rain Water: {heights}")
    print(f"   Water trapped: {trap_rain_water(heights)}")

    # 6. Container
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"\n6. Container Water: {heights}")
    print(f"   Max area: {max_area(heights)}")

    # 7. First Missing Positive
    arr = [3, 4, -1, 1]
    print(f"\n7. First Missing Positive: {arr}")
    print(f"   Result: {first_missing_positive(arr.copy())}")

    # 8. Merge Intervals
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(f"\n8. Merge Intervals: {intervals}")
    print(f"   Merged: {merge_intervals(intervals)}")

    print("\n" + "=" * 60)
    print("✅ Advanced patterns demonstrated!")
    print("\nTHESE SEPARATE GOOD FROM GREAT:")
    print("- Dutch Flag: O(n) partitioning")
    print("- Moore's Voting: O(1) space majority finding")
    print("- Monotonic Stack: Next greater/smaller")
    print("- Two Pointers: Water trapping/container")
