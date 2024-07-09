from time import sleep
from threading import Thread
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

fig, ax = plt.subplots()
# 设置图形显示位置
plt.subplots_adjust(bottom=0.2)

# 实验数据
range_start, range_end, range_step = 0, 1, 0.005
t = np.arange(range_start, range_end, range_step)
s = np.sin(4*np.pi*t)
l, = plt.plot(t, s, lw=2)

# 自定义类，用来封装两个按钮的单击事件处理函数
class ButtonHandler:
    def __init__(self):
        self.flag = False
        self.range_s, self.range_e, self.range_step = 0, 1, 0.005
        
    # 线程函数，用来更新数据并重新绘制图形
    def thread_start(self):
        while self.flag:
            sleep(0.02)
            self.range_s += self.range_step
            self.range_e += self.range_step
            t = np.arange(self.range_s, self.range_e,
                          self.range_step)
            ydata = np.sin(4*np.pi*t)
            # 更新数据
            l.set_ydata(ydata)
            # 重新绘制图形
            plt.draw()
            
    def start(self, event):
        if not self.flag:
            self.flag = True
            # 创建并启动新线程
            Thread(target=self.thread_start).start()
        
    def stop(self, event):
        if self.flag:
            self.flag = False

callback = ButtonHandler()

# 创建按钮并设置单击事件处理函数
axStart = plt.axes([0.7, 0.05, 0.1, 0.075])
btnStart = Button(axStart, 'Start', color='0.7', hovercolor='r')
btnStart.on_clicked(callback.start)
axStop = plt.axes([0.81, 0.05, 0.1, 0.075])
btnStop = Button(axStop, 'Stop')
btnStop.on_clicked(callback.stop)

plt.show()
