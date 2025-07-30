""" Matrix operations with NumPy """

import numpy as np

# create a 2x2 matrix
matrix = np.array([[1, 2], [3, 4]])
print(matrix)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# addition
print("Addition:\n", A + B)

# subtraction
print("Subtraction:\n", A - B)

# multiplication
print("Multiplication element wise:\n ", A * B)

# dot product
print("Dot product:\n", np.dot(A, B))

# transpose
print("Transpose of A: \n", A.T)

# determinant
det = np.linalg.det(A)
print("Determinants:\n", det)

# inverse
if det != 0:
    inverse = np.linalg.inv(A)
    print("Inverse:\n", inverse)
else:
    print("Matrix is not invertible")
