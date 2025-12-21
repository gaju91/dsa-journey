# Index Marking Algorithm Pattern

> **Core Insight**: Use the array itself as a hash table by mapping values to indices and encoding "seen" information using the sign of elements.

---

## Table of Contents

1. [What is Index Marking?](#what-is-index-marking)
2. [When to Use This Pattern](#when-to-use-this-pattern)
3. [The Base Template](#the-base-template)
4. [How It Works](#how-it-works)
5. [Problem Variants](#problem-variants)
6. [Common Mistakes](#common-mistakes)
7. [Mental Checklist](#mental-checklist)
8. [Practice Problems](#practice-problems)

---

## What is Index Marking?

**Index Marking** is an in-place technique that uses the **sign** of array elements to encode additional information without using extra space.

**Analogy**: Think of it like a roll call checklist. Instead of keeping a separate list of who showed up, you cross out (negate) each person's name on the original roster as they arrive.

**Key Property**: We exploit the fact that:

- Array has length `n`
- Values are in range `[1..n]` (or `[0..n]`)
- Each value `x` can map to index `x-1`
- We have an unused dimension: the **sign**

---

## When to Use This Pattern

Index marking works **ONLY when ALL conditions are true**:

### ✅ Required Conditions

1. **Bounded Range**: Array values are in a known range (usually `[1..n]`)
2. **Array Length = n**: Length matches the range
3. **Presence/Absence Query**: Problem asks about duplicates, missing numbers, or existence
4. **Modification Allowed**: You can modify the input array

### ❌ When NOT to Use

- Values outside `[1..n]` range
- Array cannot be modified (immutable requirement)
- Need to preserve original values
- Values can be negative (conflicts with sign encoding)

---

## The Base Template

```python
def index_marking_template(nums: List[int]) -> List[int]:
    """
    Base template for index marking pattern

    Invariant after marking:
    - nums[i] < 0 means number (i+1) exists in array
    - nums[i] > 0 means number (i+1) is missing
    """
    n = len(nums)

    # Phase 1: Mark presence by negating
    for i in range(n):
        value = abs(nums[i])      # ALWAYS use abs() to read original value
        index = value - 1         # Map value to index (1-indexed → 0-indexed)
        nums[index] = -abs(nums[index])  # Mark as visited

    # Phase 2: Extract information from marks
    result = []
    for i in range(n):
        if nums[i] > 0:          # Positive = never visited
            result.append(i + 1)  # i+1 is missing

    return result
```

### Critical Rules

1. **Always read with `abs()`**: `value = abs(nums[i])`
2. **Map correctly**: `index = value - 1` (convert 1-indexed to 0-indexed)
3. **Mark with negation**: `nums[index] = -abs(nums[index])`

---

## How It Works

### Step-by-Step Example

**Input**: `nums = [4, 3, 2, 7, 8, 2, 3, 1]` (find duplicates)

| Step | Current Value | Index to Mark | Array State                        | Found       |
| ---- | ------------- | ------------- | ---------------------------------- | ----------- |
| 0    | 4             | 3             | `[4, 3, 2, -7, 8, 2, 3, 1]`      | -           |
| 1    | 3             | 2             | `[4, 3, -2, -7, 8, 2, 3, 1]`     | -           |
| 2    | 2 (abs)       | 1             | `[4, -3, -2, -7, 8, 2, 3, 1]`    | -           |
| 3    | 7             | 6             | `[4, -3, -2, -7, 8, 2, -3, 1]`   | -           |
| 4    | 8             | 7             | `[4, -3, -2, -7, 8, 2, -3, -1]`  | -           |
| 5    | 2 (abs)       | 1             | Already negative!                  | **2** |
| 6    | 3 (abs)       | 2             | Already negative!                  | **3** |
| 7    | 1             | 0             | `[-4, -3, -2, -7, 8, 2, -3, -1]` | -           |

**Result**: Duplicates are `[2, 3]`

### What the Sign Encodes

```
After marking:
  nums[i] < 0  →  number (i+1) appeared
  nums[i] > 0  →  number (i+1) is missing

During marking:
  nums[idx] already negative  →  duplicate detected!
```

---

## Problem Variants

### Variant 1: Find Missing Numbers (LC #448)

**Problem**: Find all numbers in `[1..n]` that don't appear.

```python
def findDisappearedNumbers(nums: List[int]) -> List[int]:
    """
    Example: [4,3,2,7,8,2,3,1] → [5,6]
    Numbers 5 and 6 are missing
    """
    # Mark present numbers
    for i in range(len(nums)):
        idx = abs(nums[i]) - 1
        nums[idx] = -abs(nums[idx])

    # Positive indices indicate missing numbers
    missing = []
    for i in range(len(nums)):
        if nums[i] > 0:
            missing.append(i + 1)whhy

    return missing
```

**Time**: O(n), **Space**: O(1)

---

### Variant 2: Find Duplicates (LC #442)

**Problem**: Find all numbers that appear twice.

```python
def findDuplicates(nums: List[int]) -> List[int]:
    """
    Example: [4,3,2,7,8,2,3,1] → [2,3]
    2 and 3 appear twice
    """
    duplicates = []

    for i in range(len(nums)):
        idx = abs(nums[i]) - 1

        # If already marked, it's a duplicate
        if nums[idx] < 0:
            duplicates.append(idx + 1)
        else:
            nums[idx] = -nums[idx]

    return duplicates
```

**Key Insight**: Second visit to already-negative index = duplicate

---

### Variant 3: Set Mismatch (LC #645)

**Problem**: One number appears twice, one is missing.

```python
def findErrorNums(nums: List[int]) -> List[int]:
    """
    Example: [1,2,2,4] → [2,3]
    2 appears twice, 3 is missing
    """
    duplicate = missing = -1

    # Find duplicate
    for i in range(len(nums)):
        idx = abs(nums[i]) - 1
        if nums[idx] < 0:
            duplicate = idx + 1
        else:
            nums[idx] = -nums[idx]

    # Find missing
    for i in range(len(nums)):
        if nums[i] > 0:
            missing = i + 1
            break

    return [duplicate, missing]
```

**Combines both techniques**: Duplicate detection + Missing detection

---

### Variant 4: First Missing Positive (LC #41) ⭐ HARDEST

**Problem**: Find smallest missing positive integer.

**Extra Challenge**: Array may contain negatives and values > n

```python
def firstMissingPositive(nums: List[int]) -> int:
    """
    Example: [3,4,-1,1] → 2
    Example: [7,8,9,11,12] → 1
    """
    n = len(nums)

    # Step 1: Clean array - replace invalid values
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1  # Safe placeholder

    # Step 2: Mark presence (only for valid range)
    for i in range(n):
        x = abs(nums[i])
        if 1 <= x <= n:
            nums[x - 1] = -abs(nums[x - 1])

    # Step 3: Find first positive (unmaked) index
    for i in range(n):
        if nums[i] > 0:
            return i + 1

    return n + 1  # All [1..n] present
```

**Extra Steps**:

1. **Cleaning**: Replace out-of-range values
2. **Bounds checking**: Only mark if `1 <= x <= n`
3. **Edge case**: Return `n+1` if all present

---

### Variant 5: Find the Single Duplicate (LC #287)

**Problem**: Array has one duplicate, find it.

```python
def findDuplicate(nums: List[int]) -> int:
    """
    Example: [1,3,4,2,2] → 2
    Only one number appears twice
    """
    for i in range(len(nums)):
        idx = abs(nums[i]) - 1
        if nums[idx] < 0:
            return idx + 1
        nums[idx] = -nums[idx]
```

**Note**: This modifies the array. LC #287 prefers Floyd's cycle detection for immutability.

---

## Common Mistakes

### ❌ Mistake 1: Forgetting `abs()`

```python
# WRONG
idx = nums[i] - 1  # If nums[i] is already negative, this fails

# CORRECT
idx = abs(nums[i]) - 1
```

### ❌ Mistake 2: Wrong Index Mapping

```python
# WRONG
idx = nums[i]  # Off by one error

# CORRECT
idx = nums[i] - 1  # Map [1..n] to [0..n-1]
```

### ❌ Mistake 3: Not Using `-abs()` When Marking

```python
# WRONG
nums[idx] = -nums[idx]  # If nums[idx] is already negative, this makes it positive!

# CORRECT
nums[idx] = -abs(nums[idx])  # Always negative after marking
```

### ❌ Mistake 4: Skipping Bounds Check (LC #41)

```python
# WRONG - crashes if x > n
idx = abs(nums[i]) - 1
nums[idx] = -nums[idx]

# CORRECT
x = abs(nums[i])
if 1 <= x <= n:
    nums[x - 1] = -abs(nums[x - 1])
```

### ❌ Mistake 5: Unnecessary Array Restoration

```python
# Unnecessary in most problems
for i in range(n):
    nums[i] = abs(nums[i])  # Only restore if problem requires it
```

---

## Mental Checklist

Before using index marking in an interview, verify:

- [ ] Values are in bounded range `[1..n]` or `[0..n]`
- [ ] Array length matches the range
- [ ] Problem asks about presence/absence/duplicates
- [ ] Modifying input is allowed
- [ ] I understand the mapping: `value x → index x-1`
- [ ] I'm using `abs()` when reading values
- [ ] I'm using `-abs()` when marking

---

## Practice Problems

### Easy (Understand the Pattern)

1. **LC #448** - Find All Numbers Disappeared in an Array
2. **LC #442** - Find All Duplicates in an Array
3. **LC #645** - Set Mismatch

### Medium (Apply with Variations)

4. **LC #41** - First Missing Positive ⭐ Must Know
5. **LC #287** - Find the Duplicate Number (index marking version)
6. **LC #268** - Missing Number (can use index marking)

### Hard (Combine with Other Techniques)

7. **LC #565** - Array Nesting
8. **LC #1995** - Count Special Quadruplets (modified approach)

---

## Complexity Analysis

| Metric                 | Value | Reason                     |
| ---------------------- | ----- | -------------------------- |
| **Time**         | O(n)  | Single or double pass      |
| **Space**        | O(1)  | No extra data structures   |
| **Modification** | Yes   | Array is modified in-place |

---

## Why This Pattern Matters

### Interview Perspective

- **Shows constraint exploitation**: You understand how to use problem constraints
- **Demonstrates space optimization**: O(1) instead of O(n) using hash maps
- **Pattern recognition**: Index marking is a category, not a memorized solution
- **Advanced thinking**: Using sign as a dimension is non-obvious

### Real-World Use

- **Embedded systems**: Limited memory
- **In-place algorithms**: When you can't allocate extra space
- **Cache-friendly**: No hash map lookups

---

## Key Takeaways

1. **Index marking is not a trick** - it's **in-place hashing**
2. **The sign bit** is your storage - use it wisely
3. **Always use `abs()`** when reading, **`-abs()`** when marking
4. **Check bounds** for problems with values outside `[1..n]`
5. **This pattern appears in ~10 LeetCode problems** - master it once, solve them all

---

## Next Steps

1. **Study**: Read `concepts/` folder for deeper understanding
2. **Practice**: Solve problems in `problems/` folder
3. **Review**: Come back to this README before interviews

---

**Last Updated**: 2025-12-13
**Pattern Difficulty**: Medium
**Interview Frequency**: High (FAANG loves this)
