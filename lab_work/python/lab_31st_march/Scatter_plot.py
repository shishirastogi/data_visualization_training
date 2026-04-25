import matplotlib.pyplot as plt
import numpy as np
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 20, 12]

plt.scatter(x, y)
max_index = np.argmax(y)
plt.scatter(x[max_index], y[max_index], color='red', label='Max Point')
plt.legend()
plt.show()