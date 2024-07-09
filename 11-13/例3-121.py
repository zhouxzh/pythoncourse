import numpy as np
import matplotlib.pyplot as plt

# 测试数据
data = {f'20{i:02d}年': np.random.randint(30, 80, 12)
        for i in range(24)}
# 当前轴域
ax = plt.gca()
for year, values in data.items():
    # 清除轴域
    plt.cla()
    # 设置轴域背景色
    ax.set_facecolor(np.random.random(3))
    # 对数据排序，绘制水平柱状图，大数显示在最上面
    temp = sorted(zip(range(1,13),values),
                  key=lambda item:item[1])
    x = [item[0] for item in temp]
    y = [item[1] for item in temp]
    plt.barh(range(1,13), y)
    plt.title(year, fontproperties='simhei', fontsize=24)
    # 设置y轴上显示的标签
    plt.yticks(range(1,13),
               [f'{i}月' for i in x],
               fontproperties='simhei',
               fontsize=16)
    plt.xticks(range(0,101,10))
    # 在水平柱状图右侧显示对应的数值
    for xx, yy in zip(range(1,13), y):
        plt.text(yy+0.1, xx-0.1, str(yy))
    # 暂停1秒
    plt.pause(1)
    
plt.show()
