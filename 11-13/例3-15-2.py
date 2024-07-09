import numpy as np
import matplotlib.pyplot as plt

# 函数自变量取值范围区间
start, end = 0, 10
# 计算所有采样点的x坐标、y坐标，绘制折线图
x = np.arange(start, end, 0.01)
y = 3*np.sin(x) + 5*np.cos(3*x)
s, = plt.plot(x, y, 'r-')

for index, yy in enumerate(y):
    if index == 0:
        if yy > y[1]:
            s1 = plt.scatter(x[index], yy, marker='*', c='b')
        elif yy < y[1]:
            s2 = plt.scatter(x[index], yy, marker='*', c='g')
    elif index == len(y)-1:
        if yy > y[index-1]:
            s1 = plt.scatter(x[index], yy, marker='*', c='b')
        elif yy < y[index-1]:
            s2 = plt.scatter(x[index], yy, marker='*', c='g')
    elif yy>=y[index-1] and yy>=y[index+1]:
        s1 = plt.scatter(x[index], yy, marker='*', c='b')
    elif yy<=y[index-1] and yy<=y[index+1]:
        s2 = plt.scatter(x[index], yy, marker='*', c='g')

# 创建图例
plt.legend([s,s1,s2], ['curve','local max','local min'])
#显示绘制的结果
plt.show()
