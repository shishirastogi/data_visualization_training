import numpy as np
arr = np.array([1, 3, 5, 7, 9])
value = 4

indices = np.where(arr > value)[0]
print(indices)