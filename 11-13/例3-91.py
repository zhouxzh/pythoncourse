import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

x, y = np.mgrid[-2:2:20j, -2:2:20j]
z = x*x - y*y

ax = plt.subplot(111, projection='3d')
ax.plot_surface(x, y, z,
                rstride=1, cstride=1,
                cmap=plt.cm.coolwarm)
plt.show()
