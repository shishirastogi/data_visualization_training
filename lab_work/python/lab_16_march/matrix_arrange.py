import numpy as np
arr = np.arange(1, 11)
arr[arr % 2 == 0] = 0

print(arr)