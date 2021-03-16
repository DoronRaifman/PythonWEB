import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# fake data
x = np.arange(1.0, 11.0)[::-1]
y = [5,6,7,8,2,5,6,3,7,2]
z = np.zeros(10)
dx = np.ones(10)
dy = np.ones(10)
dz = np.arange(1.0, 11.0)

fig = plt.figure()
ax = Axes3D(fig)
ax.bar3d(x, y, z, dx, dy, dz)
plt.show()
plt.close(fig)

