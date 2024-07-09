import numpy as np
import matplotlib.pyplot as plt

# 4个圆周的角度，单位为弧度
theta = np.arange(0, 8*np.pi, 0.1)
r = np.arange(20, 20+len(theta))
# 在采样点位置处绘制红色圆圈
plt.plot(r*np.cos(theta), r*np.sin(theta), 'ro')

plt.show()
