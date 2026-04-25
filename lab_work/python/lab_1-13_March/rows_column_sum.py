import numpy as np
m = np.arange(1, 17).reshape(4, 4)
print(f"Row Sum: {m.sum(1)}\nCol Sum: {m.sum(0)}")