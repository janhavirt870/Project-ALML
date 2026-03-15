print(" AI ")
print("ML")
print("PROJECT")

import numpy as np
num1 = np.arange(5)
print("1D array:")
print(num1)
num2 = np.arange(10).reshape(2, 5)
print("\n2D array:")
print(num2)
# Combine 1-D and 2-D arrays
for a, b in np.nditer([num1, num2]):
    print("%d:%d" % (a, b))