import numpy as np
import matplotlib.pyplot as plt

# 创建极坐标系
ax = plt.subplot(111, polar=True)
theta = np.linspace(0, 2*np.pi, 200)
r = np.sin(6*theta)
ax.plot(theta, r, color='r', lw=3)
# 设置径向网格线，两行代码等价
# ax.set_rgrids(np.arange(-1,1.1,0.5))
ax.set_yticks(np.arange(-1,1.1,0.5))
# 设置角度方向的网格线
ax.set_xticks(np.arange(0, 2*np.pi, 1))
# 不显示最外层网格线
ax.spines['polar'].set_visible(False)
# 关闭所有网格线
# plt.axis('off')
plt.show()
