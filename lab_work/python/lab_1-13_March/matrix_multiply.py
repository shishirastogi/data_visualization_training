import numpy as np
A, B = np.arange(1, 10).reshape(3, 3), np.arange(9, 0, -1).reshape(3, 3)
print(A @ B)