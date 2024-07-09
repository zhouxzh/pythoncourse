import numpy as np
import matplotlib.pyplot as plt

labels = ('Frogs', 'Cats', 'Dogs', 'Horses')
colors = ('#FF0000', 'yellowgreen', 'gold', 'blue')
explode = (0, 0.02, 0, 0.08)       # 使所有饼状图中第2片和第4片裂开

fig = plt.figure(num=1,            # num为数字表示图像编号，
                                   # 如果是字符串则表示图形窗口标题
                 figsize=(10,8),   # 图形大小，格式为(宽度,高度)
                                   # 单位为英寸
                 dpi=110,          # 分辨率
                 facecolor='white')# 背景色

np.random.seed(20220702)
ax = fig.gca()                     # 获取当前轴域（或子图）
ax.pie(np.random.random(4),        # 4个介于0和1之间的随机数据
       explode=explode,            # 设置每个扇形的裂出情况
       labels=labels,              # 设置每个扇形的标签
       labeldistance=1.2,          # 扇形标签到饼心的距离
       colors=colors,              # 设置每个扇形的颜色
       pctdistance=0.5,            # 设置扇形内百分比文本与中心的距离
       autopct='{:.2f}%'.format,   # 设置每个扇形上百分比文本的格式
       shadow=True,                # 使用阴影，呈现一定的立体感
       startangle=90,              # 设置第一块扇形的起始角度
       radius=0.25,                # 设置饼的半径
       center=(0,0),               # 设置饼在图形窗口中的坐标
       counterclock=False,         # 顺时针绘制，默认是逆时针
       frame=True)                 # 显示图形边框
ax.pie(np.random.random(4), explode=explode, labels=labels,
       labeldistance=1.4, colors=colors, pctdistance=0.5,
       autopct='{:.2f}%'.format, shadow=True,
       startangle=45, radius=0.25, center=(1, 1), frame=True)
ax.pie(np.random.random(4), explode=explode, labels=labels,
       labeldistance=1.2, colors=colors, pctdistance=0.5,
       autopct='{:.2f}%'.format, shadow=True,
       startangle=90, radius=0.25, center=(0, 1), frame=True)
ax.pie(np.random.random(4), explode=explode, labels=labels,
       labeldistance=1.2, colors=colors, pctdistance=0.5,
       autopct='{:.2f}%'.format, shadow=False,
       startangle=135, radius=0.35, center=(1, 0), frame=True)
ax.set_xticks([0, 1])                    # 设置x坐标轴刻度
ax.set_yticks([0, 1])                    # 设置y轴坐标轴刻度

ax.set_xticklabels(['Sunny', 'Cloudy'])  # 设置坐标轴刻度上的标签
ax.set_yticklabels(['Dry', 'Rainy'])

ax.set_xlim((-0.7, 1.7))                 # 设置坐标轴跨度
ax.set_ylim((-0.6, 1.6))

ax.set_aspect('equal')                   # 设置纵横比相等

plt.show()
