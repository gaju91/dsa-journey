"""
01. Python List Basics
======================
Lists are Python's most versatile data structure - ordered, mutable, and can hold mixed types.
"""

# ============================================
# 1. CREATING LISTS
# ============================================

# Empty list
empty_list = []
empty_list_alt = list()

# List with elements
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]

# Mixed types (allowed but not recommended for DSA)
mixed = [1, "hello", 3.14, True, None]

# List from other iterables
from_string = list("hello")  # ['h', 'e', 'l', 'l', 'o']
from_range = list(range(5))  # [0, 1, 2, 3, 4]
from_tuple = list((1, 2, 3))  # [1, 2, 3]

# ============================================
# 2. LIST WITH DEFAULT VALUES
# ============================================

# Repeat single value
zeros = [0] * 5          # [0, 0, 0, 0, 0]
ones = [1] * 10          # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
empty_strings = [""] * 3  # ['', '', '']

# CAUTION: Mutable objects are shared references!
# Wrong way (all rows point to same list)
wrong_2d = [[0] * 3] * 3  # Changing one row changes all!

# Right way (each row is independent)
correct_2d = [[0] * 3 for _ in range(3)]

# ============================================
# 3. ACCESSING ELEMENTS
# ============================================

arr = [10, 20, 30, 40, 50]

# Positive indexing (0-based)
first = arr[0]   # 10
second = arr[1]  # 20
last = arr[4]    # 50

# Negative indexing (from end)
last_neg = arr[-1]    # 50
second_last = arr[-2]  # 40
first_neg = arr[-5]   # 10

# ============================================
# 4. CHECKING MEMBERSHIP
# ============================================

arr = [1, 2, 3, 4, 5]

# 'in' operator - O(n) time
exists = 3 in arr      # True
not_exists = 10 in arr  # False
check_not = 10 not in arr  # True

# ============================================
# 5. LIST LENGTH
# ============================================

arr = [1, 2, 3, 4, 5]
length = len(arr)  # 5

empty = []
is_empty = len(empty) == 0  # True
# Pythonic way to check empty
if not empty:
    print("List is empty")

# ============================================
# 6. MODIFYING ELEMENTS
# ============================================

arr = [1, 2, 3, 4, 5]

# Direct assignment
arr[0] = 100  # [100, 2, 3, 4, 5]
arr[-1] = 500  # [100, 2, 3, 4, 500]

# Swap elements
arr[0], arr[1] = arr[1], arr[0]  # Pythonic swap

# ============================================
# 7. LIST IDENTITY VS EQUALITY
# ============================================

a = [1, 2, 3]
b = [1, 2, 3]
c = a

# Equality (same values)
print(a == b)  # True

# Identity (same object in memory)
print(a is b)  # False
print(a is c)  # True

# ============================================
# PRACTICE EXERCISES
# ============================================
"""
1. Create a list of first 10 even numbers using list()
2. Access the middle element of [1, 2, 3, 4, 5, 6, 7]
3. Swap first and last element of a list
4. Check if 'python' exists in ['java', 'python', 'c++']
5. Create a 3x3 matrix initialized with -1
"""

if __name__ == "__main__":
    # Demo
    demo = [1, 2, 3, 4, 5]
    print(f"List: {demo}")
    print(f"First: {demo[0]}, Last: {demo[-1]}")
    print(f"Length: {len(demo)}")
    print(f"3 in list: {3 in demo}")
