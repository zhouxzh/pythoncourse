import warnings
import numpy as np
import matplotlib.pyplot as plt

# 忽略警告信息
# warnings.filterwarnings('ignore', '.*GUI is implemented.*')

# 测试数据
x = np.arange(1, 13)
y = np.random.randint(1, 30, 12)
for i in range(24):
    # 清除当前轴域
    plt.cla()
    # 按每个月的数值升序排序
    temp = sorted(zip(x,y), key=lambda item:item[1])
    x = [item[0] for item in temp]
    y = [item[1] for item in temp]
    # 重新绘制水平柱状图
    plt.barh(range(1,13), y)
    plt.title(f'20{i:02d}年', fontproperties='simhei',
              fontsize=20)
    plt.yticks(range(1,13), list(map(lambda i: f'{i}月', x)),
               fontproperties='simhei')
    plt.xticks(range(0,160,20))
    for xx, yy in zip(range(1,13), y):
        plt.text(yy+0.1, xx-0.1, str(yy))
    # 暂停1秒
    plt.pause(1)
    # 更新数据
    y = y + np.random.randint(0, 10, 12)
    
plt.show()
