import numpy as np
a = np.arange(1, 11)
print(np.where(a % 2 == 0, 0, a))