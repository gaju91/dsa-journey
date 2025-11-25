"""
05. Iterating Techniques
========================
All the ways to loop through lists in Python.
"""

# ============================================
# 1. BASIC FOR LOOP
# ============================================

arr = ['a', 'b', 'c', 'd']

# Simple iteration
for item in arr:
    print(item)  # a, b, c, d

# Using range with indexing (avoid if possible)
for i in range(len(arr)):
    print(arr[i])

# ============================================
# 2. ENUMERATE - INDEX + VALUE
# ============================================

arr = ['apple', 'banana', 'cherry']

# Get both index and value
for index, value in enumerate(arr):
    print(f"{index}: {value}")
# 0: apple
# 1: banana
# 2: cherry

# Start from custom index
for index, value in enumerate(arr, start=1):
    print(f"{index}: {value}")
# 1: apple
# 2: banana
# 3: cherry

# ============================================
# 3. ZIP - PARALLEL ITERATION
# ============================================

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['NYC', 'LA', 'Chicago']

# Two lists
for name, age in zip(names, ages):
    print(f"{name} is {age}")

# Multiple lists
for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, from {city}")

# Stops at shortest list
short = [1, 2]
long = [10, 20, 30, 40]
for a, b in zip(short, long):
    print(a, b)  # Only prints 2 pairs

# zip_longest for unequal lengths
from itertools import zip_longest
for a, b in zip_longest(short, long, fillvalue=0):
    print(a, b)  # Fills missing with 0

# ============================================
# 4. REVERSED - ITERATE BACKWARDS
# ============================================

arr = [1, 2, 3, 4, 5]

# Using reversed()
for item in reversed(arr):
    print(item)  # 5, 4, 3, 2, 1

# With enumerate (index still goes 0, 1, 2...)
for i, item in enumerate(reversed(arr)):
    print(i, item)

# Reverse with original indices
for i in range(len(arr) - 1, -1, -1):
    print(i, arr[i])  # 4:5, 3:4, 2:3, 1:2, 0:1

# ============================================
# 5. ITERTOOLS - ADVANCED ITERATION
# ============================================

from itertools import (
    chain, cycle, repeat, islice,
    combinations, permutations, product,
    groupby, accumulate, takewhile, dropwhile
)

# chain - Combine multiple iterables
a = [1, 2]
b = [3, 4]
c = [5, 6]
for item in chain(a, b, c):
    print(item)  # 1, 2, 3, 4, 5, 6

# cycle - Infinite loop through iterable
colors = ['red', 'green', 'blue']
for i, color in enumerate(cycle(colors)):
    if i >= 7: break
    print(color)  # red, green, blue, red, green, blue, red

# repeat - Repeat value
for x in repeat(5, 3):
    print(x)  # 5, 5, 5

# islice - Slice an iterator
for x in islice(range(100), 5, 10):
    print(x)  # 5, 6, 7, 8, 9

# combinations - All r-length combinations
for combo in combinations([1, 2, 3], 2):
    print(combo)  # (1,2), (1,3), (2,3)

# permutations - All r-length arrangements
for perm in permutations([1, 2, 3], 2):
    print(perm)  # (1,2), (1,3), (2,1), (2,3), (3,1), (3,2)

# product - Cartesian product
for p in product([1, 2], ['a', 'b']):
    print(p)  # (1,'a'), (1,'b'), (2,'a'), (2,'b')

# ============================================
# 6. WHILE LOOP ITERATION
# ============================================

arr = [1, 2, 3, 4, 5]

# Index-based while loop
i = 0
while i < len(arr):
    print(arr[i])
    i += 1

# Two pointers pattern
left, right = 0, len(arr) - 1
while left < right:
    print(arr[left], arr[right])
    left += 1
    right -= 1

# ============================================
# 7. MODIFYING WHILE ITERATING
# ============================================

# WRONG - Modifying list during iteration
arr = [1, 2, 3, 4, 5]
# for item in arr:
#     if item % 2 == 0:
#         arr.remove(item)  # Skips elements!

# CORRECT - Iterate over copy
arr = [1, 2, 3, 4, 5]
for item in arr[:]:  # arr.copy() also works
    if item % 2 == 0:
        arr.remove(item)
# arr = [1, 3, 5]

# BETTER - Use list comprehension
arr = [1, 2, 3, 4, 5]
arr = [x for x in arr if x % 2 != 0]
# [1, 3, 5]

# ALSO CORRECT - Iterate backwards
arr = [1, 2, 3, 4, 5]
for i in range(len(arr) - 1, -1, -1):
    if arr[i] % 2 == 0:
        arr.pop(i)

# ============================================
# 8. MAP, FILTER, REDUCE
# ============================================

arr = [1, 2, 3, 4, 5]

# map - Apply function to each element
squares = list(map(lambda x: x**2, arr))  # [1, 4, 9, 16, 25]
# Prefer: [x**2 for x in arr]

# filter - Keep elements that satisfy condition
evens = list(filter(lambda x: x % 2 == 0, arr))  # [2, 4]
# Prefer: [x for x in arr if x % 2 == 0]

# reduce - Reduce to single value
from functools import reduce
total = reduce(lambda acc, x: acc + x, arr)  # 15
product = reduce(lambda acc, x: acc * x, arr)  # 120
# Prefer: sum(arr) for summation

# ============================================
# 9. BREAKING AND CONTINUING
# ============================================

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# break - Exit loop early
for x in arr:
    if x == 5:
        break
    print(x)  # 1, 2, 3, 4

# continue - Skip current iteration
for x in arr:
    if x % 2 == 0:
        continue
    print(x)  # 1, 3, 5, 7, 9

# else clause - Runs if loop completes without break
for x in arr:
    if x == 100:
        break
else:
    print("100 not found")

# ============================================
# 10. NESTED ITERATION
# ============================================

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Iterate 2D array
for row in matrix:
    for val in row:
        print(val, end=' ')
    print()

# With indices
for i, row in enumerate(matrix):
    for j, val in enumerate(row):
        print(f"[{i}][{j}] = {val}")

# ============================================
# 11. ANY AND ALL
# ============================================

arr = [2, 4, 6, 8, 10]

# any - True if ANY element satisfies condition
has_odd = any(x % 2 != 0 for x in arr)  # False

# all - True if ALL elements satisfy condition
all_even = all(x % 2 == 0 for x in arr)  # True
all_positive = all(x > 0 for x in arr)   # True

# Short-circuit evaluation
large_list = range(1000000)
has_5 = any(x == 5 for x in large_list)  # Stops at 5, doesn't check rest

# ============================================
# PRACTICE EXERCISES
# ============================================
"""
1. Print indices and values of [10, 20, 30, 40]
2. Add corresponding elements of two lists
3. Find first negative number in list (use break)
4. Remove all occurrences of a value while iterating
5. Iterate two lists of different lengths
"""

if __name__ == "__main__":
    arr = ['a', 'b', 'c']

    print("enumerate:")
    for i, v in enumerate(arr):
        print(f"  {i}: {v}")

    print("\nzip:")
    nums = [1, 2, 3]
    for c, n in zip(arr, nums):
        print(f"  {c} -> {n}")

    print("\nreversed:")
    for v in reversed(arr):
        print(f"  {v}")
