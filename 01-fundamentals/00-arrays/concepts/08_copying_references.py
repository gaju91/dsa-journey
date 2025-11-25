"""
08. Copying and References
==========================
Understanding shallow copy, deep copy, and reference behavior.
"""

import copy

# ============================================
# 1. REFERENCE BEHAVIOR
# ============================================

# Assignment creates a REFERENCE, not a copy
original = [1, 2, 3, 4, 5]
reference = original  # Both point to same object!

reference[0] = 100
print(original)   # [100, 2, 3, 4, 5] - Changed!
print(reference)  # [100, 2, 3, 4, 5]

# Check identity
print(original is reference)  # True - same object
print(id(original) == id(reference))  # True

# ============================================
# 2. SHALLOW COPY
# ============================================

original = [1, 2, 3, 4, 5]

# Method 1: slice
shallow1 = original[:]

# Method 2: list() constructor
shallow2 = list(original)

# Method 3: copy() method
shallow3 = original.copy()

# Method 4: copy module
shallow4 = copy.copy(original)

# Modifying shallow copy doesn't affect original
shallow1[0] = 100
print(original)  # [1, 2, 3, 4, 5] - Unchanged!
print(shallow1)  # [100, 2, 3, 4, 5]

# ============================================
# 3. SHALLOW COPY PROBLEM WITH NESTED LISTS
# ============================================

# Shallow copy only copies REFERENCES for nested objects!
original = [[1, 2], [3, 4], [5, 6]]
shallow = original.copy()

# Outer list is independent
print(original is shallow)     # False

# But inner lists are shared!
print(original[0] is shallow[0])  # True!

# Modifying inner list affects both
shallow[0][0] = 999
print(original)  # [[999, 2], [3, 4], [5, 6]] - Changed!
print(shallow)   # [[999, 2], [3, 4], [5, 6]]

# Adding new inner list only affects copy
shallow.append([7, 8])
print(original)  # [[999, 2], [3, 4], [5, 6]] - Unchanged
print(shallow)   # [[999, 2], [3, 4], [5, 6], [7, 8]]

# ============================================
# 4. DEEP COPY
# ============================================

original = [[1, 2], [3, 4], [5, 6]]
deep = copy.deepcopy(original)

# Completely independent
print(original is deep)        # False
print(original[0] is deep[0])  # False - different inner lists!

# Modifying deep copy doesn't affect original
deep[0][0] = 999
print(original)  # [[1, 2], [3, 4], [5, 6]] - Unchanged!
print(deep)      # [[999, 2], [3, 4], [5, 6]]

# ============================================
# 5. MANUAL DEEP COPY (FOR 2D ARRAYS)
# ============================================

# Using list comprehension
original = [[1, 2], [3, 4], [5, 6]]
deep_manual = [row[:] for row in original]
# or
deep_manual = [list(row) for row in original]

# For deeper nesting, use copy.deepcopy

# ============================================
# 6. VISUALIZING MEMORY
# ============================================

"""
REFERENCE (a = b):
    a ──────┐
            ├──> [1, 2, 3]
    b ──────┘

SHALLOW COPY:
    original ──> [ptr1, ptr2, ptr3]
                   │      │      │
                   ▼      ▼      ▼
    shallow  ──> [ptr1, ptr2, ptr3]
                   │      │      │
                   ▼      ▼      ▼
                 [1,2]  [3,4]  [5,6]  <- SHARED!

DEEP COPY:
    original ──> [ptr1, ptr2, ptr3]
                   │      │      │
                   ▼      ▼      ▼
                 [1,2]  [3,4]  [5,6]

    deep     ──> [ptr4, ptr5, ptr6]
                   │      │      │
                   ▼      ▼      ▼
                 [1,2]  [3,4]  [5,6]  <- INDEPENDENT!
"""

# ============================================
# 7. COMMON PITFALLS
# ============================================

# Pitfall 1: Default mutable argument
def append_to(element, lst=[]):  # WRONG!
    lst.append(element)
    return lst

print(append_to(1))  # [1]
print(append_to(2))  # [1, 2] - Unexpected!

# CORRECT way:
def append_to_correct(element, lst=None):
    if lst is None:
        lst = []
    lst.append(element)
    return lst

# Pitfall 2: Multiplication with nested lists
wrong = [[0] * 3] * 3
wrong[0][0] = 1
print(wrong)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]] - All rows changed!

correct = [[0] * 3 for _ in range(3)]
correct[0][0] = 1
print(correct)  # [[1, 0, 0], [0, 0, 0], [0, 0, 0]] - Only first row

# Pitfall 3: Passing list to function
def modify(lst):
    lst.append(100)  # Modifies original!

my_list = [1, 2, 3]
modify(my_list)
print(my_list)  # [1, 2, 3, 100]

# To avoid modification, pass a copy
modify(my_list.copy())

# ============================================
# 8. CHECKING COPY STATUS
# ============================================

a = [1, 2, [3, 4]]
b = a
c = a.copy()
d = copy.deepcopy(a)

# Identity check
print(a is b)  # True - same object
print(a is c)  # False - different object
print(a is d)  # False - different object

# Equality check
print(a == b == c == d)  # True - same values

# Nested object identity
print(a[2] is b[2])  # True - same nested
print(a[2] is c[2])  # True - shallow copy shares nested
print(a[2] is d[2])  # False - deep copy is independent

# ============================================
# 9. WHEN TO USE WHAT
# ============================================

"""
USE REFERENCE (=):
- When you want multiple names for same object
- When you want changes to reflect everywhere

USE SHALLOW COPY:
- For flat lists (no nested objects)
- When nested objects should be shared
- Faster than deep copy

USE DEEP COPY:
- For nested structures that must be independent
- When you need complete isolation
- Slower, uses more memory
"""

# ============================================
# 10. PERFORMANCE COMPARISON
# ============================================

import time

# Setup
size = 10000
original = [[i, i+1] for i in range(size)]

# Benchmark
def benchmark(name, func):
    start = time.time()
    for _ in range(100):
        func()
    print(f"{name}: {time.time() - start:.4f}s")

# Uncomment to test:
# benchmark("Reference", lambda: original)
# benchmark("Shallow [:] ", lambda: original[:])
# benchmark("Shallow copy()", lambda: original.copy())
# benchmark("Deep copy", lambda: copy.deepcopy(original))
# benchmark("Manual deep", lambda: [row[:] for row in original])

"""
Typical results:
Reference:      ~0.0001s
Shallow copy:   ~0.01s
Manual deep:    ~0.1s
Deep copy:      ~1.0s
"""

if __name__ == "__main__":
    # Demo
    original = [[1, 2], [3, 4]]

    shallow = original.copy()
    deep = copy.deepcopy(original)

    print("Original:", original)
    print("Shallow is separate?", original is not shallow)
    print("Shallow inner shared?", original[0] is shallow[0])
    print("Deep inner shared?", original[0] is deep[0])
