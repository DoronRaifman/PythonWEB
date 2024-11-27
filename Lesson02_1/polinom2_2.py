import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
plt.suptitle("Parabula y = ax^2 +bx + c", size=30)
a = 1
for b in range(10):
    x = np.arange(-10, 10)
    y = a * x ** 2 + b * x
    plt.plot(x, y, label=f"a=1, x={b}")
plt.xlabel('x', size=20)
plt.ylabel('y', size=20)
plt.legend()

plt.show()
plt.close(fig)

