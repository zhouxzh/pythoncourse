import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

def circleXY(r=20, sideNum=6):
    theta = np.linspace(0, 2*np.pi,  # 绘制一个完整的圆
                        sideNum+1,   # 顶点数量
                        True)        # 划分角度时包含终点
    x = r * np.cos(theta)            # 圆周上点的x坐标
    y = r * np.sin(theta)            # 圆周上点的y坐标
    return (x, y)

fig, ax = plt.subplots()             # 创建图形和轴域
plt.subplots_adjust(bottom=0.25)

x, y = circleXY()
line, = plt.plot(x, y, lw=2,         # 绘制折线图形成闭合多边形
                 color='red')        # 设置线宽和颜色

axColor = 'lightgoldenrodyellow'
# 创建子图
# 然后在其中创建Slider组件，设置位置/尺寸、背景色和初始值
axSideNum = plt.axes([0.2, 0.15, 0.6, 0.03],
                     facecolor=axColor) 
slideSideNum = Slider(axSideNum, 'side number',
                      valmin=3, valmax=60,   # 最小值、最大值
                      valinit=6,             # 默认值
                      valfmt='%d')           # 数字显示格式
axRadius = plt.axes([0.2, 0.085, 0.6, 0.03],
                    facecolor=axColor) 
slideRadius = Slider(axRadius, 'Radius',
                     valmin=10, valmax=40,
                     valinit=20, valfmt='%d')

# 为Slider组件设置事件处理函数
def update(event):
    sideNum = int(slideSideNum.val)       # 获取Slider组件的当前值
    r = int(slideRadius.val)              # 获取半径大小
    x, y = circleXY(r=r, sideNum=sideNum) # 重新计算圆周上点的坐标
    line.set_data(x, y)                   # 更新数据
    plt.draw()                            # 重新绘制多边形
slideSideNum.on_changed(update)
slideRadius.on_changed(update)

# 创建按钮组件，用来恢复Slider组件的初始值
resetax = plt.axes([0.45, 0.03, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axColor,
                hovercolor='yellow')
def reset(event):
    slideSideNum.reset()
    slideRadius.reset()
button.on_clicked(reset)

ax.set_aspect('equal')
ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)
plt.show()
