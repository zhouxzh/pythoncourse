import numpy as np
import matplotlib.pyplot as plt

r = 20
# 4个圆周的角度，单位为弧度
theta = np.arange(0, 8*np.pi, 0.1)
r = np.arange(20, 20+len(theta))
# 在采样点位置处绘制红色圆圈
plt.plot(r*np.cos(theta), r*np.sin(theta), 'ro')

plt.show()
import numpy as np
import matplotlib.pyplot as plt

x = range(10)
# 10行3列随机数，每个都介于[20,50)区间内
y = np.random.randint(20, 50, (10,3))
# 绘制3条折线图，每列数据对应一条折线图
plt.plot(x, y, label=['a','b','c'])
plt.legend()

plt.show()
