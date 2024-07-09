import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

ax = plt.subplot(projection='3d')
# 网格数据的另一种表示形式
x, y = np.ogrid[-4:4:20j, -4:4:20j]
z = np.sin(x) + np.cos(y)
# 自动对x和y进行广播
ax.plot_surface(x, y, z)

plt.show()
