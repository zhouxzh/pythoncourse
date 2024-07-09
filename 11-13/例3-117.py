from itertools import cycle
import matplotlib.pyplot as plt

# 存储鼠标依次单击的位置
x, y = [], []
# 可用颜色和当前颜色
colors = cycle('rgbcmyk')
color = next(colors)

def on_mouse_click(event):
    global color
    if event.button == 1:
        # 单击鼠标左键，绘制新直线连接最后两个点
        x.append(event.xdata)
        y.append(event.ydata)
        if len(x) > 1:
            plt.plot(x[-2:], y[-2:], c=color, lw=2)
        plt.xticks(range(10))
        plt.yticks(range(10))
    elif event.button == 3:
        # 单击鼠标右键，切换颜色
        color = next(colors)
    elif event.button == 2:
        # 单击鼠标中键，删除最后绘制的一个线条
        if ax.lines:
            ax.lines.remove(ax.lines[-1])
            del x[-1], y[-1]
    event.canvas.draw()
        
def on_close(event):
    print('closed')

def on_clear(event):
    # 按下键盘上的c，清除所有端点和已绘制图形
    if event.key == 'c':
        ax.lines.clear()
        del x[:], y[:]
        # 更新图形画布
        event.canvas.draw()

fig = plt.figure()
ax = plt.gca()
plt.xticks(range(10))
plt.yticks(range(10))
fig.canvas.mpl_connect('button_press_event', on_mouse_click)
fig.canvas.mpl_connect('key_press_event', on_clear)
fig.canvas.mpl_connect('close_event', on_close)
plt.show()
