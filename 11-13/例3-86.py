import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 绘制三维子图
ax = plt.axes(projection='3d')

# 生成测试数据
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-4, 4, 100) * 0.3
r = z**4 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)

# 绘制三维曲线，设置标签
ax.plot(x, y, z, 'rv-', label='参数曲线')

# 设置图例字体、字号，显示图例
plt.rcParams['legend.fontsize'] = 10
ax.legend(prop='simhei')

plt.show()
