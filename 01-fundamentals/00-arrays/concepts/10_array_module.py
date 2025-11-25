"""
10. Array Module and NumPy Basics
=================================
Typed arrays for performance-critical applications.
"""

# ============================================
# 1. PYTHON ARRAY MODULE
# ============================================

from array import array

# Create typed array
# Type codes: 'b'=byte, 'i'=int, 'f'=float, 'd'=double, etc.

int_arr = array('i', [1, 2, 3, 4, 5])  # signed int
float_arr = array('f', [1.0, 2.5, 3.14])  # float
double_arr = array('d', [1.0, 2.5, 3.14])  # double

# Common type codes
"""
| Code | C Type           | Python Type | Size (bytes) |
|------|------------------|-------------|--------------|
| 'b'  | signed char      | int         | 1            |
| 'B'  | unsigned char    | int         | 1            |
| 'h'  | signed short     | int         | 2            |
| 'H'  | unsigned short   | int         | 2            |
| 'i'  | signed int       | int         | 2-4          |
| 'I'  | unsigned int     | int         | 2-4          |
| 'l'  | signed long      | int         | 4            |
| 'L'  | unsigned long    | int         | 4            |
| 'q'  | signed long long | int         | 8            |
| 'Q'  | unsigned long long| int        | 8            |
| 'f'  | float            | float       | 4            |
| 'd'  | double           | float       | 8            |
"""

# ============================================
# 2. ARRAY OPERATIONS
# ============================================

arr = array('i', [1, 2, 3, 4, 5])

# Access and modify (same as list)
print(arr[0])      # 1
arr[0] = 10
print(arr)         # array('i', [10, 2, 3, 4, 5])

# Slicing
print(arr[1:4])    # array('i', [2, 3, 4])

# Append and extend
arr.append(6)
arr.extend([7, 8, 9])

# Insert and pop
arr.insert(0, 0)   # Insert at index 0
arr.pop()          # Remove last

# Type checking
print(arr.typecode)  # 'i'
print(arr.itemsize)  # 4 (bytes per element)

# Convert to list
lst = arr.tolist()

# ============================================
# 3. ARRAY VS LIST MEMORY
# ============================================

import sys

# List stores object references
lst = list(range(1000))
arr = array('i', range(1000))

print(f"List size: {sys.getsizeof(lst)} bytes")
print(f"Array size: {sys.getsizeof(arr)} bytes")
# Array uses ~10x less memory for integers!

# ============================================
# 4. NUMPY BASICS (if installed)
# ============================================

try:
    import numpy as np

    # Creating arrays
    np_arr = np.array([1, 2, 3, 4, 5])
    zeros = np.zeros(5)           # [0., 0., 0., 0., 0.]
    ones = np.ones(5)             # [1., 1., 1., 1., 1.]
    empty = np.empty(5)           # Uninitialized
    arange = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
    linspace = np.linspace(0, 1, 5)  # [0., 0.25, 0.5, 0.75, 1.]

    # 2D arrays
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    zeros_2d = np.zeros((3, 4))   # 3x4 matrix of zeros
    identity = np.eye(3)          # 3x3 identity matrix

    # Data types
    int_arr = np.array([1, 2, 3], dtype=np.int32)
    float_arr = np.array([1, 2, 3], dtype=np.float64)

    # Array properties
    print(f"Shape: {matrix.shape}")     # (2, 3)
    print(f"Dimensions: {matrix.ndim}") # 2
    print(f"Size: {matrix.size}")       # 6
    print(f"Dtype: {matrix.dtype}")     # int64

    # ============================================
    # 5. NUMPY OPERATIONS
    # ============================================

    a = np.array([1, 2, 3, 4, 5])
    b = np.array([10, 20, 30, 40, 50])

    # Element-wise operations (vectorized)
    print(a + b)      # [11, 22, 33, 44, 55]
    print(a * b)      # [10, 40, 90, 160, 250]
    print(a ** 2)     # [1, 4, 9, 16, 25]
    print(np.sqrt(a)) # [1., 1.41, 1.73, 2., 2.24]

    # Comparison (returns boolean array)
    print(a > 2)      # [False, False, True, True, True]

    # Boolean indexing
    print(a[a > 2])   # [3, 4, 5]

    # Aggregation
    print(np.sum(a))      # 15
    print(np.mean(a))     # 3.0
    print(np.std(a))      # 1.41
    print(np.min(a))      # 1
    print(np.max(a))      # 5
    print(np.argmin(a))   # 0 (index of min)
    print(np.argmax(a))   # 4 (index of max)

    # ============================================
    # 6. NUMPY SLICING
    # ============================================

    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    # Same as Python lists
    print(arr[2:5])     # [2, 3, 4]
    print(arr[::2])     # [0, 2, 4, 6, 8]
    print(arr[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    # 2D slicing
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(matrix[0, :])   # [1, 2, 3] - first row
    print(matrix[:, 0])   # [1, 4, 7] - first column
    print(matrix[0:2, 1:3])  # [[2, 3], [5, 6]]

    # ============================================
    # 7. NUMPY RESHAPING
    # ============================================

    arr = np.arange(12)  # [0, 1, 2, ..., 11]

    # Reshape to 2D
    matrix = arr.reshape(3, 4)  # 3 rows, 4 cols
    matrix = arr.reshape(4, 3)  # 4 rows, 3 cols
    matrix = arr.reshape(2, -1) # -1 = auto-calculate

    # Flatten
    flat = matrix.flatten()  # Returns copy
    flat = matrix.ravel()    # Returns view if possible

    # Transpose
    transposed = matrix.T

    # ============================================
    # 8. NUMPY BROADCASTING
    # ============================================

    # Scalar operations
    arr = np.array([1, 2, 3])
    print(arr + 10)    # [11, 12, 13]
    print(arr * 2)     # [2, 4, 6]

    # Array broadcasting
    a = np.array([[1], [2], [3]])  # (3, 1)
    b = np.array([10, 20, 30])      # (3,)
    print(a + b)
    # [[11, 21, 31],
    #  [12, 22, 32],
    #  [13, 23, 33]]

    NUMPY_AVAILABLE = True

except ImportError:
    NUMPY_AVAILABLE = False
    print("NumPy not installed. Install with: pip install numpy")

# ============================================
# 9. WHEN TO USE WHAT
# ============================================

"""
USE PYTHON LIST:
- Mixed data types
- Frequent insertions/deletions
- Small datasets
- When you need list methods

USE ARRAY MODULE:
- Homogeneous numeric data
- Memory-constrained
- When NumPy is overkill
- Interfacing with C code

USE NUMPY:
- Numerical computations
- Large datasets
- Matrix operations
- Scientific computing
- Performance-critical numeric code
"""

# ============================================
# 10. PERFORMANCE COMPARISON
# ============================================

import time

def benchmark_sum():
    size = 1000000

    # Python list
    lst = list(range(size))
    start = time.time()
    total = sum(lst)
    list_time = time.time() - start

    # Array module
    arr = array('i', range(size))
    start = time.time()
    total = sum(arr)
    array_time = time.time() - start

    print(f"List sum: {list_time:.4f}s")
    print(f"Array sum: {array_time:.4f}s")

    if NUMPY_AVAILABLE:
        np_arr = np.arange(size)
        start = time.time()
        total = np.sum(np_arr)
        numpy_time = time.time() - start
        print(f"NumPy sum: {numpy_time:.4f}s")

# Uncomment to run:
# benchmark_sum()

if __name__ == "__main__":
    # Array module demo
    arr = array('i', [1, 2, 3, 4, 5])
    print(f"Array: {arr}")
    print(f"Type: {arr.typecode}")
    print(f"Item size: {arr.itemsize} bytes")

    if NUMPY_AVAILABLE:
        np_arr = np.array([1, 2, 3, 4, 5])
        print(f"\nNumPy array: {np_arr}")
        print(f"Shape: {np_arr.shape}")
        print(f"Sum: {np.sum(np_arr)}")
        print(f"Squared: {np_arr ** 2}")
