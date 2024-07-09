import numpy as np
import matplotlib.pyplot as plt

x, y = np.mgrid[0:50:80j, 0:50:80j]
c = np.sin(x**2-y**2)
plt.pcolormesh(x, y, c, shading='nearest',
               edgecolors='b', alpha=0.7)
plt.gca().set_aspect('equal')
plt.show()
