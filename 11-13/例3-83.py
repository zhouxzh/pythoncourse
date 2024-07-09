import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker, cm

x, y = np.mgrid[-3:3:100j, -2:2:100j]

# 以自然常数e为底的幂运算
z = np.exp(x**2 - y**2)

fig, ax = plt.subplots()
# contourf()填充，contour()不填充
cs = ax.contourf(x, y, z,
                 locator=ticker.LogLocator(),
                 cmap=cm.PuBu_r)
# 添加颜色条
cbar = fig.colorbar(cs)
# 添加标签
plt.clabel(cs, fontsize=14, colors='r')
plt.show()
