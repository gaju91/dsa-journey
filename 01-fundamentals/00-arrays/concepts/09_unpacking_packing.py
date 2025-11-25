"""
09. Unpacking and Packing
=========================
Pythonic ways to work with sequences.
"""

# ============================================
# 1. BASIC UNPACKING
# ============================================

# Unpack list to variables
arr = [1, 2, 3]
a, b, c = arr
print(a, b, c)  # 1 2 3

# Unpack tuple
point = (10, 20)
x, y = point

# Unpack string
chars = "ABC"
first, second, third = chars  # 'A', 'B', 'C'

# Number of variables must match!
# a, b = [1, 2, 3]  # ValueError: too many values to unpack
# a, b, c, d = [1, 2, 3]  # ValueError: not enough values

# ============================================
# 2. SWAPPING VALUES
# ============================================

a, b = 1, 2
a, b = b, a  # Swap without temp variable!
print(a, b)  # 2 1

# Rotate three values
a, b, c = 1, 2, 3
a, b, c = b, c, a
print(a, b, c)  # 2 3 1

# Swap in list
arr = [1, 2, 3, 4, 5]
arr[0], arr[-1] = arr[-1], arr[0]  # Swap first and last
print(arr)  # [5, 2, 3, 4, 1]

# ============================================
# 3. EXTENDED UNPACKING (*)
# ============================================

# First and rest
first, *rest = [1, 2, 3, 4, 5]
print(first)  # 1
print(rest)   # [2, 3, 4, 5]

# Last and rest
*rest, last = [1, 2, 3, 4, 5]
print(rest)   # [1, 2, 3, 4]
print(last)   # 5

# First, last, and middle
first, *middle, last = [1, 2, 3, 4, 5]
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5

# Head and tail pattern
head, *tail = [1, 2, 3, 4, 5]
# Like Haskell/Lisp car/cdr

# ============================================
# 4. IGNORING VALUES (_)
# ============================================

# Ignore specific values
a, _, c = [1, 2, 3]  # Ignore middle
print(a, c)  # 1 3

# Ignore multiple
a, *_, b = [1, 2, 3, 4, 5]  # Only first and last
print(a, b)  # 1 5

# Common in loops
for _, value in enumerate(['a', 'b', 'c']):
    print(value)  # Don't need index

# Unpack function return when you only need some
def get_user():
    return "Alice", 25, "NYC"

name, _, city = get_user()

# ============================================
# 5. NESTED UNPACKING
# ============================================

# Nested list
data = [1, [2, 3], 4]
a, (b, c), d = data
print(a, b, c, d)  # 1 2 3 4

# Matrix row unpacking
matrix = [[1, 2], [3, 4], [5, 6]]
for a, b in matrix:
    print(f"{a} + {b} = {a + b}")

# Coordinates
points = [(0, 0), (1, 1), (2, 4)]
for x, y in points:
    print(f"Point: ({x}, {y})")

# ============================================
# 6. PACKING (CREATING TUPLES/LISTS)
# ============================================

# Implicit tuple packing
packed = 1, 2, 3  # Creates (1, 2, 3)
print(type(packed))  # <class 'tuple'>

# Return multiple values (packing)
def min_max(arr):
    return min(arr), max(arr)  # Returns tuple

minimum, maximum = min_max([3, 1, 4, 1, 5])

# ============================================
# 7. * IN FUNCTION CALLS
# ============================================

def add(a, b, c):
    return a + b + c

arr = [1, 2, 3]

# Unpack list as arguments
result = add(*arr)  # Same as add(1, 2, 3)
print(result)  # 6

# Combine with other args
result = add(10, *[20, 30])  # add(10, 20, 30)

# ============================================
# 8. * IN LIST LITERALS
# ============================================

# Combine lists
a = [1, 2]
b = [3, 4]
c = [5, 6]

combined = [*a, *b, *c]  # [1, 2, 3, 4, 5, 6]
# Equivalent to: a + b + c

# Add elements while combining
combined = [0, *a, 999, *b]  # [0, 1, 2, 999, 3, 4]

# Create copy
original = [1, 2, 3]
copy = [*original]  # Same as original[:]

# ============================================
# 9. ** FOR DICTIONARIES
# ============================================

# Merge dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged = {**dict1, **dict2}  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Override values
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 99, 'c': 3}
merged = {**dict1, **dict2}  # {'a': 1, 'b': 99, 'c': 3}

# ============================================
# 10. COMMON PATTERNS
# ============================================

# Get first n and rest
n = 3
arr = [1, 2, 3, 4, 5, 6, 7]
first_n, *rest = arr[:n], arr[n:]  # Alternative way
# Better:
first_n = arr[:n]
rest = arr[n:]

# Rotate left
arr = [1, 2, 3, 4, 5]
first, *rest = arr
arr = [*rest, first]  # [2, 3, 4, 5, 1]

# Rotate right
*rest, last = arr
arr = [last, *rest]  # [1, 2, 3, 4, 5]

# Partition around pivot
def partition(arr):
    first, *middle, last = arr
    return first, middle, last

# Remove duplicates while preserving order
def unique(arr):
    seen = set()
    result = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# ============================================
# 11. UNPACKING IN LOOPS
# ============================================

# Enumerate
arr = ['a', 'b', 'c']
for i, char in enumerate(arr):
    print(i, char)

# Zip
names = ['Alice', 'Bob']
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name}: {age}")

# Items from dict
d = {'a': 1, 'b': 2}
for key, value in d.items():
    print(key, value)

# Nested structures
data = [('Alice', [90, 85, 88]), ('Bob', [78, 82, 80])]
for name, scores in data:
    print(f"{name}: avg = {sum(scores)/len(scores)}")

# ============================================
# 12. EDGE CASES
# ============================================

# Empty list with *
first, *rest = [1]
print(first)  # 1
print(rest)   # []

# Single element
*rest, last = [1]
print(rest)  # []
print(last)  # 1

# Two elements
first, *mid, last = [1, 2]
print(first, mid, last)  # 1 [] 2

if __name__ == "__main__":
    # Demo
    arr = [1, 2, 3, 4, 5]

    first, *rest = arr
    print(f"First: {first}, Rest: {rest}")

    *init, last = arr
    print(f"Init: {init}, Last: {last}")

    a, b, *_ = arr
    print(f"First two: {a}, {b}")

    # Swap
    arr[0], arr[-1] = arr[-1], arr[0]
    print(f"Swapped: {arr}")
