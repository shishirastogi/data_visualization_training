import numpy as np
arr = np.random.rand(10)

normalized = (arr - arr.min()) / (arr.max() - arr.min())

print("Original Array:")
print(arr)

print("\nNormalized Array:")
print(normalized)