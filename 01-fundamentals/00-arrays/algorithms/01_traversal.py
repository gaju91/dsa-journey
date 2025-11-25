"""
01. Array Traversal
===================

ANALOGY: Like reading a book page by page, from start to finish.
You visit each element once, in order.

INTERVIEW TIP: Traversal is the foundation. Almost every array algorithm
involves traversing. Master different ways to traverse!
"""

# ============================================
# APPROACH 1: BASIC FOR LOOP
# ============================================
# Time: O(n), Space: O(1)

def traverse_basic(arr):
    """Visit each element using range and index"""
    for i in range(len(arr)):
        print(f"Index {i}: {arr[i]}")


# ============================================
# APPROACH 2: PYTHONIC ITERATION
# ============================================
# Time: O(n), Space: O(1)

def traverse_pythonic(arr):
    """Visit each element directly (preferred in Python)"""
    for element in arr:
        print(element)


# ============================================
# APPROACH 3: WITH INDEX (ENUMERATE)
# ============================================
# Time: O(n), Space: O(1)

def traverse_with_index(arr):
    """Get both index and value"""
    for index, value in enumerate(arr):
        print(f"arr[{index}] = {value}")


# ============================================
# APPROACH 4: WHILE LOOP
# ============================================
# Time: O(n), Space: O(1)

def traverse_while(arr):
    """Using while loop (useful for complex conditions)"""
    i = 0
    while i < len(arr):
        print(arr[i])
        i += 1


# ============================================
# APPROACH 5: REVERSE TRAVERSAL
# ============================================
# Time: O(n), Space: O(1)

def traverse_reverse(arr):
    """Visit elements from end to start"""
    # Method 1: Using reversed()
    for element in reversed(arr):
        print(element)

    # Method 2: Using range backwards
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i])

    # Method 3: Using negative indices
    for i in range(-1, -len(arr) - 1, -1):
        print(arr[i])


# ============================================
# INTERVIEW VARIATIONS
# ============================================

def traverse_with_operation(arr):
    """
    Traverse and perform operation (sum, product, etc.)

    ANALOGY: Like a cashier scanning items and adding prices
    """
    total = 0
    for num in arr:
        total += num
    return total


def traverse_with_condition(arr):
    """
    Traverse with filtering

    ANALOGY: Like security checking bags - only interested in certain items
    """
    evens = []
    for num in arr:
        if num % 2 == 0:
            evens.append(num)
    return evens


def traverse_two_arrays(arr1, arr2):
    """
    Parallel traversal

    ANALOGY: Like reading subtitles while watching a movie
    """
    result = []
    for a, b in zip(arr1, arr2):
        result.append(a + b)
    return result


def traverse_nested(matrix):
    """
    Traverse 2D array

    ANALOGY: Like reading a spreadsheet row by row, cell by cell
    """
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()


def traverse_with_step(arr, step=2):
    """
    Skip elements

    ANALOGY: Like reading every other line in a book
    """
    for i in range(0, len(arr), step):
        print(arr[i])


# ============================================
# COMMON INTERVIEW PATTERNS
# ============================================

def find_first_occurrence(arr, target):
    """
    Find first element matching condition

    Time: O(n) worst case
    Space: O(1)

    ANALOGY: Looking for a specific book in a shelf, stop when found
    """
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1


def count_occurrences(arr, target):
    """
    Count how many times element appears

    Time: O(n)
    Space: O(1)
    """
    count = 0
    for element in arr:
        if element == target:
            count += 1
    return count


def collect_indices(arr, target):
    """
    Collect all positions where element appears

    Time: O(n)
    Space: O(k) where k = number of occurrences
    """
    indices = []
    for i, element in enumerate(arr):
        if element == target:
            indices.append(i)
    return indices


# ============================================
# PERFORMANCE TIPS
# ============================================

"""
1. Prefer 'for element in arr' over 'for i in range(len(arr))'
   - More Pythonic
   - Faster (no indexing overhead)
   - Cleaner code

2. Use enumerate() when you need both index and value
   - Don't manually maintain counter

3. Use reversed() instead of range(len-1, -1, -1)
   - More readable

4. Short-circuit when possible
   - Use 'break' when found what you need
   - Use 'any()' or 'all()' for boolean checks

5. Avoid modifying array while traversing
   - Can cause skipped elements or infinite loops
"""

# ============================================
# INTERVIEW GOTCHAS
# ============================================

def demonstrate_gotcha():
    """Common mistakes during traversal"""

    # GOTCHA 1: Off-by-one errors
    arr = [1, 2, 3, 4, 5]
    # Wrong: for i in range(len(arr) + 1)  # IndexError!
    # Right: for i in range(len(arr))

    # GOTCHA 2: Modifying while iterating
    arr = [1, 2, 3, 4, 5]
    # Wrong:
    # for num in arr:
    #     if num % 2 == 0:
    #         arr.remove(num)  # Skips elements!
    # Right: Iterate over copy
    for num in arr[:]:
        if num % 2 == 0:
            arr.remove(num)

    # GOTCHA 3: Empty array
    arr = []
    # Always check if empty before accessing
    if arr:
        first = arr[0]


# ============================================
# COMPLEXITY ANALYSIS
# ============================================

"""
Time Complexity:
- Single pass: O(n)
- Nested (2D): O(n * m) where n=rows, m=cols
- With operation: O(n * k) where k = operation cost

Space Complexity:
- Usually O(1) - just iterating
- O(k) if collecting results
- O(n) if creating new array

KEY POINT: Traversal itself is O(n) time, O(1) space.
The operations you perform during traversal determine overall complexity.
"""


if __name__ == "__main__":
    print("=" * 50)
    print("ARRAY TRAVERSAL DEMO")
    print("=" * 50)

    arr = [10, 20, 30, 40, 50]

    print("\n1. Basic Traversal:")
    for x in arr:
        print(x, end=' ')

    print("\n\n2. With Index:")
    for i, x in enumerate(arr):
        print(f"arr[{i}]={x}", end=' ')

    print("\n\n3. Reverse:")
    for x in reversed(arr):
        print(x, end=' ')

    print("\n\n4. Sum (traversal with operation):")
    print(f"Sum: {traverse_with_operation(arr)}")

    print("\n\n5. Find Element:")
    target = 30
    index = find_first_occurrence(arr, target)
    print(f"Found {target} at index {index}")

    print("\n\n6. Count:")
    arr_with_dups = [1, 2, 2, 3, 2, 4]
    print(f"Array: {arr_with_dups}")
    print(f"Count of 2: {count_occurrences(arr_with_dups, 2)}")

    print("\n\n7. 2D Traversal:")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Matrix:")
    traverse_nested(matrix)

    print("\n" + "=" * 50)
    print("✅ Traversal patterns demonstrated!")
