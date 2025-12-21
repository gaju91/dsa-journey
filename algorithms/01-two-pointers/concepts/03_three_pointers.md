# Three Pointers Pattern (Dutch National Flag)

While this folder is called "Two Pointers", one important variant uses **THREE** pointers for 3-way partitioning problems.

---

## When to Use Three Pointers

Use three pointers when you need to:
- **Partition into 3 groups** (low, mid, high values)
- **Sort 3 distinct values** (e.g., 0, 1, 2)
- **Segregate into 3 categories**

**Classic Problem**: Sort Colors (LC #75) - Dutch National Flag

---

## The Three-Pointer Setup

```
Array divided into 4 regions:

[0, 0, ..., 0, 1, 1, ..., 1, ?, ?, ..., ?, 2, 2, ..., 2]
 ↑             ↑             ↑             ↑
 0            low           mid           high    n-1

Regions:
1. [0, low): All 0s (processed, in place)
2. [low, mid): All 1s (processed, in place)
3. [mid, high]: Unknown (being processed)
4. (high, n-1]: All 2s (processed, in place)
```

---

## The Algorithm

```python
def sort_colors(nums):
    low = 0       # Boundary for 0s
    mid = 0       # Current element
    high = len(nums) - 1  # Boundary for 2s

    while mid <= high:
        if nums[mid] == 0:
            # Move to low region
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1  # Safe to advance: nums[low] was 1

        elif nums[mid] == 1:
            # Already in correct position
            mid += 1

        else:  # nums[mid] == 2
            # Move to high region
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
            # DON'T advance mid! Need to check swapped element
```

---

## Critical Asymmetry

**Why does mid advance with 0 but not with 2?**

### When swapping with low (nums[mid] == 0):
```
[0, 0, 1, 1, ?, ?, 2, 2]
       ↑     ↑
      low   mid

- nums[low] is in [low, mid) region
- This region contains ONLY 1s (by invariant)
- So nums[low] == 1 (known!)
- After swap: nums[mid] = 1 (correct position)
- ✓ Safe to advance mid
```

### When swapping with high (nums[mid] == 2):
```
[0, 0, 1, 1, ?, ?, 2, 2]
             ↑  ↑
            mid high

- nums[high] is in unknown region
- It could be 0, 1, or 2 (unknown!)
- After swap: nums[mid] = ??? (need to check)
- ✗ NOT safe to advance mid
- Must examine in next iteration
```

---

## Example Walkthrough

Input: `[2, 0, 2, 1, 1, 0]`

```
Step 1: [2, 0, 2, 1, 1, 0]  low=0, mid=0, high=5
        nums[mid]=2 → swap with high
        [0, 0, 2, 1, 1, 2]  low=0, mid=0, high=4

Step 2: [0, 0, 2, 1, 1, 2]  low=0, mid=0, high=4
        nums[mid]=0 → swap with low
        [0, 0, 2, 1, 1, 2]  low=1, mid=1, high=4

Step 3: [0, 0, 2, 1, 1, 2]  low=1, mid=1, high=4
        nums[mid]=0 → swap with low
        [0, 0, 2, 1, 1, 2]  low=2, mid=2, high=4

Step 4: [0, 0, 2, 1, 1, 2]  low=2, mid=2, high=4
        nums[mid]=2 → swap with high
        [0, 0, 1, 1, 2, 2]  low=2, mid=2, high=3

Step 5: [0, 0, 1, 1, 2, 2]  low=2, mid=2, high=3
        nums[mid]=1 → mid++
        [0, 0, 1, 1, 2, 2]  low=2, mid=3, high=3

Step 6: [0, 0, 1, 1, 2, 2]  low=2, mid=3, high=3
        nums[mid]=1 → mid++
        [0, 0, 1, 1, 2, 2]  low=2, mid=4, high=3

mid > high → DONE!
Final: [0, 0, 1, 1, 2, 2] ✓
```

---

## Invariant Proof

**Loop Invariant**: At start of each iteration:
- All elements in [0, low) are 0
- All elements in [low, mid) are 1
- All elements in (high, n-1] are 2
- Elements in [mid, high] are unknown

**Initialization**:
- low = 0, mid = 0, high = n-1
- [0, 0) = empty → no 0s ✓
- [0, 0) = empty → no 1s ✓
- (n-1, n-1] = empty → no 2s ✓
- [0, n-1] = entire array → all unknown ✓

**Maintenance**: Each operation preserves invariant

**Termination**: When mid > high
- Unknown region [mid, high] is empty
- All elements partitioned ✓

---

## Comparison with Quicksort Partition

The Dutch National Flag algorithm is similar to 3-way partitioning in Quicksort:

```
Quicksort 3-way partition:
- Elements < pivot
- Elements == pivot
- Elements > pivot

Dutch National Flag:
- Elements == 0
- Elements == 1
- Elements == 2
```

Both use three pointers to maintain regions!

---

## Common Mistakes

### ❌ Mistake 1: Advancing mid with 2
```python
if nums[mid] == 2:
    nums[mid], nums[high] = nums[high], nums[mid]
    high -= 1
    mid += 1  # WRONG!
```

### ❌ Mistake 2: Using mid < high
```python
while mid < high:  # WRONG! Misses element at mid==high
```
**Fix**: `while mid <= high`

### ❌ Mistake 3: Swapping 0 with high
```python
if nums[mid] == 0:
    nums[mid], nums[high] = nums[high], nums[mid]  # WRONG!
```
**Fix**: Swap with low, not high

### ❌ Mistake 4: Not advancing low with 0
```python
if nums[mid] == 0:
    nums[mid], nums[low] = nums[low], nums[mid]
    mid += 1  # Forgot low += 1!
```

---

## Related Problems

**Three Pointers / Partitioning**:
- LC #75: Sort Colors ⭐ (THE classic problem)
- LC #283: Move Zeroes (2-way partition)
- Quicksort 3-way partition
- LC #partition-array: Partition Array

**When to use**:
- ✅ Exactly 3 categories/values
- ✅ Need one-pass sorting
- ✅ O(1) space required
- ✅ In-place modification allowed

**When NOT to use**:
- ❌ More than 3 categories (use counting sort)
- ❌ Need stable sort (this is not stable)
- ❌ Values are not distinct/small range

---

## Key Takeaways

1. **Three pointers** for **three categories**
2. Maintain **four regions**: low, mid, unknown, high
3. **Asymmetric movement**: mid advances with 0, not with 2
4. **Invariant maintenance** is key to correctness
5. **One pass O(n)**, **constant space O(1)**

**Named after**: Edsger Dijkstra, Dutch computer scientist who invented it to sort the Dutch flag's three horizontal stripes (red, white, blue).

---

**The Pattern**: When you see "sort 3 values in one pass", think **Dutch National Flag**!
