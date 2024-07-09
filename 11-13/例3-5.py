import numpy as np
import matplotlib.pyplot as plt

x1 = np.arange(0, 2*np.pi, 0.01)
y1 = np.sin(x1)
x2 = np.arange(2*np.pi, 4*np.pi, 0.01)
y2 = np.cos(x2)
# 指定每条曲线的采样点位置和线条属性
lines = plt.plot(x1, y1, 'r-', x2, y2, 'b-.')
# 为两条曲线创建图例
plt.legend(lines, ['sin','cos'])

plt.show()
