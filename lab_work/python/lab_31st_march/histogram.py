import matplotlib.pyplot as plt
import numpy as np
data = np.random.randint(0, 50, 100)

plt.hist(data, bins=10, color='skyblue', edgecolor='black')
plt.show()