# Two Pointers Pattern Variants

There are **4 main variants** of the two pointers technique. Each solves a different class of problems.

---

## Variant 1: Opposite Direction (Converging Pointers)

### When to Use

- Array is **sorted**
- Looking for **pairs** with specific property
- Problems involving **palindromes**
- **Container** problems (max area, water trapping)

### Movement Pattern

```
Start:  [... ... ... ... ... ... ...]
         ↑                       ↑
         L                       R

Step:   [... ... ... ... ... ...]
             ↑               ↑
             L               R

End:    [... ... ... ... ...]
                 ↑   ↑
                 L=R
```

Pointers **converge** from opposite ends.

### Template

```python
def opposite_direction_template(arr):
    left = 0
    right = len(arr) - 1

    while left < right:  # Stop when pointers meet
        # Process current pair
        result = process(arr[left], arr[right])

        # Decision: which pointer to move?
        if condition_met:
            return result
        elif need_larger_value:
            left += 1  # Move left forward
        else:
            right -= 1  # Move right backward

    return default_result
```

### Example Problems

**1. Two Sum (Sorted Array)**
```python
def two_sum(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum

    return [-1, -1]
```

**2. Valid Palindrome**
```python
def is_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
```

**3. Container With Most Water**
```python
def max_area(heights):
    left, right = 0, len(heights) - 1
    max_water = 0

    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        max_water = max(max_water, width * height)

        # Move pointer with smaller height
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_water
```

### Key Characteristics

- **Time**: O(n)
- **Space**: O(1)
- **Boundary**: `left < right` (strict inequality)
- **When stops**: Pointers meet or cross

---

## Variant 2: Same Direction (Fast and Slow Pointers)

### When to Use

- **Remove duplicates** in-place
- **Partition** array
- **In-place modifications**
- **Separate elements** by condition

### Movement Pattern

```
Both start at beginning, move at different rates

Start:  [... ... ... ... ... ... ...]
         ↑ ↑
         S F

Step:   [... ... ... ... ... ...]
         ↑       ↑
         S       F

End:    [... ... ... ... ...]
                 ↑           ↑
                 S           F
```

Slow pointer marks **write position**, fast pointer **reads**.

### Template

```python
def same_direction_template(arr):
    slow = 0  # Write position

    for fast in range(len(arr)):
        # Condition to decide if we keep element
        if should_keep(arr[fast]):
            arr[slow] = arr[fast]
            slow += 1

    return slow  # New length or write position
```

### Example Problems

**1. Remove Duplicates**
```python
def remove_duplicates(nums):
    """
    [1, 1, 2, 2, 3, 3, 4]
     ↑ ↑
     S F

    Slow writes unique, Fast reads all
    """
    if not nums:
        return 0

    slow = 0  # Next write position

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1  # New length
```

**2. Move Zeroes**
```python
def move_zeroes(nums):
    """
    Move all zeros to end, maintain relative order

    [0, 1, 0, 3, 12]
     ↑ ↑
     S F

    Slow marks position for non-zeros
    """
    slow = 0  # Position for next non-zero

    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
```

**3. Partition Array (Dutch National Flag)**
```python
def sort_colors(nums):
    """
    Sort array of 0s, 1s, and 2s

    Three pointers: low, mid, high
    """
    low = mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
```

### Key Characteristics

- **Time**: O(n)
- **Space**: O(1)
- **Pattern**: `slow` writes, `fast` reads
- **Usage**: In-place array modifications

---

## Variant 3: Sliding Window

### When to Use

- **Subarray** problems
- **Substring** with constraints
- **Maximum/minimum** in window
- **K-sized** window problems

### Movement Pattern

```
Window expands and contracts

Expand:
[... ... ... ... ...]
 ↑   ↑
 L   R →

Contract:
[... ... ... ... ...]
     ↑       ↑
   L →       R

Window size = R - L + 1
```

### Template (Variable Window)

```python
def sliding_window_variable(arr, constraint):
    left = 0
    window_state = initial_state
    result = 0

    for right in range(len(arr)):
        # Expand window: include arr[right]
        window_state = update_state(window_state, arr[right])

        # Contract window while violates constraint
        while violates_constraint(window_state, constraint):
            window_state = remove_from_state(window_state, arr[left])
            left += 1

        # Update result with current valid window
        result = max(result, right - left + 1)

    return result
```

### Template (Fixed Window)

```python
def sliding_window_fixed(arr, k):
    window_sum = sum(arr[:k])  # Initial window
    result = window_sum

    for right in range(k, len(arr)):
        # Slide window: add right, remove left
        window_sum += arr[right]
        window_sum -= arr[right - k]
        result = max(result, window_sum)

    return result
```

### Example Problems

**1. Longest Substring Without Repeating Characters**
```python
def length_of_longest_substring(s):
    """
    Variable window

    "abcabcbb"
     ↑ ↑
     L R
    """
    left = 0
    char_set = set()
    max_length = 0

    for right in range(len(s)):
        # Expand: add s[right]
        while s[right] in char_set:
            # Contract: remove s[left]
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length
```

**2. Maximum Sum Subarray of Size K**
```python
def max_sum_subarray(arr, k):
    """
    Fixed window

    [1, 3, 2, 5, 1, 1, 2], k=3
     ↑     ↑
     L     R (R - L + 1 = 3)
    """
    if len(arr) < k:
        return 0

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for right in range(k, len(arr)):
        # Slide: add new, remove old
        window_sum += arr[right] - arr[right - k]
        max_sum = max(max_sum, window_sum)

    return max_sum
```

**3. Minimum Window Substring**
```python
def min_window(s, t):
    """
    Find smallest substring of s containing all chars of t
    Variable window with hash map
    """
    from collections import Counter

    if not s or not t:
        return ""

    need = Counter(t)
    have = {}
    required = len(need)
    formed = 0

    left = 0
    min_len = float('inf')
    min_window = ""

    for right in range(len(s)):
        char = s[right]
        have[char] = have.get(char, 0) + 1

        if char in need and have[char] == need[char]:
            formed += 1

        # Contract window
        while formed == required:
            # Update result
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = s[left:right + 1]

            # Remove from left
            have[s[left]] -= 1
            if s[left] in need and have[s[left]] < need[s[left]]:
                formed -= 1
            left += 1

    return min_window
```

### Key Characteristics

- **Time**: O(n) - each element visited at most twice
- **Space**: O(1) to O(k) depending on window state
- **Two types**: Fixed size, Variable size
- **Pattern**: Expand right, contract left

---

## Variant 4: Multiple Sequences

### When to Use

- **Merge** two sorted arrays
- **Compare** two sequences
- **Find common** elements
- **Intersect/Union** operations

### Movement Pattern

```
One pointer per sequence

Seq1: [1, 3, 5, 7]
       ↑
       i

Seq2: [2, 3, 4, 6]
       ↑
       j

Move based on comparison
```

### Template

```python
def two_sequences_template(seq1, seq2):
    i, j = 0, 0
    result = []

    while i < len(seq1) and j < len(seq2):
        if seq1[i] < seq2[j]:
            # Process seq1[i]
            result.append(seq1[i])
            i += 1
        elif seq1[i] > seq2[j]:
            # Process seq2[j]
            result.append(seq2[j])
            j += 1
        else:  # Equal
            # Process both
            result.append(seq1[i])
            i += 1
            j += 1

    # Append remaining elements
    result.extend(seq1[i:])
    result.extend(seq2[j:])

    return result
```

### Example Problems

**1. Merge Two Sorted Arrays**
```python
def merge(nums1, m, nums2, n):
    """
    Merge nums2 into nums1

    Trick: Start from end to avoid overwriting
    """
    i, j = m - 1, n - 1
    k = m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
```

**2. Intersection of Two Arrays**
```python
def intersection(nums1, nums2):
    """
    Return common elements

    Both arrays must be sorted
    """
    i, j = 0, 0
    result = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            result.append(nums1[i])
            i += 1
            j += 1

    return result
```

### Key Characteristics

- **Time**: O(m + n)
- **Space**: O(1) or O(min(m,n)) for result
- **Pattern**: Compare and advance
- **Usage**: Merge, intersect, union

---

## Choosing the Right Variant

### Decision Tree

```
What's the problem?
│
├─ Find pair with property?
│  ├─ Sorted? → Opposite Direction
│  └─ Unsorted? → Hash Map (not two pointers)
│
├─ Modify array in-place?
│  └─ Same Direction (Fast & Slow)
│
├─ Subarray/substring?
│  └─ Sliding Window
│
└─ Two sequences?
   └─ Multiple Sequences
```

---

## Comparison Table

| Variant | Start Position | Movement | Stop Condition | Use Case |
|---------|---------------|----------|----------------|----------|
| **Opposite** | Both ends | Toward each other | Meet/cross | Pairs, palindromes |
| **Same Direction** | Same start | Different speeds | Fast reaches end | In-place modify |
| **Sliding Window** | Left=0, Right varies | Right expands, Left contracts | Right reaches end | Subarrays |
| **Multiple Sequences** | Start of each | Based on comparison | One exhausted | Merge, intersect |

---

## Common Patterns Across Variants

### 1. All use O(n) or O(m+n) time

Each element visited at most twice (in sliding window).

### 2. All use O(1) extra space

(Excluding space for result)

### 3. All require linear structure

Arrays, strings, linked lists.

### 4. All have clear termination

Loop conditions are well-defined.

---

## Summary

- **Opposite Direction**: Sorted pairs, palindromes
- **Same Direction**: In-place modifications
- **Sliding Window**: Subarrays with constraints
- **Multiple Sequences**: Merge operations

**Pro Tip**: In interviews, explicitly state which variant you're using and why.

---

**Next**: Read `03_when_to_use.md` for pattern recognition guide
