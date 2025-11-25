# Arrays

## Overview

An array is a collection of elements stored at contiguous memory locations. It's the most fundamental data structure and forms the basis for many other data structures.

---

## Python Concepts (Detailed Files)

| # | Topic | File | Status |
|---|-------|------|--------|
| 1 | List Basics | `concepts/01_list_basics.py` | ✅ |
| 2 | Indexing & Slicing | `concepts/02_indexing_slicing.py` | ✅ |
| 3 | List Methods | `concepts/03_list_methods.py` | ✅ |
| 4 | List Comprehensions | `concepts/04_list_comprehensions.py` | ✅ |
| 5 | Iterating Techniques | `concepts/05_iterating_techniques.py` | ✅ |
| 6 | 2D Arrays | `concepts/06_2d_arrays.py` | ✅ |
| 7 | Built-in Functions | `concepts/07_builtin_functions.py` | ✅ |
| 8 | Copying & References | `concepts/08_copying_references.py` | ✅ |
| 9 | Unpacking & Packing | `concepts/09_unpacking_packing.py` | ✅ |
| 10 | Array Module & NumPy | `concepts/10_array_module.py` | ✅ |
| 11 | Collections Module | `concepts/11_collections_module.py` | ✅ |
| 12 | Common Patterns | `concepts/12_common_patterns.py` | ✅ |

---

## Concepts Summary

### 1. What is an Array?
- Collection of elements of the **same data type**
- Stored in **contiguous memory** locations
- Elements accessed using **index** (0-based in Python)
- **Fixed size** in most languages (dynamic in Python - lists)

### 2. Array Declaration in Python
```python
# Using list (dynamic array)
arr = [1, 2, 3, 4, 5]

# Empty array
arr = []

# Array with default values
arr = [0] * 10  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 2D Array
matrix = [[0] * cols for _ in range(rows)]

# Using array module (typed arrays)
from array import array
arr = array('i', [1, 2, 3, 4, 5])  # 'i' = signed int
```

### 3. Memory Representation
```
Index:    0     1     2     3     4
        +-----+-----+-----+-----+-----+
Array:  |  10 |  20 |  30 |  40 |  50 |
        +-----+-----+-----+-----+-----+
Address: 100   104   108   112   116  (assuming 4 bytes per int)

Address of element = Base Address + (Index × Size of Element)
```

### 4. Static vs Dynamic Arrays

| Feature | Static Array | Dynamic Array (Python List) |
|---------|--------------|----------------------------|
| Size | Fixed at creation | Can grow/shrink |
| Memory | Allocated once | Reallocated when needed |
| Insertion | O(n) | O(1) amortized (append) |
| Memory overhead | None | Extra space for growth |

### 5. Time Complexity

| Operation | Time Complexity |
|-----------|----------------|
| Access by index | O(1) |
| Search (unsorted) | O(n) |
| Search (sorted) | O(log n) |
| Insert at end | O(1) amortized |
| Insert at beginning | O(n) |
| Insert at middle | O(n) |
| Delete at end | O(1) |
| Delete at beginning | O(n) |
| Delete at middle | O(n) |

### 6. Space Complexity
- O(n) where n is the number of elements

---

## Algorithms (Complete! ✅)

| # | File | Covers | Key Algorithms | Status |
|---|------|--------|----------------|--------|
| 1 | `01_traversal.py` | Iteration patterns | For/while loops, enumerate, zip, nested, reverse | ✅ |
| 2 | `02_insertion.py` | Adding elements | Insert at end/beginning/position, sorted insert | ✅ |
| 3 | `03_deletion.py` | Removing elements | Delete by index/value, duplicates, two-pointer technique | ✅ |
| 4 | `04_searching.py` | Finding elements | Linear search, Binary search (+ variations), Rotated array | ✅ |
| 5 | `05_reverse_rotate.py` | Manipulation | Reverse in-place, Rotation (reversal trick), Count rotations | ✅ |
| 6 | `06_interview_classics.py` | Top patterns | Two Sum, Kadane's, Sliding Window, Stock Buy/Sell, Prefix Sum | ✅ |
| 7 | `07_advanced_patterns.py` | Hard problems | Dutch Flag, Moore's Voting, Monotonic Stack, Trapping Water | ✅ |

### What's Covered (50+ algorithms!)

**Basic Operations:**
- Traversal (forward, reverse, nested, conditional)
- Insertion (end, beginning, position, sorted)
- Deletion (by index, by value, duplicates, two-pointer)

**Searching:**
- Linear Search (basic, with condition)
- Binary Search (standard, leftmost, rightmost, insert position, rotated array)
- Interpolation Search, Jump Search

**Manipulation:**
- Reverse (in-place, partial)
- Rotation (left, right, reversal trick, cyclic)
- Merge sorted arrays (standard, in-place)

**Interview Classics (LeetCode Top Patterns):**
- Two Sum (brute, hash, sorted)
- Maximum Subarray (Kadane's Algorithm)
- Sliding Window (fixed size, variable size)
- Best Time to Buy/Sell Stock (single, multiple transactions)
- Product of Array Except Self
- Subarray Sum Equals K
- Contains Duplicate (nearby variant)

**Advanced Patterns:**
- Dutch National Flag (3-way partition)
- Moore's Voting Algorithm (majority element)
- Next Greater/Smaller Element (monotonic stack)
- Trapping Rain Water (two pointers)
- Container With Most Water
- First Missing Positive (cyclic sort)
- Merge Intervals
- Set Matrix Zeros

---

## Practice Problems

### Easy

| # | Problem | Source | Solution | Status |
|---|---------|--------|----------|--------|
| 1 | Two Sum | LeetCode #1 | `problems/01_two_sum.py` | ⚪️ |
| 2 | Remove Duplicates from Sorted Array | LeetCode #26 | `problems/02_remove_duplicates.py` | ⚪️ |
| 3 | Remove Element | LeetCode #27 | `problems/03_remove_element.py` | ⚪️ |
| 4 | Search Insert Position | LeetCode #35 | `problems/04_search_insert.py` | ⚪️ |
| 5 | Plus One | LeetCode #66 | `problems/05_plus_one.py` | ⚪️ |
| 6 | Merge Sorted Array | LeetCode #88 | `problems/06_merge_sorted.py` | ⚪️ |
| 7 | Best Time to Buy and Sell Stock | LeetCode #121 | `problems/07_buy_sell_stock.py` | ⚪️ |
| 8 | Single Number | LeetCode #136 | `problems/08_single_number.py` | ⚪️ |
| 9 | Majority Element | LeetCode #169 | `problems/09_majority_element.py` | ⚪️ |
| 10 | Contains Duplicate | LeetCode #217 | `problems/10_contains_duplicate.py` | ⚪️ |

### Medium

| # | Problem | Source | Solution | Status |
|---|---------|--------|----------|--------|
| 11 | 3Sum | LeetCode #15 | `problems/11_three_sum.py` | ⚪️ |
| 12 | Container With Most Water | LeetCode #11 | `problems/12_container_water.py` | ⚪️ |
| 13 | Next Permutation | LeetCode #31 | `problems/13_next_permutation.py` | ⚪️ |
| 14 | Search in Rotated Array | LeetCode #33 | `problems/14_search_rotated.py` | ⚪️ |
| 15 | Find First and Last Position | LeetCode #34 | `problems/15_first_last_position.py` | ⚪️ |
| 16 | Rotate Array | LeetCode #189 | `problems/16_rotate_array.py` | ⚪️ |
| 17 | Product of Array Except Self | LeetCode #238 | `problems/17_product_except_self.py` | ⚪️ |
| 18 | Maximum Subarray (Kadane's) | LeetCode #53 | `problems/18_max_subarray.py` | ⚪️ |
| 19 | Subarray Sum Equals K | LeetCode #560 | `problems/19_subarray_sum_k.py` | ⚪️ |
| 20 | Sort Colors (Dutch National Flag) | LeetCode #75 | `problems/20_sort_colors.py` | ⚪️ |

### Hard

| # | Problem | Source | Solution | Status |
|---|---------|--------|----------|--------|
| 21 | First Missing Positive | LeetCode #41 | `problems/21_first_missing_positive.py` | ⚪️ |
| 22 | Trapping Rain Water | LeetCode #42 | `problems/22_trapping_rain_water.py` | ⚪️ |
| 23 | Median of Two Sorted Arrays | LeetCode #4 | `problems/23_median_two_arrays.py` | ⚪️ |
| 24 | Sliding Window Maximum | LeetCode #239 | `problems/24_sliding_window_max.py` | ⚪️ |

---

## Key Patterns to Learn

1. **Two Pointers** - Start/End or Slow/Fast
2. **Sliding Window** - Fixed or Variable size
3. **Prefix Sum** - Running totals
4. **Binary Search** - On sorted arrays
5. **Dutch National Flag** - 3-way partitioning
6. **Kadane's Algorithm** - Maximum subarray
7. **Moore's Voting** - Majority element

---

## Notes

### Common Mistakes to Avoid
- Off-by-one errors (index out of bounds)
- Forgetting 0-based indexing
- Modifying array while iterating
- Not handling empty arrays

### Python Tips
```python
# List comprehension
squares = [x**2 for x in range(10)]

# Enumerate for index + value
for i, val in enumerate(arr):
    print(i, val)

# Zip for parallel iteration
for a, b in zip(arr1, arr2):
    print(a, b)

# Slice notation
arr[start:end:step]
arr[::-1]  # Reverse

# Built-in functions
len(arr), sum(arr), min(arr), max(arr)
sorted(arr), arr.sort()  # Returns new vs in-place
```

---

## Progress

- [ ] Complete all concepts
- [ ] Implement all algorithms
- [ ] Solve 10 Easy problems
- [ ] Solve 10 Medium problems
- [ ] Solve 4 Hard problems
