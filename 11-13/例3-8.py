import numpy as np
import matplotlib.pyplot as plt

r = 6
angles = np.arange(0, np.pi*2, 0.01)
# 把4改成其他数字可以得到不同图案
x = r * np.cos(4*angles) * np.cos(angles)
y = r * np.cos(4*angles) * np.sin(angles)
plt.plot(x, y, 'r')

# 设置坐标轴纵横比相等
plt.gca().set_aspect('equal')
# 显示图形
plt.show()
