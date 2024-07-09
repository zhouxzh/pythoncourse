import numpy as np
import matplotlib.pyplot as plt

x, y = np.mgrid[-3:3:256j, -3:3:256j]
z = (1-x/2+x**3+y**2) * np.exp(-x**2-y**2)
ct = plt.contour(x, y, z)
plt.colorbar(ct)
plt.clabel(ct, fontsize=14, colors='r')

plt.show()
