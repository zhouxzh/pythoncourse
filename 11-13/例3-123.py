import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)
t = np.arange(0.0, 1.0, 0.001)

# 初始振幅与频率，并绘制初始图形
a0, f0 = 5, 3
s = a0*np.sin(2*np.pi*f0*t)
line, = plt.plot(t, s, lw=2, color='red')
# 设置坐标轴刻度范围，参数含义为[xmin, xmax, ymin, ymax]
plt.axis([0, 1, -10, 10])

axColor = 'lightgoldenrodyellow'
# 创建两个Slider组件，分别设置位置/尺寸、背景色和初始值
axfreq = plt.axes([0.1, 0.1, 0.75, 0.03], facecolor=axColor)
sfreq = Slider(axfreq, 'Freq', 0.1, 30.0, valinit=f0)
axamp = plt.axes([0.1, 0.15, 0.75, 0.03], facecolor=axColor)
samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=a0)

# 为Slider组件设置事件处理函数
def update(event):
    # 获取两个Slider组件的当前值，并以此来更新图形
    amp = samp.val
    freq = sfreq.val
    line.set_ydata(amp*np.sin(2*np.pi*freq*t))
    plt.draw()
sfreq.on_changed(update)
samp.on_changed(update)

# 增加两个Slider的值，自动调整曲线形状
def adjustSliderValue(event):
    samp.set_val((samp.val+0.05) % 10)
    sfreq.set_val((sfreq.val+0.5) % 30)
    update(event)
axAdjust = plt.axes([0.6, 0.025, 0.1, 0.04])
buttonAdjust = Button(axAdjust, 'Adjust', color=axColor,
                      hovercolor='red')
buttonAdjust.on_clicked(adjustSliderValue)

# 创建按钮组件，用来恢复初始值
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axColor,
                hovercolor='yellow')
def reset(event):
    sfreq.reset()
    samp.reset()
button.on_clicked(reset)

plt.show()
