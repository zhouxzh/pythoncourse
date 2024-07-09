import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 演示数据
data = {f'20{i:02d}年': np.random.randint(30, 80, 12)
        for i in range(25)}

# 创建图形和轴域
fig, ax = plt.subplots()
bars = ax.barh(range(1,13), [0]*12)

def init():
    return bars

def update(year):
    # 清除轴域上的图形
    plt.cla()
    # 获取数据，按数值大小排序
    values = data[year]
    temp = sorted(zip(range(1,13), values),
                  key=lambda item:item[1])
    x = [item[0] for item in temp]
    y = [item[1] for item in temp]
    plt.barh(range(1,13), y)    
    plt.title(year, fontproperties='simhei', fontsize=24)
    # 设置坐标轴上显示的标签
    plt.xticks(range(0,101,10))
    plt.yticks(range(1,13),
               [f'{i}月' for i in x],
               fontproperties='simhei',
               fontsize=16)
    # 在水平柱状图右侧显示对应的数值
    for xx, yy in zip(range(1,13),y):
        plt.text(yy+0.1, xx-0.1, str(yy))
    # 重新绘制图形
    plt.draw()
    return bars

ani = FuncAnimation(fig=fig, func=update,
                    frames=data.keys(), init_func=init,
                    interval=500, blit=True)
ani.save('bars.gif', writer='imagemagick')
