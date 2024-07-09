from random import choice
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons, Button

# 3种不同频率的信号
t = np.arange(0.0, 2.0, 0.01)
s0 = np.sin(2*np.pi*t)
s1 = np.sin(4*np.pi*t)
s2 = np.sin(8*np.pi*t)

# 创建图形
fig, ax = plt.subplots()
line, = ax.plot(t, s0, lw=2, color='red')
plt.subplots_adjust(left=0.3)

# 定义几种频率对应的单选钮组件以及事件响应代码
# 其中[0.05, 0.7, 0.15, 0.15]表示组件在窗口上的归一化位置
axcolor = '#886699'
rax = plt.axes([0.05, 0.7, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('2 Hz', '4 Hz', '8 Hz'))
hzdict = {'2 Hz': s0, '4 Hz': s1, '8 Hz': s2}
def freq_func(label):
    ydata = hzdict[label]
    line.set_ydata(ydata)
    fig.canvas.draw()          # 与plt.draw()功能等价
radio.on_clicked(freq_func)

# 定义几种颜色对应的单选钮组件以及事件响应代码
rax = plt.axes([0.05, 0.4, 0.15, 0.15], facecolor=axcolor)
colors = ('red', 'blue', 'green')
radio2 = RadioButtons(rax, colors)
def color_func(label):
    line.set_color(label)
    plt.draw()                 # 重新绘制当前图形
radio2.on_clicked(color_func)

# 定义几种线型对应的单选钮组件
rax = plt.axes([0.05, 0.1, 0.15, 0.15], facecolor=axcolor)
styles = ('-', '--', '-.', ':')
radio3 = RadioButtons(rax, styles)
def style_func(label):
    line.set_linestyle(label)
    plt.draw()
radio3.on_clicked(style_func)

# 定义按钮单击事件处理函数，并在窗口上创建按钮
def random_fig(event):
    # 随机选择一个频率，同时设置单选钮的选中项
    hz = choice(tuple(hzdict.keys()))
    hzLabels = [label.get_text() for label in radio.labels]
    radio.set_active(hzLabels.index(hz))
    line.set_ydata(hzdict[hz])
    
    # 随机选择一个颜色，同时设置单选钮的选中项
    c = choice(colors)
    radio2.set_active(colors.index(c))
    line.set_color(c)
    
    # 随机选择一个线型，同时设置单选钮的选中项
    style = choice(styles)
    radio3.set_active(styles.index(style))
    line.set_linestyle(style)
    
    # 更新图形
    plt.draw()
axRnd = plt.axes([0.5, 0.015, 0.2, 0.045])
buttonRnd = Button(axRnd, 'Random Figure',
                   # 亮度值，'0'表示黑色，'1'表示白色
                   color='0.6',
                   # 鼠标滑过上方时的颜色
                   hovercolor='r')
buttonRnd.on_clicked(random_fig)

plt.show()
