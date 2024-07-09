import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca()

x = np.arange(0, 4*np.pi, 0.3)
y = np.sin(x)
ax.plot(x, y, 'r-*', picker=5)

def onpick(event):
    # 触发事件的图形
    thisline = event.artist
    # 图形上的采样点坐标
    xdata = thisline.get_xdata()
    ydata = thisline.get_ydata()
    # 当前拾取到的当前采样点序号
    ind = event.ind
    points = tuple(zip(xdata[ind], ydata[ind]))
    print(f'顶点编号：{ind[0]}\n坐标：{points}')
fig.canvas.mpl_connect('pick_event', onpick)
plt.show()
