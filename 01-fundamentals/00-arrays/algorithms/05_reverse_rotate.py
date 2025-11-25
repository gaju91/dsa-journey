"""
05. Array Reverse and Rotation
===============================

ANALOGY:
- REVERSE: Reading a book backwards
- ROTATE: Circular shifting - like a carousel or rotating queue

These are FUNDAMENTAL manipulations - appear in many problems!
"""

# ============================================
# PART 1: REVERSE ARRAY
# ============================================

def reverse_using_extra_space(arr):
    """
    Reverse using new array

    ANALOGY: Writing sentences right-to-left on new paper

    Time: O(n)
    Space: O(n) - creates new array

    NOT OPTIMAL for interviews!
    """
    return arr[::-1]  # or list(reversed(arr))


def reverse_in_place(arr):
    """
    Reverse array IN-PLACE using two pointers

    ANALOGY: Swapping positions of people at both ends of line,
    moving toward center

    Time: O(n)
    Space: O(1) - THIS IS OPTIMAL! ✅

    INTERVIEW: This is the technique they want!
    """
    left, right = 0, len(arr) - 1

    while left < right:
        # Swap
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


def reverse_using_python_method(arr):
    """
    Using built-in reverse() method

    Time: O(n)
    Space: O(1)

    INTERVIEW: Know this exists, but show you can code it manually!
    """
    arr.reverse()
    return arr


def reverse_part_of_array(arr, left, right):
    """
    Reverse only a portion [left, right]

    ANALOGY: Flipping pages in middle of a book

    Time: O(n)
    Space: O(1)

    INTERVIEW: Used in rotation, palindrome problems!
    """
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


# ============================================
# PART 2: ARRAY ROTATION
# ============================================

def rotate_right_naive(arr, k):
    """
    Rotate array RIGHT by k positions (Brute Force)

    ANALOGY: Moving people in circular queue k times

    Example: [1,2,3,4,5] rotate right by 2 → [4,5,1,2,3]

    Time: O(n * k) - rotate one by one, k times
    Space: O(1)

    NOT OPTIMAL!
    """
    n = len(arr)
    k = k % n  # Handle k > n

    for _ in range(k):
        # Rotate by 1
        last = arr[-1]
        for i in range(n - 1, 0, -1):
            arr[i] = arr[i - 1]
        arr[0] = last

    return arr


def rotate_right_using_extra_space(arr, k):
    """
    Rotate using temporary array

    Time: O(n)
    Space: O(n)

    Better than naive, but still not optimal
    """
    n = len(arr)
    k = k % n

    rotated = [0] * n
    for i in range(n):
        rotated[(i + k) % n] = arr[i]

    arr[:] = rotated
    return arr


def rotate_right_reversal(arr, k):
    """
    Rotate using REVERSAL TRICK

    ANALOGY: Magic trick - reverse whole, reverse parts!

    Example: [1,2,3,4,5] rotate right by 2
    Step 1: Reverse all → [5,4,3,2,1]
    Step 2: Reverse first k → [4,5,3,2,1]
    Step 3: Reverse rest → [4,5,1,2,3] ✓

    Time: O(n) - 3 reversals
    Space: O(1)

    THIS IS THE OPTIMAL SOLUTION! ⭐

    INTERVIEW: LeetCode #189 - This trick impresses!
    """
    n = len(arr)
    k = k % n

    # Step 1: Reverse entire array
    reverse_part_of_array(arr, 0, n - 1)

    # Step 2: Reverse first k elements
    reverse_part_of_array(arr, 0, k - 1)

    # Step 3: Reverse remaining n-k elements
    reverse_part_of_array(arr, k, n - 1)

    return arr


def rotate_left_reversal(arr, k):
    """
    Rotate LEFT by k positions

    Example: [1,2,3,4,5] rotate left by 2 → [3,4,5,1,2]

    Time: O(n)
    Space: O(1)

    TRICK: Left rotation by k = Right rotation by (n-k)
    OR: Reverse order is opposite
    """
    n = len(arr)
    k = k % n

    # Method 1: Convert to right rotation
    # return rotate_right_reversal(arr, n - k)

    # Method 2: Reverse in different order
    # Step 1: Reverse first k
    reverse_part_of_array(arr, 0, k - 1)

    # Step 2: Reverse remaining
    reverse_part_of_array(arr, k, n - 1)

    # Step 3: Reverse all
    reverse_part_of_array(arr, 0, n - 1)

    return arr


def rotate_right_cyclic_replacements(arr, k):
    """
    Rotate using cyclic replacements (Advanced)

    ANALOGY: Musical chairs - everyone moves k seats

    Time: O(n)
    Space: O(1)

    This is elegant but complex - reversal method is simpler
    """
    n = len(arr)
    k = k % n
    count = 0
    start = 0

    while count < n:
        current = start
        prev = arr[start]

        while True:
            next_pos = (current + k) % n
            arr[next_pos], prev = prev, arr[next_pos]
            current = next_pos
            count += 1

            if current == start:
                break

        start += 1

    return arr


# ============================================
# INTERVIEW VARIATIONS
# ============================================

def rotate_and_query(arr, rotations, queries):
    """
    After rotating, answer element queries

    Example: After rotating [1,2,3,4,5] right by 2,
    what's at index 1? → 5

    TRICK: Don't actually rotate! Calculate new position!

    Time: O(q) for q queries
    Space: O(1)
    """
    n = len(arr)
    k = rotations % n

    results = []
    for query_idx in queries:
        # Original position of element now at query_idx
        original_idx = (query_idx - k + n) % n
        results.append(arr[original_idx])

    return results


def check_if_rotated(arr1, arr2):
    """
    Check if arr2 is rotation of arr1

    ANALOGY: Are these two copies of same circular sequence?

    Example: [1,2,3,4] and [3,4,1,2] → True

    Time: O(n)
    Space: O(n)

    TRICK: arr2 is rotation of arr1 if arr2 exists in arr1+arr1
    """
    if len(arr1) != len(arr2):
        return False

    # Concatenate arr1 with itself
    doubled = arr1 + arr1

    # Check if arr2 is substring (sublist)
    # Convert to strings for easier checking
    return str(arr2)[1:-1] in str(doubled)[1:-1]


def count_rotations(arr):
    """
    Count how many times sorted array was rotated

    Example: [4,5,6,7,0,1,2] → rotated 4 times

    ANALOGY: How many steps back to restore order?

    Time: O(log n) using binary search
    Space: O(1)

    KEY: Rotation count = index of minimum element
    """
    n = len(arr)
    left, right = 0, n - 1

    while left <= right:
        # Already sorted
        if arr[left] <= arr[right]:
            return left

        mid = left + (right - left) // 2
        next_idx = (mid + 1) % n
        prev_idx = (mid - 1 + n) % n

        # Check if mid is minimum
        if arr[mid] <= arr[next_idx] and arr[mid] <= arr[prev_idx]:
            return mid

        # Decide which half
        if arr[mid] <= arr[right]:
            right = mid - 1
        else:
            left = mid + 1

    return 0


# ============================================
# COMPLEXITY SUMMARY
# ============================================

"""
Operation                  | Time    | Space | Method
---------------------------|---------|-------|------------------
Reverse (extra space)      | O(n)    | O(n)  | New array
Reverse (in-place)         | O(n)    | O(1)  | Two pointers ✅
Rotate (naive)             | O(n*k)  | O(1)  | One by one
Rotate (extra space)       | O(n)    | O(n)  | Temp array
Rotate (reversal trick)    | O(n)    | O(1)  | Best! ⭐
Check rotation             | O(n)    | O(n)  | String trick
Count rotations            | O(log n)| O(1)  | Binary search

INTERVIEW GOLD:
1. In-place reverse using two pointers
2. Rotation using reversal trick (3 reversals)
3. These patterns appear EVERYWHERE!
"""


if __name__ == "__main__":
    print("=" * 60)
    print("REVERSE & ROTATION DEMO")
    print("=" * 60)

    # Demo 1: Reverse in-place
    arr = [1, 2, 3, 4, 5]
    print(f"\n1. Original: {arr}")
    reverse_in_place(arr.copy())  # Use copy to preserve original
    print(f"   Reversed: {reverse_in_place(arr.copy())}")

    # Demo 2: Reverse part
    arr = [1, 2, 3, 4, 5]
    print(f"\n2. Original: {arr}")
    result = arr.copy()
    reverse_part_of_array(result, 1, 3)  # Reverse indices 1-3
    print(f"   Reverse [1:3]: {result}")

    # Demo 3: Rotate right
    arr = [1, 2, 3, 4, 5]
    print(f"\n3. Original: {arr}")
    result = arr.copy()
    rotate_right_reversal(result, 2)
    print(f"   Rotate right by 2: {result}")

    # Demo 4: Rotate left
    arr = [1, 2, 3, 4, 5]
    print(f"\n4. Original: {arr}")
    result = arr.copy()
    rotate_left_reversal(result, 2)
    print(f"   Rotate left by 2: {result}")

    # Demo 5: Check if rotated
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [3, 4, 5, 1, 2]
    print(f"\n5. Array 1: {arr1}")
    print(f"   Array 2: {arr2}")
    print(f"   Is arr2 rotation of arr1? {check_if_rotated(arr1, arr2)}")

    # Demo 6: Count rotations
    arr = [4, 5, 6, 7, 0, 1, 2]
    print(f"\n6. Rotated sorted: {arr}")
    print(f"   Rotation count: {count_rotations(arr)}")

    print("\n" + "=" * 60)
    print("✅ Reverse & Rotation demonstrated!")
    print("\nKEY PATTERNS:")
    print("- Two pointers for reverse: O(n), O(1)")
    print("- Reversal trick for rotation: 3 reversals = optimal!")
    print("- These appear in: palindromes, rotation problems, cyclic shifts")
