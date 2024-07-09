import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import matplotlib.animation as animation

# 创建图形和用来显示波形的轴域
fig = plt.figure(figsize=(10,5))
ax = fig.add_axes(rect=(0.05,0.2,0.9,0.75))
ax.set_ylim(-2.2, 2.2)
# 绘制三条正弦曲线上的采样点，每个采样点表示一个振动的质子
# 模拟两个波的传播和叠加
# 频率相同、相位差恒定、振动方向相同的两个波叠加时，
# 某些区域的振动总是加强，某些区域的振动总是减弱，这种现象叫干涉
x, y1, y2 = [], [], []
line1, = ax.plot(x, y1, 'bo', markersize=4)
line2, = ax.plot(x, y2, 'ro', markersize=4)
line3, = ax.plot(x, y1+y2, 'ko', markersize=4)
# 绘制一条紫色水平直线，表示所有质子简谐振动的平衡位置
plt.plot([0,4*np.pi], [0,0], 'purple')
# 放置3个滑动块，用来调整两个波的频率和相位差
ax1 = fig.add_axes(rect=(0.05,0.05,0.2,0.1))
slider1 = Slider(ax1, 'freq1', valmin=1, valmax=6,
                 valinit=1, valfmt='%d')
ax2 = fig.add_axes(rect=(0.4,0.05,0.2,0.1))
slider2 = Slider(ax2, 'freq2', valmin=1, valmax=6,
                 valinit=1, valfmt='%d')
ax3 = fig.add_axes(rect=(0.7,0.05,0.2,0.1))
slider3 = Slider(ax3, 'diff', valmin=0, valmax=6, valstep=0.01,
                 valinit=2, valfmt='%.2f')

# 初始化图形，设置动画的初始状态
def init():
    line1.set_data(x, y1)
    line2.set_data(x, y2)
    line3.set_data(x, y1+y2)
    return line1, line2, line3

# 根据滑动块位置设置图形初始状态
def update_slider(event):
    global x, y1, y2, freq1, freq2, diff
    freq1 = int(slider1.val)
    freq2 = int(slider2.val)
    diff = float(slider3.val)
    x = np.arange(0, 4*np.pi, 0.1)
    y1 = np.sin(x*freq1)
    y2 = np.sin(x*freq2+diff)
    init()
slider1.on_changed(update_slider)
slider2.on_changed(update_slider)
slider3.on_changed(update_slider)
update_slider(None)

# 更新图形
def update(offset):
    # 修改相位，模拟质点振动向右传播
    xx = x - offset
    yy1 = np.sin(xx*freq1)
    yy2 = np.sin(xx*freq2+diff)
    line1.set_data(x, yy1)
    line2.set_data(x, yy2)
    line3.set_data(x, yy1+yy2)
    return line1, line2, line3

# 创建并显示动画
anim = animation.FuncAnimation(fig, init_func=init, func=update,
                               frames=np.arange(0,2*np.pi,0.01),
                               interval=20, repeat=True,
                               repeat_delay=50, blit=True)
plt.show()
