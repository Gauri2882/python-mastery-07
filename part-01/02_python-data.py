""" Handling user input for matrices """

import numpy as np

# function to create matrix from user input
def get_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    print("Enter the matrix elements row by row:")
    elements = []
    for _ in range(rows):
        row = list(map(float, input().split()))
        elements.append(row)
    return np.array(elements)

# example usage
matrix = get_matrix()
print("Matrix:\n", matrix)