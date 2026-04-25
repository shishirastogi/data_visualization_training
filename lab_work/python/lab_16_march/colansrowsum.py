import numpy as np
matrix = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12],[13,14,15,16]])

row_sum = matrix.sum(axis=1)
col_sum = matrix.sum(axis=0)

print("Row Sum:")
print(row_sum)

print("\nColumn Sum:")
print(col_sum)