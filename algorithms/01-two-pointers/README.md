# Two Pointers Algorithm Pattern

> **Core Insight**: Use two indices moving through an array (or linked list) to solve problems in O(n) time that would otherwise require O(n²) nested loops.

---

## Table of Contents

1. [What is Two Pointers?](#what-is-two-pointers)
2. [When to Use This Pattern](#when-to-use-this-pattern)
3. [Pattern Variants](#pattern-variants)
4. [Base Templates](#base-templates)
5. [Common Problem Types](#common-problem-types)
6. [Mental Checklist](#mental-checklist)
7. [Practice Problems](#practice-problems)

---

## What is Two Pointers?

**Two Pointers** is a technique where you use two indices (pointers) to traverse a data structure, typically moving them towards each other or in the same direction.

**Analogy**: Think of two people searching for each other in a hallway:
- **Opposite Ends**: They start at opposite ends and walk towards the middle
- **Same Direction**: One person walks fast, one walks slow (like a race)
- **Sliding Window**: They walk together maintaining a fixed distance

**Key Property**: Eliminates nested loops by intelligently moving pointers based on problem logic.

---

## When to Use This Pattern

### ✅ Strong Indicators

1. **Sorted array** (or can be sorted)
2. **Pair/triplet** problems (find two/three elements)
3. **Palindrome** checking
4. **Removing duplicates** in-place
5. **Partition** problems
6. **Subarray/substring** with conditions

### ✅ Required Conditions

- Array or sequence of elements
- Need to find pairs, triplets, or subarrays
- Can afford O(n) time with O(1) space
- Problem has some **monotonic property** (sorted, or can decide to move which pointer)

### ❌ When NOT to Use

- Unsorted array and sorting would break the solution
- Need to find all subarrays (usually DP)
- Random access patterns (no sequential traversal)
- Problems requiring backtracking

---

## Pattern Variants

### Variant 1: Opposite Direction (Most Common)

**Use When**: Sorted array, finding pairs with a target sum

```
Left pointer starts at beginning →
Right pointer starts at end ←

[1, 2, 3, 4, 5, 6, 7]
 ↑                 ↑
 L                 R

Move based on comparison:
- If sum < target: L++
- If sum > target: R--
- If sum == target: Found!
```

**Template**:
```python
def two_pointers_opposite(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current = arr[left] + arr[right]

        if current == target:
            return [left, right]
        elif current < target:
            left += 1
        else:
            right -= 1

    return [-1, -1]
```

**Time**: O(n), **Space**: O(1)

---

### Variant 2: Same Direction (Fast & Slow)

**Use When**: Remove duplicates, partition array, cycle detection

```
Both start at beginning, move at different speeds

[1, 1, 2, 2, 3, 3, 4]
 ↑ ↑
 S F

Slow writes, Fast reads
```

**Template**:
```python
def two_pointers_same_direction(arr):
    slow = 0  # Write position

    for fast in range(len(arr)):
        # Condition to write
        if should_keep(arr[fast]):
            arr[slow] = arr[fast]
            slow += 1

    return slow  # New length
```

**Time**: O(n), **Space**: O(1)

---

### Variant 3: Sliding Window (Fixed/Variable Size)

**Use When**: Subarray problems with constraints

```
Window expands/contracts based on condition

[1, 3, 2, 5, 1, 1, 2]
 ↑     ↑
 L     R

Expand R to grow window
Contract L to shrink window
```

**Template**:
```python
def sliding_window(arr, k):
    left = 0
    window_sum = 0
    result = 0

    for right in range(len(arr)):
        # Expand window
        window_sum += arr[right]

        # Shrink window if needed
        while window_sum > k:
            window_sum -= arr[left]
            left += 1

        # Update result
        result = max(result, right - left + 1)

    return result
```

**Time**: O(n), **Space**: O(1)

---

### Variant 4: Two Sequences (Merge)

**Use When**: Merging sorted arrays, comparing sequences

```
One pointer per sequence

arr1: [1, 3, 5]
       ↑
      i

arr2: [2, 4, 6]
       ↑
      j
```

**Template**:
```python
def merge_two_arrays(arr1, arr2):
    i = j = 0
    result = []

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
```

**Time**: O(n+m), **Space**: O(n+m)

---

## Common Problem Types

### Type 1: Pair with Target Sum

**Problem**: Find two numbers that sum to target (sorted array)

```python
def two_sum_sorted(nums, target):
    """
    LC #167: Two Sum II - Input Array Is Sorted

    Analogy: "Two people walking towards each other"
    """
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum

    return [-1, -1]
```

**Why it works**: If sum is too small, we must increase (move left). If too large, we must decrease (move right).

---

### Type 2: Remove Duplicates

**Problem**: Remove duplicates from sorted array in-place

```python
def remove_duplicates(nums):
    """
    LC #26: Remove Duplicates from Sorted Array

    Analogy: "Slow writes unique values, Fast reads all values"
    """
    if not nums:
        return 0

    slow = 0  # Position for next unique element

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1  # New length
```

**Why it works**: Slow pointer marks position for unique elements, fast pointer scans ahead.

---

### Type 3: Container Problems

**Problem**: Find container with most water

```python
def max_area(heights):
    """
    LC #11: Container With Most Water

    Analogy: "Maximize rectangle between two vertical lines"
    """
    left, right = 0, len(heights) - 1
    max_water = 0

    while left < right:
        # Area = width × min_height
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

**Why move smaller height**: The smaller height limits area, so we try to find a taller one.

---

### Type 4: Palindrome Checking

**Problem**: Check if string is palindrome

```python
def is_palindrome(s):
    """
    LC #125: Valid Palindrome

    Analogy: "Mirror test - compare from both ends"
    """
    left, right = 0, len(s) - 1

    while left < right:
        # Skip non-alphanumeric
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
```

---

### Type 5: Three Sum (Extended Pattern)

**Problem**: Find three numbers that sum to zero

```python
def three_sum(nums):
    """
    LC #15: 3Sum

    Extension: Fix one number, use two pointers for remaining two
    """
    nums.sort()  # MUST sort first
    result = []

    for i in range(len(nums) - 2):
        # Skip duplicates for first number
        if i > 0 and nums[i] == nums[i-1]:
            continue

        # Two pointers for remaining numbers
        left, right = i + 1, len(nums) - 1
        target = -nums[i]

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1

                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return result
```

**Pattern**: Fix one element, apply two pointers on remaining

---

## Decision Tree: Which Variant?

```
Is array sorted?
│
├─ Yes ──────────────────┐
│                        │
│  Looking for pair?     │
│  ├─ Yes → Opposite Direction
│  └─ No → Check other conditions
│
└─ No ───────────────────┐
                         │
   Can modify in-place?  │
   ├─ Yes → Same Direction (partition/remove)
   └─ No → Consider sorting first or use hash map
```

---

## Common Mistakes

### ❌ Mistake 1: Not Handling Duplicates

```python
# WRONG - doesn't skip duplicates in Three Sum
while left < right:
    if nums[left] + nums[right] == target:
        result.append([nums[i], nums[left], nums[right]])
        left += 1  # BUG: Might add duplicate triplets
        right -= 1
```

**Fix**: Skip duplicate values after finding a match.

### ❌ Mistake 2: Wrong Boundary Conditions

```python
# WRONG - should be left < right, not <=
while left <= right:  # BUG: Allows same element twice
    if nums[left] + nums[right] == target:
        return [left, right]
```

**Fix**: Use `left < right` for pair problems.

### ❌ Mistake 3: Forgetting to Sort

```python
# WRONG - two pointers on unsorted array
def two_sum(nums, target):
    left, right = 0, len(nums) - 1
    # BUG: Doesn't work on unsorted array!
```

**Fix**: Sort first, or use hash map instead.

### ❌ Mistake 4: Off-by-One Errors

```python
# WRONG - returns 0-indexed but problem wants 1-indexed
return [left, right]  # BUG for LC #167

# CORRECT
return [left + 1, right + 1]
```

---

## Mental Checklist

Before using two pointers in an interview, verify:

- [ ] Is the array sorted (or can I sort it)?
- [ ] Am I looking for pairs, triplets, or subarrays?
- [ ] Do I need to modify the array in-place?
- [ ] Is there a monotonic property to guide pointer movement?
- [ ] Which variant: opposite, same direction, or sliding window?
- [ ] Do I need to handle duplicates?
- [ ] Are indices 0-indexed or 1-indexed?

---

## Practice Problems

### Easy (Master the Basics)
1. **LC #167** - Two Sum II (sorted array) ⭐ Start Here
2. **LC #26** - Remove Duplicates from Sorted Array
3. **LC #27** - Remove Element
4. **LC #125** - Valid Palindrome
5. **LC #283** - Move Zeroes
6. **LC #344** - Reverse String

### Medium (Apply Variants)
7. **LC #15** - 3Sum ⭐ Important
8. **LC #11** - Container With Most Water
9. **LC #16** - 3Sum Closest
10. **LC #75** - Sort Colors (Dutch National Flag)
11. **LC #80** - Remove Duplicates II
12. **LC #713** - Subarray Product Less Than K

### Hard (Combine Techniques)
13. **LC #42** - Trapping Rain Water ⭐ Classic
14. **LC #76** - Minimum Window Substring
15. **LC #159** - Longest Substring with At Most Two Distinct Characters

---

## Complexity Analysis

| Variant | Time | Space | Notes |
|---------|------|-------|-------|
| Opposite Direction | O(n) | O(1) | Single pass |
| Same Direction | O(n) | O(1) | Single pass |
| Sliding Window | O(n) | O(1) | Amortized - each element visited max twice |
| Three Sum | O(n²) | O(1) | Two pointers inside loop |

---

## Pattern Combinations

### Two Pointers + Binary Search
Problem: Find K closest elements

### Two Pointers + Hash Map
Problem: Two Sum variants on unsorted arrays

### Two Pointers + Sorting
Problem: 3Sum, 4Sum family

### Two Pointers + Greedy
Problem: Container with most water

---

## Why This Pattern Matters

### Interview Perspective

- **Reduces complexity**: O(n²) → O(n)
- **Space efficient**: Usually O(1) extra space
- **Shows optimization skill**: From brute force to optimal
- **Common in FAANG**: Appears in 40% of array problems

### Real-World Use

- **Merge algorithms**: Mergesort, merging logs
- **Database joins**: Merge join on sorted tables
- **String processing**: Palindrome checks, compression
- **Memory management**: Partition algorithms

---

## Key Takeaways

1. **Two pointers eliminates nested loops** when there's a decision rule for pointer movement
2. **Sorted arrays** are prime candidates for opposite-direction pointers
3. **In-place modifications** often use same-direction pointers
4. **Always consider** whether sorting first would help
5. **Handle duplicates** explicitly in problems that require unique results

---

## Comparison with Other Patterns

| Pattern | Time | Space | Use Case |
|---------|------|-------|----------|
| **Two Pointers** | O(n) | O(1) | Sorted arrays, pairs |
| Hash Map | O(n) | O(n) | Unsorted, any sum |
| Sliding Window | O(n) | O(1) | Subarrays with constraints |
| Binary Search | O(log n) | O(1) | Search in sorted |

---

## Next Steps

1. **Study**: Read `concepts/` folder for deeper understanding
2. **Practice**: Solve problems in `problems/` folder
3. **Master**: Complete all Easy problems first
4. **Extend**: Try Medium and Hard problems

---

**Last Updated**: 2025-12-13
**Pattern Difficulty**: Easy to Medium
**Interview Frequency**: Very High (40% of array problems)
**Must-Know**: Yes - Top 3 most important patterns
