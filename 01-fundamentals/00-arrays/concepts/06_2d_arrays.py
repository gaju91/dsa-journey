"""
06. 2D Arrays (Nested Lists)
============================
Working with matrices and multi-dimensional arrays.
"""

# ============================================
# 1. CREATING 2D ARRAYS
# ============================================

# Direct initialization
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Empty 2D array
empty = [[], [], []]

# Using list comprehension (CORRECT way)
rows, cols = 3, 4
matrix = [[0 for _ in range(cols)] for _ in range(rows)]
# [[0,0,0,0], [0,0,0,0], [0,0,0,0]]

# WRONG WAY - Creates shared references!
wrong = [[0] * 4] * 3  # All rows point to same list!
wrong[0][0] = 99       # Changes ALL rows!
# [[99,0,0,0], [99,0,0,0], [99,0,0,0]]

# Initialize with values
matrix = [[i * cols + j for j in range(cols)] for i in range(rows)]
# [[0,1,2,3], [4,5,6,7], [8,9,10,11]]

# ============================================
# 2. ACCESSING ELEMENTS
# ============================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access single element: matrix[row][col]
element = matrix[0][0]  # 1 (top-left)
element = matrix[1][2]  # 6 (row 1, col 2)
element = matrix[-1][-1]  # 9 (bottom-right)

# Access entire row
first_row = matrix[0]  # [1, 2, 3]
last_row = matrix[-1]  # [7, 8, 9]

# Access column (need comprehension)
first_col = [row[0] for row in matrix]  # [1, 4, 7]
last_col = [row[-1] for row in matrix]  # [3, 6, 9]

# ============================================
# 3. DIMENSIONS
# ============================================

matrix = [[1, 2, 3], [4, 5, 6]]

rows = len(matrix)        # 2
cols = len(matrix[0])     # 3 (assumes all rows equal)

# Safe way for jagged arrays
def get_dimensions(matrix):
    if not matrix:
        return 0, 0
    return len(matrix), len(matrix[0]) if matrix else 0

# ============================================
# 4. ITERATING 2D ARRAYS
# ============================================

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Row by row
for row in matrix:
    print(row)

# Element by element
for row in matrix:
    for val in row:
        print(val, end=' ')
    print()

# With indices
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(f"[{i}][{j}] = {matrix[i][j]}")

# Using enumerate
for i, row in enumerate(matrix):
    for j, val in enumerate(row):
        print(f"[{i}][{j}] = {val}")

# ============================================
# 5. MODIFYING 2D ARRAYS
# ============================================

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Modify single element
matrix[0][0] = 100

# Modify entire row
matrix[1] = [10, 20, 30]

# Modify column
for i in range(len(matrix)):
    matrix[i][2] = 0

# ============================================
# 6. COMMON MATRIX OPERATIONS
# ============================================

# --- Transpose ---
matrix = [[1, 2, 3], [4, 5, 6]]
# Method 1: List comprehension
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# [[1, 4], [2, 5], [3, 6]]

# Method 2: Using zip
transposed = [list(row) for row in zip(*matrix)]

# --- Flatten ---
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [val for row in matrix for val in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# --- Unflatten ---
flat = [1, 2, 3, 4, 5, 6]
cols = 3
matrix = [flat[i:i+cols] for i in range(0, len(flat), cols)]
# [[1, 2, 3], [4, 5, 6]]

# --- Rotate 90° clockwise ---
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotated = [list(row) for row in zip(*matrix[::-1])]
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

# --- Rotate 90° counter-clockwise ---
rotated_ccw = [list(row)[::-1] for row in zip(*matrix)]
# [[3, 6, 9], [2, 5, 8], [1, 4, 7]]

# ============================================
# 7. DIAGONAL TRAVERSALS
# ============================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Main diagonal (top-left to bottom-right)
main_diag = [matrix[i][i] for i in range(len(matrix))]
# [1, 5, 9]

# Anti-diagonal (top-right to bottom-left)
n = len(matrix)
anti_diag = [matrix[i][n-1-i] for i in range(n)]
# [3, 5, 7]

# All diagonals (for n x n matrix)
def get_all_diagonals(matrix):
    n = len(matrix)
    diagonals = []

    # Upper diagonals (including main)
    for d in range(n):
        diag = [matrix[i][i+d] for i in range(n-d)]
        diagonals.append(diag)

    # Lower diagonals
    for d in range(1, n):
        diag = [matrix[i+d][i] for i in range(n-d)]
        diagonals.append(diag)

    return diagonals

# ============================================
# 8. SPIRAL TRAVERSAL
# ============================================

def spiral_order(matrix):
    if not matrix:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Right
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # Down
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            # Left
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            # Up
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result

# ============================================
# 9. MATRIX MATH
# ============================================

# Matrix addition
def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]

# Matrix multiplication
def multiply_matrices(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    if cols_A != rows_B:
        raise ValueError("Incompatible dimensions")

    result = [[0] * cols_B for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

# ============================================
# 10. SPECIAL MATRICES
# ============================================

n = 4

# Identity matrix
identity = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

# Zero matrix
zeros = [[0] * n for _ in range(n)]

# Lower triangular
lower = [[1 if i >= j else 0 for j in range(n)] for i in range(n)]

# Upper triangular
upper = [[1 if i <= j else 0 for j in range(n)] for i in range(n)]

# ============================================
# 11. SEARCHING IN 2D
# ============================================

def search_2d(matrix, target):
    """Search in unsorted 2D array - O(m*n)"""
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == target:
                return (i, j)
    return (-1, -1)

def search_sorted_matrix(matrix, target):
    """
    Search in row-wise and column-wise sorted matrix
    Start from top-right corner - O(m+n)
    """
    if not matrix:
        return (-1, -1)

    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1

    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return (row, col)
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1

    return (-1, -1)

# ============================================
# PRACTICE EXERCISES
# ============================================
"""
1. Create a 5x5 matrix where element = row + col
2. Find the sum of each row in a matrix
3. Find the maximum element in each column
4. Check if a matrix is symmetric
5. Implement matrix spiral traversal
"""

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Original:")
    for row in matrix:
        print(row)

    print("\nTransposed:")
    transposed = [list(row) for row in zip(*matrix)]
    for row in transposed:
        print(row)

    print("\nDiagonal:", [matrix[i][i] for i in range(3)])
    print("Spiral:", spiral_order(matrix))
