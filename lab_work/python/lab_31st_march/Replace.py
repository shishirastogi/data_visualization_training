import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
print(arr)
arr[arr % 2 == 1] = -1
print(arr)