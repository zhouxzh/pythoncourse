import numpy as np
import matplotlib.pyplot as plt

# 初始速度和加速度
v0, a = 3, 1.8
# 时间轴，第5到20秒
t = np.arange(5, 21)
# 速度
v = v0 + a*t
# 位移
x = v0*t + 0.5*a*t*t
# 创建左右两个子图
fig, (ax1, ax2) = plt.subplots(1, 2)
# 设置子图之间的水平间距，wspace单位为子图宽度的比例
plt.subplots_adjust(wspace=0.5)
# 选择左边子图为当前子图
plt.sca(ax1)
# 在当前子图中绘制折线图
plt.plot(t, v, c='red')
plt.title('时间-速度', fontproperties='STKAITI', fontsize=24)
plt.xlabel('时间（s）', fontproperties='STKAITI', fontsize=18)
plt.ylabel('速度（m/s）', fontproperties='STKAITI', fontsize=18)
# 设置坐标轴刻度范围
plt.xlim(5, 21)
plt.ylim(0, 40)

# 选择右边子图为当前子图
plt.sca(ax2)
# 在当前子图中绘制折线图
plt.plot(t, x, c='blue')
plt.title('时间-位移', fontproperties='STKAITI', fontsize=24)
plt.xlabel('时间（s）', fontproperties='STKAITI', fontsize=18)
plt.ylabel('位移（m）', fontproperties='STKAITI', fontsize=18)
plt.xlim(5, 21)
plt.ylim(0, 450)

plt.show()
