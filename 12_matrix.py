# Import numpy
import numpy as np

# 1. Create a 3x3 matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("Original Matrix:")
print(matrix)

# 2. Access elements
print("\nElement at row 2, column 3:", matrix[1, 2])  # Indexing starts from 0

# 3. Slice matrix (get first two rows and first two columns)
sub_matrix = matrix[0:2, 0:2]
print("\nSub-matrix (first 2 rows and columns):")
print(sub_matrix)

# 4. Perform arithmetic operations
print("\nMatrix + 10:")
print(matrix + 10)

print("\nMatrix * 2:")
print(matrix * 2)

# 5. Transpose of the matrix
transpose = matrix.T
print("\nTranspose of the Matrix:")
print(transpose)

# 6. Matrix multiplication (matrix * transpose)
matrix_mult = np.dot(matrix, transpose)
print("\nMatrix multiplied by its Transpose:")
print(matrix_mult)
