import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 500)     # 创建自变量数组
y1 = np.sin(x)                       # 创建函数值数组
y2 = np.cos(x)
y3 = np.sin(x*x)

plt.figure()                         # 创建图形
ax1 = plt.subplot(2,                 # 把绘图区域切分为两行
                  2,                 # 把绘图区域切分为两列
                  1)                 # 选择两行两列的第一个区域
ax2 = plt.subplot(2,2,2)             # 选择两行两列的第二个区域
ax3 = plt.subplot(212,               # 把绘图区域切分为两行一列
                                     # 选择两行一列的第二个区域
                  facecolor='y')     # 设置背景颜色为黄色
plt.sca(ax1)                         # 选择ax1
plt.plot(x, y1, color='red')         # 绘制红色曲线
plt.ylim(-1.2, 1.2)                  # 限制y坐标轴范围

plt.sca(ax2)                         # 选择ax2
plt.plot(x, y2, 'b--')               # 绘制蓝色虚线
plt.ylim(-1.2, 1.2)

plt.sca(ax3)
plt.plot(x, y3, 'g--')
plt.ylim(-1.2, 1.2)

plt.show()
