"""
12. Common Array Patterns and Tricks
=====================================
Essential patterns for coding interviews.
"""

# ============================================
# 1. TWO POINTERS
# ============================================

# Pattern: Start from both ends and move inward

def two_sum_sorted(arr, target):
    """Find two numbers that add to target in sorted array"""
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return [-1, -1]


def reverse_array(arr):
    """Reverse array in-place"""
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


def is_palindrome(s):
    """Check if string is palindrome"""
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


# ============================================
# 2. SLIDING WINDOW
# ============================================

# Fixed window
def max_sum_subarray(arr, k):
    """Maximum sum of subarray of size k"""
    if len(arr) < k:
        return -1

    # First window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide window
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


# Variable window
def smallest_subarray_with_sum(arr, target):
    """Smallest subarray with sum >= target"""
    min_length = float('inf')
    window_sum = 0
    left = 0

    for right in range(len(arr)):
        window_sum += arr[right]

        while window_sum >= target:
            min_length = min(min_length, right - left + 1)
            window_sum -= arr[left]
            left += 1

    return min_length if min_length != float('inf') else 0


# ============================================
# 3. PREFIX SUM
# ============================================

def build_prefix_sum(arr):
    """Build prefix sum array"""
    prefix = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]
    return prefix


def range_sum(prefix, left, right):
    """Sum of elements from left to right (inclusive)"""
    return prefix[right + 1] - prefix[left]


# Count subarrays with sum = k
def subarray_sum_equals_k(arr, k):
    """Count subarrays with sum equal to k"""
    count = 0
    prefix_sum = 0
    prefix_count = {0: 1}

    for num in arr:
        prefix_sum += num
        if prefix_sum - k in prefix_count:
            count += prefix_count[prefix_sum - k]
        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

    return count


# ============================================
# 4. KADANE'S ALGORITHM
# ============================================

def max_subarray_sum(arr):
    """Maximum subarray sum (Kadane's algorithm)"""
    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


def max_subarray_indices(arr):
    """Return max sum with start and end indices"""
    max_sum = arr[0]
    current_sum = arr[0]
    start = end = temp_start = 0

    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return max_sum, start, end


# ============================================
# 5. DUTCH NATIONAL FLAG (3-WAY PARTITION)
# ============================================

def sort_colors(arr):
    """Sort array of 0s, 1s, and 2s in-place"""
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


# ============================================
# 6. MOORE'S VOTING ALGORITHM
# ============================================

def majority_element(arr):
    """Find element appearing more than n/2 times"""
    candidate = None
    count = 0

    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Verify (optional if majority guaranteed)
    if arr.count(candidate) > len(arr) // 2:
        return candidate
    return -1


# ============================================
# 7. CYCLIC SORT
# ============================================

def cyclic_sort(arr):
    """Sort array containing 1 to n"""
    i = 0
    while i < len(arr):
        correct_idx = arr[i] - 1
        if arr[i] != arr[correct_idx]:
            arr[i], arr[correct_idx] = arr[correct_idx], arr[i]
        else:
            i += 1
    return arr


def find_missing_number(arr):
    """Find missing number in 0 to n"""
    n = len(arr)
    i = 0
    while i < n:
        if arr[i] < n and arr[i] != arr[arr[i]]:
            arr[arr[i]], arr[i] = arr[i], arr[arr[i]]
        else:
            i += 1

    for i in range(n):
        if arr[i] != i:
            return i
    return n


# ============================================
# 8. BINARY SEARCH PATTERNS
# ============================================

def binary_search(arr, target):
    """Standard binary search"""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def lower_bound(arr, target):
    """First index where arr[i] >= target"""
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def upper_bound(arr, target):
    """First index where arr[i] > target"""
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


# ============================================
# 9. IN-PLACE TRICKS
# ============================================

def move_zeros(arr):
    """Move all zeros to end"""
    insert_pos = 0
    for num in arr:
        if num != 0:
            arr[insert_pos] = num
            insert_pos += 1

    while insert_pos < len(arr):
        arr[insert_pos] = 0
        insert_pos += 1

    return arr


def remove_duplicates_sorted(arr):
    """Remove duplicates from sorted array in-place"""
    if not arr:
        return 0

    insert_pos = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[insert_pos] = arr[i]
            insert_pos += 1

    return insert_pos


# ============================================
# 10. NEXT/PREVIOUS GREATER/SMALLER
# ============================================

def next_greater_element(arr):
    """Find next greater element for each"""
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])

    return result


# ============================================
# 11. INTERVAL PATTERNS
# ============================================

def merge_intervals(intervals):
    """Merge overlapping intervals"""
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return merged


# ============================================
# PATTERN CHEAT SHEET
# ============================================
"""
| Problem Type                    | Pattern                    |
|--------------------------------|----------------------------|
| Find pair with sum             | Two Pointers / Hashing     |
| Subarray with sum k            | Prefix Sum + Hash          |
| Max/Min subarray               | Kadane's / Sliding Window  |
| Find missing/duplicate         | Cyclic Sort / XOR          |
| Sort 0,1,2 / partition         | Dutch National Flag        |
| Majority element               | Moore's Voting             |
| Search in sorted               | Binary Search              |
| Overlapping intervals          | Sort + Merge               |
| Next greater element           | Monotonic Stack            |
| K largest/smallest             | Heap / QuickSelect         |
"""

if __name__ == "__main__":
    # Demo each pattern
    print("=== Two Pointers ===")
    print(f"Two sum [1,2,3,4,5], target=7: {two_sum_sorted([1,2,3,4,5], 7)}")

    print("\n=== Sliding Window ===")
    print(f"Max sum k=3 in [2,1,5,1,3,2]: {max_sum_subarray([2,1,5,1,3,2], 3)}")

    print("\n=== Kadane's ===")
    print(f"Max subarray [-2,1,-3,4,-1,2,1,-5,4]: {max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4])}")

    print("\n=== Dutch Flag ===")
    print(f"Sort colors [2,0,2,1,1,0]: {sort_colors([2,0,2,1,1,0])}")

    print("\n=== Moore's Voting ===")
    print(f"Majority in [3,2,3]: {majority_element([3,2,3])}")

    print("\n=== Binary Search ===")
    print(f"Search 5 in [1,2,3,4,5,6]: {binary_search([1,2,3,4,5,6], 5)}")
