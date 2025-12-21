# Core Principle of Two Pointers

## The Fundamental Problem

**Question**: How can we find a pair of elements in an array without checking every possible pair?

**Naive Answer**: Nested loops - O(n²) time

```python
# Brute force: Check all pairs
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            return [i, j]
```

**Problem**: n² comparisons for array of size n

---

## The Breakthrough: Exploiting Order

### Key Insight

**If the array is sorted**, we can make intelligent decisions about which elements to consider next.

```
Sorted array: [1, 2, 3, 4, 5, 6, 7, 8, 9]

Question: Find two numbers that sum to 10

Brute force would check:
(1,2), (1,3), (1,4), ..., (1,9)  → 8 comparisons
(2,3), (2,4), ..., (2,9)         → 7 comparisons
...
Total: 8+7+6+5+4+3+2+1 = 36 comparisons

Two pointers:
Start: (1, 9) → sum = 10 ✓ Found!
Total: 1 comparison
```

---

## The Core Principle

**Use two indices and a decision rule to eliminate half the search space at each step.**

### The Magic Formula

```
For sorted array and target sum:

current_sum = arr[left] + arr[right]

if current_sum < target:
    → All pairs with arr[left] will be < target
    → Skip arr[left], move left pointer right
    → left += 1

if current_sum > target:
    → All pairs with arr[right] will be > target
    → Skip arr[right], move right pointer left
    → right -= 1

if current_sum == target:
    → Found!
```

---

## Visual Proof: Why It Works

### Example: Find pair that sums to 11

```
Array: [1, 2, 4, 6, 8, 9, 10, 12]
Target: 11

Step 1: Start at both ends
[1, 2, 4, 6, 8, 9, 10, 12]
 ↑                      ↑
 L(1)                  R(12)

Sum = 1 + 12 = 13 > 11
Decision: Too large, need smaller sum
Action: R-- (eliminate 12)
Proof: ANY pair with 12 will be > 11 (since all values > 0)
      1+12=13, 2+12=14, 4+12=16, ...all > 11 ✓

Step 2:
[1, 2, 4, 6, 8, 9, 10, 12]
 ↑                  ↑
 L(1)              R(10)

Sum = 1 + 10 = 11 ✓ Found!
```

---

## Mathematical Justification

### Why We Don't Miss the Answer

**Claim**: Two pointers finds the pair if it exists.

**Proof** (by contradiction):

Assume the answer is `(arr[i], arr[j])` where `i < j`.

**Case 1**: Our left pointer skips past `i` (moves from `k` to `k+1` where `k < i`)

This happens when `arr[k] + arr[right] < target`.

But we know `arr[i] + arr[j] = target`.

Since `arr[k] < arr[i]` (sorted array) and we had `arr[k] + arr[right] < target`:
- If `right > j`: Then `arr[right] ≥ arr[j]`
  - So `arr[k] + arr[right] ≥ arr[k] + arr[j] > arr[i] + arr[j] = target`
  - Contradiction with `arr[k] + arr[right] < target`

- If `right = j`: Then we would have found the answer
  - If `arr[k] + arr[j] < target` and `arr[i] + arr[j] = target`
  - Then `arr[k] < arr[i]` ✓ Consistent with sorted array
  - We correctly skipped `k` because it's too small

- If `right < j`: Similar analysis

**Conclusion**: We never incorrectly skip the answer.

---

## The Elimination Principle

At each step, we **eliminate** either:
1. All pairs with `arr[left]` (move left++)
2. All pairs with `arr[right]` (move right--)

This is why we achieve O(n) instead of O(n²):

```
Comparisons = n (worst case: traverse entire array once)

vs.

Brute force = n×(n-1)/2 ≈ n²/2
```

---

## Why Sorting Is Often Required

### Unsorted Array Example

```
Array: [3, 5, 1, 8, 2, 9]
Target: 10

If we try two pointers:
Start: [3, 5, 1, 8, 2, 9]
        ↑              ↑
        L(3)          R(9)

Sum = 3 + 9 = 12 > 10
Move right left: right--

[3, 5, 1, 8, 2, 9]
 ↑           ↑
 L(3)       R(2)

Sum = 3 + 2 = 5 < 10
Move left right: left++

[3, 5, 1, 8, 2, 9]
    ↑        ↑
   L(5)     R(2)

Sum = 5 + 2 = 7 < 10
Move left right: left++

... We might MISS the answer (1, 9) = 10!
```

**Why it fails**: Without sorting, we can't make the elimination guarantee.

---

## The Three Requirements

For two pointers to work, you need:

1. **Linear structure** (array, linked list, string)
2. **Decision rule** (how to move pointers)
3. **Monotonic property** (sorted, or some ordering that guides movement)

---

## Beyond Sum Problems

The principle extends to:

### 1. Palindrome Check

```python
# Two pointers from ends
s = "racecar"
[r, a, c, e, c, a, r]
 ↑           ↑
 L           R

Compare and move inward
```

**Decision rule**: If mismatch, not palindrome. Otherwise move both inward.

### 2. Container With Most Water

```python
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]

Area = width × min_height
Width decreases as pointers converge

Decision rule: Move pointer with smaller height (bottleneck)
```

### 3. Remove Duplicates

```python
[1, 1, 2, 2, 3, 3]
 ↑ ↑
 S F

Slow = write position
Fast = read position

Decision rule: If arr[fast] != arr[slow], write and move slow
```

---

## Space-Time Tradeoff

### Two Pointers Approach

```
Time: O(n)
Space: O(1)

Requirement: Sorted array (or can sort)
```

### Hash Map Approach

```
Time: O(n)
Space: O(n)

Advantage: Works on unsorted array
```

**When to use which**:
- Array already sorted → Two pointers
- Cannot modify array → Hash map
- Multiple queries → Sort once, use two pointers
- One-time query on small array → Hash map

---

## The Pointer Movement Decision Tree

```
                   Check current state
                           |
        ┌──────────────────┼──────────────────┐
        ↓                  ↓                  ↓
    Too Small          Perfect!          Too Large
        |                  |                  |
   Increase sum      Return result      Decrease sum
        |                                     |
   left++                                right--
        |                                     |
   Eliminate left                    Eliminate right
```

---

## Invariant Maintenance

**Loop Invariant**: At each iteration, we've eliminated all pairs outside `[left, right]` range.

**Initialization**: `left=0, right=n-1` → No pairs eliminated
**Maintenance**: Each step eliminates pairs correctly
**Termination**: `left >= right` → All pairs checked

This is why the algorithm is correct and complete.

---

## Complexity Deep Dive

### Why O(n) and not O(n²)?

Each pointer moves at most `n` times:
- Left pointer: 0 → n (max n moves)
- Right pointer: n → 0 (max n moves)
- Total moves: 2n → O(n)

Each move is O(1) operation.

**Total**: O(n)

### Why O(1) space?

Only variables: `left`, `right`, `current_sum`, `result`
Fixed number of variables regardless of n.

**Space**: O(1)

---

## Analogies

### 1. The Meeting Analogy

Two people walking in a hallway:
- Start at opposite ends
- Walk toward each other
- Stop when they meet
- Total distance covered: length of hallway

### 2. The Vise Analogy

A vise closing on a workpiece:
- Jaws start wide open
- Close from both sides
- Stop when they touch
- Never reopen (monotonic movement)

### 3. The Binary Search Connection

Two pointers is like binary search on pairs:
- Instead of searching for one element
- We're searching for a pair
- Each step eliminates half the remaining candidates

---

## Common Variations

### 1. Three Pointers (3Sum)

```python
# Fix one, use two pointers on the rest
for i in range(n):
    left = i + 1
    right = n - 1
    # Apply two pointers on [left, right]
```

### 2. Multiple Sequences

```python
# One pointer per sequence
i, j = 0, 0
while i < len(arr1) and j < len(arr2):
    # Process based on comparison
```

### 3. Fast and Slow (Same Direction)

```python
# Both move forward, different speeds
slow = 0
for fast in range(n):
    # Condition-based writing
```

---

## Summary

**Core Principle**: Use two indices and an intelligent decision rule to traverse the array in O(n) time instead of O(n²).

**Key Requirements**:
1. Linear structure
2. Decision rule
3. Monotonic property (usually sorted)

**Why It Works**: Each pointer movement eliminates a portion of the search space, guaranteeing we don't miss the answer while achieving linear time.

---

**Next**: Read `02_pattern_variants.md` to understand all the different two-pointer patterns
