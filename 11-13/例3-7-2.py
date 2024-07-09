import numpy as np
import matplotlib.pyplot as plt

# 外接圆半径
r = 6
angles = np.linspace(0, 4*np.pi, 6)
x = r * np.sin(angles)
y = r * np.cos(angles)

plt.plot(x, y, 'r')
# 设置坐标轴纵横比相等
plt.gca().set_aspect('equal')
plt.show()
