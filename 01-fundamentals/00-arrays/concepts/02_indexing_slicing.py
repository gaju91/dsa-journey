"""
02. Indexing and Slicing
========================
Master the art of accessing single elements and extracting sublists.
"""

# ============================================
# 1. INDEXING RECAP
# ============================================

arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#       0    1    2    3    4    5    6   <- positive index
#      -7   -6   -5   -4   -3   -2   -1   <- negative index

# Positive indexing
print(arr[0])   # 'a' - first element
print(arr[3])   # 'd' - fourth element

# Negative indexing
print(arr[-1])  # 'g' - last element
print(arr[-3])  # 'e' - third from end

# ============================================
# 2. BASIC SLICING: arr[start:stop]
# ============================================
# Returns elements from index 'start' to 'stop-1'
# stop is EXCLUSIVE!

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slices
print(arr[2:5])   # [2, 3, 4] - index 2, 3, 4
print(arr[0:3])   # [0, 1, 2] - first 3 elements
print(arr[5:8])   # [5, 6, 7]

# Omitting start (defaults to 0)
print(arr[:4])    # [0, 1, 2, 3] - first 4 elements
print(arr[:1])    # [0] - first element as list

# Omitting stop (defaults to end)
print(arr[7:])    # [7, 8, 9] - from index 7 to end
print(arr[-3:])   # [7, 8, 9] - last 3 elements

# Omitting both (copy entire list)
print(arr[:])     # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ============================================
# 3. SLICING WITH STEP: arr[start:stop:step]
# ============================================

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Every 2nd element
print(arr[::2])     # [0, 2, 4, 6, 8]
print(arr[1::2])    # [1, 3, 5, 7, 9] - odd indices

# Every 3rd element
print(arr[::3])     # [0, 3, 6, 9]

# With start and stop
print(arr[1:8:2])   # [1, 3, 5, 7]

# ============================================
# 4. NEGATIVE STEP (REVERSE)
# ============================================

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Reverse entire list
print(arr[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Reverse with step
print(arr[::-2])    # [9, 7, 5, 3, 1]

# Reverse a portion
print(arr[5:1:-1])  # [5, 4, 3, 2] - from 5 down to 2

# ============================================
# 5. NEGATIVE INDICES IN SLICING
# ============================================

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(arr[-5:])      # [5, 6, 7, 8, 9] - last 5
print(arr[:-2])      # [0, 1, 2, 3, 4, 5, 6, 7] - all except last 2
print(arr[-7:-2])    # [3, 4, 5, 6, 7]
print(arr[-1:-6:-1]) # [9, 8, 7, 6, 5] - reverse last 5

# ============================================
# 6. SLICE ASSIGNMENT
# ============================================

arr = [0, 1, 2, 3, 4, 5]

# Replace a portion
arr[1:4] = [10, 20, 30]  # [0, 10, 20, 30, 4, 5]

# Replace with different size (list grows/shrinks)
arr = [0, 1, 2, 3, 4, 5]
arr[1:4] = [99]          # [0, 99, 4, 5]

arr = [0, 1, 2, 3, 4, 5]
arr[1:2] = [10, 20, 30]  # [0, 10, 20, 30, 2, 3, 4, 5]

# Insert without replacing
arr = [0, 1, 2, 3]
arr[2:2] = [100, 200]    # [0, 1, 100, 200, 2, 3]

# Delete using slice
arr = [0, 1, 2, 3, 4, 5]
arr[1:4] = []            # [0, 4, 5]

# ============================================
# 7. SLICING CREATES A NEW LIST
# ============================================

original = [1, 2, 3, 4, 5]
sliced = original[1:4]

sliced[0] = 999
print(original)  # [1, 2, 3, 4, 5] - unchanged
print(sliced)    # [999, 3, 4]

# Shallow copy using slice
copy = original[:]
print(copy is original)  # False - different objects

# ============================================
# 8. COMMON PATTERNS
# ============================================

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# First n elements
n = 3
first_n = arr[:n]        # [1, 2, 3]

# Last n elements
last_n = arr[-n:]        # [8, 9, 10]

# Remove first element
without_first = arr[1:]  # [2, 3, 4, 5, 6, 7, 8, 9, 10]

# Remove last element
without_last = arr[:-1]  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Middle element(s)
mid = len(arr) // 2
middle = arr[mid]        # 6 (for odd length, single middle)

# Split in half
first_half = arr[:mid]   # [1, 2, 3, 4, 5]
second_half = arr[mid:]  # [6, 7, 8, 9, 10]

# Every nth element starting from k
k, n = 1, 3
pattern = arr[k::n]      # [2, 5, 8]

# ============================================
# 9. OUT OF BOUNDS BEHAVIOR
# ============================================

arr = [1, 2, 3, 4, 5]

# Indexing out of bounds raises IndexError
# arr[10]  # IndexError!

# But slicing is forgiving!
print(arr[2:100])   # [3, 4, 5] - goes to end
print(arr[100:200]) # [] - empty list
print(arr[-100:2])  # [1, 2] - starts from beginning

# ============================================
# 10. STRINGS USE SAME SLICING!
# ============================================

s = "Hello, World!"
print(s[0:5])    # "Hello"
print(s[::-1])   # "!dlroW ,olleH" - reverse
print(s[7:])     # "World!"

# ============================================
# PRACTICE EXERCISES
# ============================================
"""
1. Get the last 4 elements of [1,2,3,4,5,6,7,8,9,10]
2. Reverse a list using slicing
3. Get every 3rd element starting from index 1
4. Extract middle 3 elements from [1,2,3,4,5,6,7]
5. Remove first and last elements using slicing
"""

if __name__ == "__main__":
    demo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Original: {demo}")
    print(f"First 3: {demo[:3]}")
    print(f"Last 3: {demo[-3:]}")
    print(f"Reversed: {demo[::-1]}")
    print(f"Every 2nd: {demo[::2]}")
