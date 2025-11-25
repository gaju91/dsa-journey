"""
07. Built-in Functions for Lists
=================================
Master Python's powerful built-in functions for array manipulation.
"""

# ============================================
# 1. LENGTH, SUM, MIN, MAX
# ============================================

arr = [3, 1, 4, 1, 5, 9, 2, 6]

# len() - O(1) - stored as attribute
length = len(arr)  # 8

# sum() - O(n) - with optional start value
total = sum(arr)           # 31
total = sum(arr, 10)       # 41 (starts from 10)

# min() and max() - O(n)
minimum = min(arr)  # 1
maximum = max(arr)  # 9

# With key function
words = ["python", "java", "c", "javascript"]
shortest = min(words, key=len)  # "c"
longest = max(words, key=len)   # "javascript"

# With default (Python 3.4+)
empty = []
# min(empty)  # ValueError!
minimum = min(empty, default=0)  # 0

# ============================================
# 2. SORTED() vs sort()
# ============================================

arr = [3, 1, 4, 1, 5, 9, 2, 6]

# sorted() - Returns NEW sorted list, original unchanged
new_sorted = sorted(arr)
print(arr)        # [3, 1, 4, 1, 5, 9, 2, 6] - unchanged
print(new_sorted) # [1, 1, 2, 3, 4, 5, 6, 9]

# .sort() - Sorts IN-PLACE, returns None
arr.sort()
print(arr)  # [1, 1, 2, 3, 4, 5, 6, 9]

# Reverse sorting
sorted_desc = sorted(arr, reverse=True)
arr.sort(reverse=True)

# Custom key
words = ["Banana", "apple", "Cherry"]
sorted(words)                    # ['Banana', 'Cherry', 'apple'] - ASCII order
sorted(words, key=str.lower)     # ['apple', 'Banana', 'Cherry']
sorted(words, key=len)           # ['apple', 'Banana', 'Cherry']

# Multiple criteria
students = [("Alice", 85), ("Bob", 90), ("Charlie", 85)]
sorted(students, key=lambda x: (-x[1], x[0]))  # By score desc, then name asc
# [('Bob', 90), ('Alice', 85), ('Charlie', 85)]

# ============================================
# 3. REVERSED()
# ============================================

arr = [1, 2, 3, 4, 5]

# reversed() returns iterator, not list
rev_iter = reversed(arr)
rev_list = list(reversed(arr))  # [5, 4, 3, 2, 1]

# Works on any sequence
reversed_str = ''.join(reversed("hello"))  # "olleh"

# ============================================
# 4. ANY() and ALL()
# ============================================

arr = [0, 1, 2, 3, 4]

# any() - True if at least one truthy value
any(arr)              # True (1, 2, 3, 4 are truthy)
any([0, 0, 0])        # False
any([])               # False

# all() - True if all values are truthy
all(arr)              # False (0 is falsy)
all([1, 2, 3])        # True
all([])               # True (vacuous truth)

# With conditions (generator expressions)
nums = [2, 4, 6, 8]
all_even = all(x % 2 == 0 for x in nums)  # True
has_negative = any(x < 0 for x in nums)   # False

# ============================================
# 5. MAP()
# ============================================

arr = [1, 2, 3, 4, 5]

# Apply function to each element
squares = list(map(lambda x: x**2, arr))  # [1, 4, 9, 16, 25]
strings = list(map(str, arr))             # ['1', '2', '3', '4', '5']

# Multiple iterables
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))  # [11, 22, 33]

# Prefer list comprehension for readability
squares = [x**2 for x in arr]

# ============================================
# 6. FILTER()
# ============================================

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Keep elements that satisfy condition
evens = list(filter(lambda x: x % 2 == 0, arr))  # [2, 4, 6, 8, 10]

# Filter None/falsy values
mixed = [0, 1, "", "hello", None, [], [1, 2]]
truthy = list(filter(None, mixed))  # [1, 'hello', [1, 2]]

# Prefer list comprehension
evens = [x for x in arr if x % 2 == 0]

# ============================================
# 7. REDUCE() - from functools
# ============================================

from functools import reduce

arr = [1, 2, 3, 4, 5]

# Accumulate with binary function
total = reduce(lambda acc, x: acc + x, arr)  # 15
product = reduce(lambda acc, x: acc * x, arr)  # 120
maximum = reduce(lambda a, b: a if a > b else b, arr)  # 5

# With initial value
total = reduce(lambda acc, x: acc + x, arr, 100)  # 115

# Finding max with index
arr = [3, 1, 4, 1, 5, 9, 2, 6]
max_idx = reduce(
    lambda acc, x: x if arr[x[0]] > arr[acc[0]] else acc,
    enumerate(arr),
    (0, arr[0])
)

# ============================================
# 8. ZIP()
# ============================================

a = [1, 2, 3]
b = ['a', 'b', 'c']
c = [True, False, True]

# Combine iterables
zipped = list(zip(a, b))       # [(1, 'a'), (2, 'b'), (3, 'c')]
zipped = list(zip(a, b, c))    # [(1, 'a', True), (2, 'b', False), ...]

# Unzip
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
nums, chars = zip(*pairs)      # (1, 2, 3), ('a', 'b', 'c')

# Create dict from two lists
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'NYC']
person = dict(zip(keys, values))  # {'name': 'Alice', 'age': 25, 'city': 'NYC'}

# ============================================
# 9. ENUMERATE()
# ============================================

arr = ['a', 'b', 'c', 'd']

# Get index and value
list(enumerate(arr))  # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]

# Custom start index
list(enumerate(arr, start=1))  # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

# Find index of max element
arr = [3, 1, 4, 1, 5, 9, 2, 6]
max_idx = max(enumerate(arr), key=lambda x: x[1])[0]  # 5

# ============================================
# 10. RANGE()
# ============================================

# range(stop)
list(range(5))           # [0, 1, 2, 3, 4]

# range(start, stop)
list(range(2, 7))        # [2, 3, 4, 5, 6]

# range(start, stop, step)
list(range(0, 10, 2))    # [0, 2, 4, 6, 8]
list(range(10, 0, -1))   # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
list(range(10, 0, -2))   # [10, 8, 6, 4, 2]

# Memory efficient - doesn't store all values
r = range(1000000)  # Barely uses memory
len(r)              # 1000000
500000 in r         # True - O(1) check!

# ============================================
# 11. OTHER USEFUL FUNCTIONS
# ============================================

# abs() - Absolute value
abs(-5)  # 5

# round() - Round to n decimals
round(3.14159, 2)  # 3.14

# pow() - Power
pow(2, 10)     # 1024
pow(2, 10, 7)  # 2^10 % 7 = 2 (modular exponentiation)

# divmod() - Quotient and remainder
divmod(17, 5)  # (3, 2)

# id() - Memory address
id(arr)

# type() - Type of object
type(arr)  # <class 'list'>

# isinstance() - Type checking
isinstance(arr, list)  # True
isinstance(5, (int, float))  # True

# ============================================
# PERFORMANCE NOTES
# ============================================
"""
| Function   | Time Complexity | Notes                      |
|------------|-----------------|----------------------------|
| len()      | O(1)            | Stored as attribute        |
| sum()      | O(n)            | Linear scan                |
| min/max()  | O(n)            | Linear scan                |
| sorted()   | O(n log n)      | Timsort                    |
| reversed() | O(1)            | Returns iterator           |
| any/all()  | O(n)            | Short-circuits             |
| map()      | O(1)            | Returns iterator           |
| filter()   | O(1)            | Returns iterator           |
| enumerate()| O(1)            | Returns iterator           |
| zip()      | O(1)            | Returns iterator           |
| range()    | O(1)            | Lazy evaluation            |
"""

if __name__ == "__main__":
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"Array: {arr}")
    print(f"Length: {len(arr)}")
    print(f"Sum: {sum(arr)}")
    print(f"Min: {min(arr)}, Max: {max(arr)}")
    print(f"Sorted: {sorted(arr)}")
    print(f"All positive: {all(x > 0 for x in arr)}")
    print(f"Any > 5: {any(x > 5 for x in arr)}")
