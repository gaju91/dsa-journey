"""
03. List Methods
================
Complete reference of all list methods with examples and time complexity.
"""

# ============================================
# 1. ADDING ELEMENTS
# ============================================

# append(x) - Add to end - O(1) amortized
arr = [1, 2, 3]
arr.append(4)        # [1, 2, 3, 4]
arr.append([5, 6])   # [1, 2, 3, 4, [5, 6]] - adds as single element!

# extend(iterable) - Add all elements from iterable - O(k) where k = len(iterable)
arr = [1, 2, 3]
arr.extend([4, 5])   # [1, 2, 3, 4, 5]
arr.extend("ab")     # [1, 2, 3, 4, 5, 'a', 'b']
arr.extend(range(3)) # adds 0, 1, 2

# insert(i, x) - Insert at index i - O(n)
arr = [1, 2, 4, 5]
arr.insert(2, 3)     # [1, 2, 3, 4, 5] - insert 3 at index 2
arr.insert(0, 0)     # [0, 1, 2, 3, 4, 5] - insert at beginning
arr.insert(-1, 99)   # [0, 1, 2, 3, 4, 99, 5] - before last
arr.insert(100, 6)   # Appends if index > len

# ============================================
# 2. REMOVING ELEMENTS
# ============================================

# remove(x) - Remove first occurrence - O(n)
arr = [1, 2, 3, 2, 4]
arr.remove(2)        # [1, 3, 2, 4] - removes first 2
# arr.remove(99)     # ValueError if not found!

# pop([i]) - Remove and return element at index - O(1) for end, O(n) otherwise
arr = [1, 2, 3, 4, 5]
last = arr.pop()     # returns 5, arr = [1, 2, 3, 4]
first = arr.pop(0)   # returns 1, arr = [2, 3, 4]
mid = arr.pop(1)     # returns 3, arr = [2, 4]

# clear() - Remove all elements - O(n)
arr = [1, 2, 3]
arr.clear()          # []

# del statement - Remove by index or slice - O(n)
arr = [0, 1, 2, 3, 4, 5]
del arr[0]           # [1, 2, 3, 4, 5]
del arr[1:3]         # [1, 4, 5]
del arr[:]           # [] - clear all

# ============================================
# 3. FINDING ELEMENTS
# ============================================

# index(x[, start[, end]]) - Find index of first occurrence - O(n)
arr = [10, 20, 30, 20, 40]
idx = arr.index(20)       # 1 (first occurrence)
idx = arr.index(20, 2)    # 3 (search from index 2)
idx = arr.index(20, 2, 5) # 3 (search in range [2, 5))
# arr.index(99)           # ValueError if not found!

# count(x) - Count occurrences - O(n)
arr = [1, 2, 2, 3, 2, 4]
cnt = arr.count(2)        # 3
cnt = arr.count(99)       # 0 (not found)

# ============================================
# 4. SORTING
# ============================================

# sort(key=None, reverse=False) - Sort in-place - O(n log n)
arr = [3, 1, 4, 1, 5, 9, 2, 6]
arr.sort()                # [1, 1, 2, 3, 4, 5, 6, 9]

arr = [3, 1, 4, 1, 5]
arr.sort(reverse=True)    # [5, 4, 3, 1, 1]

# Sort with key function
words = ["banana", "pie", "Washington", "book"]
words.sort()                        # Alphabetical
words.sort(key=len)                 # By length
words.sort(key=str.lower)           # Case-insensitive
words.sort(key=lambda x: x[-1])     # By last character

# sorted() - Returns new sorted list (not a method, but related)
arr = [3, 1, 4, 1, 5]
new_arr = sorted(arr)               # arr unchanged
new_arr = sorted(arr, reverse=True)

# ============================================
# 5. REVERSING
# ============================================

# reverse() - Reverse in-place - O(n)
arr = [1, 2, 3, 4, 5]
arr.reverse()        # [5, 4, 3, 2, 1]

# reversed() - Returns iterator (not a method, but related)
arr = [1, 2, 3, 4, 5]
rev = list(reversed(arr))  # [5, 4, 3, 2, 1], original unchanged

# Slicing method
rev = arr[::-1]            # Creates new reversed list

# ============================================
# 6. COPYING
# ============================================

# copy() - Shallow copy - O(n)
arr = [1, 2, 3]
copy1 = arr.copy()
copy2 = arr[:]        # Equivalent using slicing
copy3 = list(arr)     # Using constructor

# Shallow copy caveat with nested lists
arr = [[1, 2], [3, 4]]
shallow = arr.copy()
shallow[0][0] = 99    # Affects both! [[99, 2], [3, 4]]

# Deep copy for nested structures
import copy
deep = copy.deepcopy(arr)

# ============================================
# 7. CONCATENATION AND REPETITION
# ============================================

# + operator - Concatenate (creates new list)
a = [1, 2]
b = [3, 4]
c = a + b            # [1, 2, 3, 4]

# += operator - Extend in-place
a = [1, 2]
a += [3, 4]          # [1, 2, 3, 4] - same as extend

# * operator - Repeat
arr = [0] * 5        # [0, 0, 0, 0, 0]
arr = [1, 2] * 3     # [1, 2, 1, 2, 1, 2]

# ============================================
# 8. COMPARISON
# ============================================

# Lexicographic comparison
[1, 2, 3] == [1, 2, 3]  # True
[1, 2, 3] < [1, 2, 4]   # True (element-wise)
[1, 2] < [1, 2, 3]      # True (shorter is "less")
[2] > [1, 9, 9]         # True (first element decides)

# ============================================
# METHOD SUMMARY TABLE
# ============================================
"""
| Method      | Description                    | Time    | Returns   |
|-------------|--------------------------------|---------|-----------|
| append(x)   | Add x to end                   | O(1)*   | None      |
| extend(it)  | Add all from iterable          | O(k)    | None      |
| insert(i,x) | Insert x at index i            | O(n)    | None      |
| remove(x)   | Remove first occurrence of x   | O(n)    | None      |
| pop([i])    | Remove & return at index       | O(1)/O(n)| Element  |
| clear()     | Remove all elements            | O(n)    | None      |
| index(x)    | Find index of x                | O(n)    | int       |
| count(x)    | Count occurrences of x         | O(n)    | int       |
| sort()      | Sort in-place                  | O(nlogn)| None      |
| reverse()   | Reverse in-place               | O(n)    | None      |
| copy()      | Shallow copy                   | O(n)    | list      |

* amortized O(1) for append
"""

if __name__ == "__main__":
    # Demo of common operations
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"Original: {arr}")

    arr.append(10)
    print(f"After append(10): {arr}")

    arr.sort()
    print(f"After sort(): {arr}")

    arr.reverse()
    print(f"After reverse(): {arr}")

    popped = arr.pop()
    print(f"pop() returned: {popped}, list: {arr}")
