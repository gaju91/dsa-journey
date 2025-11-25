"""
04. List Comprehensions
=======================
Elegant, Pythonic way to create and transform lists.
"""

# ============================================
# 1. BASIC SYNTAX
# ============================================

# Traditional for loop
squares = []
for x in range(5):
    squares.append(x ** 2)
# [0, 1, 4, 9, 16]

# List comprehension equivalent
squares = [x ** 2 for x in range(5)]
# [0, 1, 4, 9, 16]

# Syntax: [expression for item in iterable]

# ============================================
# 2. WITH CONDITION (FILTERING)
# ============================================

# Syntax: [expression for item in iterable if condition]

# Even numbers only
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# Positive numbers from mixed list
nums = [-3, -1, 0, 1, 3, 5]
positives = [x for x in nums if x > 0]
# [1, 3, 5]

# Multiple conditions
divisible_by_2_and_3 = [x for x in range(30) if x % 2 == 0 if x % 3 == 0]
# [0, 6, 12, 18, 24]

# Equivalent to:
# [x for x in range(30) if x % 2 == 0 and x % 3 == 0]

# ============================================
# 3. IF-ELSE IN COMPREHENSION
# ============================================

# Syntax: [expr1 if condition else expr2 for item in iterable]
# Note: if-else comes BEFORE for

# Replace negatives with 0
nums = [-2, -1, 0, 1, 2]
non_negative = [x if x >= 0 else 0 for x in nums]
# [0, 0, 0, 1, 2]

# Even/Odd labels
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
# ['even', 'odd', 'even', 'odd', 'even']

# Combining if-else with filter
# Get squares of even numbers, cube of odd (skip negatives)
nums = [-1, 0, 1, 2, 3, 4, 5]
result = [x**2 if x % 2 == 0 else x**3 for x in nums if x >= 0]
# [0, 1, 4, 27, 16, 125]

# ============================================
# 4. NESTED LOOPS
# ============================================

# Syntax: [expr for x in iter1 for y in iter2]
# Equivalent to nested for loops (outer first)

# All pairs
pairs = [(x, y) for x in range(3) for y in range(3)]
# [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]

# Flatten 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Cartesian product with condition
products = [(x, y) for x in range(5) for y in range(5) if x != y]

# ============================================
# 5. NESTED LIST COMPREHENSION (2D ARRAYS)
# ============================================

# Create 3x3 matrix of zeros
matrix = [[0 for _ in range(3)] for _ in range(3)]
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Create 3x4 matrix with row*col values
matrix = [[row * col for col in range(4)] for row in range(3)]
# [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

# Transpose a matrix
original = [[1, 2, 3], [4, 5, 6]]
transposed = [[row[i] for row in original] for i in range(len(original[0]))]
# [[1, 4], [2, 5], [3, 6]]

# Identity matrix
n = 3
identity = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
# [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# ============================================
# 6. USING FUNCTIONS
# ============================================

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

primes = [x for x in range(50) if is_prime(x)]
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# Using built-in functions
words = ["Hello", "WORLD", "Python"]
lower_words = [word.lower() for word in words]
# ['hello', 'world', 'python']

# ============================================
# 7. WALRUS OPERATOR (:=) - Python 3.8+
# ============================================

# Avoid computing expression twice
import math

# Without walrus (inefficient)
values = [math.sqrt(x) for x in range(100) if math.sqrt(x) > 5]

# With walrus (compute once)
values = [y for x in range(100) if (y := math.sqrt(x)) > 5]

# Filter and transform in one pass
data = ["  hello  ", "", "world", "   ", "python"]
cleaned = [stripped for s in data if (stripped := s.strip())]
# ['hello', 'world', 'python']

# ============================================
# 8. COMMON PATTERNS
# ============================================

# String processing
words = "hello world python".split()
lengths = [len(w) for w in words]  # [5, 5, 6]
caps = [w.upper() for w in words]  # ['HELLO', 'WORLD', 'PYTHON']

# Filtering with type check
mixed = [1, "a", 2, "b", 3]
nums_only = [x for x in mixed if isinstance(x, int)]  # [1, 2, 3]

# Enumerate in comprehension
indexed = [(i, x) for i, x in enumerate(['a', 'b', 'c'])]
# [(0, 'a'), (1, 'b'), (2, 'c')]

# Zip in comprehension
a = [1, 2, 3]
b = [4, 5, 6]
sums = [x + y for x, y in zip(a, b)]  # [5, 7, 9]

# Unpack nested tuples
pairs = [(1, 2), (3, 4), (5, 6)]
sums = [a + b for a, b in pairs]  # [3, 7, 11]

# ============================================
# 9. PERFORMANCE CONSIDERATIONS
# ============================================

"""
List comprehensions are generally faster than for loops because:
1. Optimized C implementation
2. Less overhead from append() calls
3. Evaluates in a single expression

However:
- Don't sacrifice readability for one-liners
- Break complex comprehensions into multiple steps
- Use regular loops for side effects (printing, modifying external state)
"""

# Too complex - avoid!
# result = [x if x > 0 else -x for x in [y**2 - 10 for y in range(-5, 6)] if x % 2 == 0]

# Better - break it down
squares_minus_10 = [y**2 - 10 for y in range(-5, 6)]
positive_evens = [x if x > 0 else -x for x in squares_minus_10 if x % 2 == 0]

# ============================================
# 10. SET AND DICT COMPREHENSIONS (BONUS)
# ============================================

# Set comprehension
unique_squares = {x**2 for x in [-2, -1, 0, 1, 2]}  # {0, 1, 4}

# Dict comprehension
square_dict = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# ============================================
# PRACTICE EXERCISES
# ============================================
"""
1. Create list of squares of even numbers from 1 to 20
2. Extract all vowels from a string using comprehension
3. Flatten [[1,2],[3,4],[5,6]] to [1,2,3,4,5,6]
4. Create 5x5 multiplication table
5. Get words longer than 3 chars from a sentence
"""

if __name__ == "__main__":
    # Demo
    print("Squares:", [x**2 for x in range(5)])
    print("Evens:", [x for x in range(10) if x % 2 == 0])
    print("Even/Odd:", ["even" if x%2==0 else "odd" for x in range(5)])

    matrix = [[i*j for j in range(1,4)] for i in range(1,4)]
    print("3x3 table:", matrix)
