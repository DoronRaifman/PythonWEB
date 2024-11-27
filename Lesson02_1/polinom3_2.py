import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
plt.suptitle("Poly3 y = ax^3 + bx^2+cx+d", size=30)
a = 1
for b in range(10):
    x = np.arange(-10, 10)
    y = a * x ** 3 + b * x ** 2
    plt.plot(x, y, label=f"b={b}")
plt.xlabel('x', size=20)
plt.ylabel('y', size=20)
plt.legend()

plt.show()
plt.close(fig)

