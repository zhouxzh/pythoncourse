import numpy as np
import matplotlib.pyplot as plt

# 函数自变量取值范围区间
start, end = 0, 10
# 计算所有采样点的x坐标、y坐标，绘制折线图
x = np.arange(start, end, 0.01)
y = 3*np.sin(x) + 5*np.cos(3*x)
s, = plt.plot(x, y, 'r-')
# 设置子区间长度，在每个子区间（不包含端点）内寻找极值
# 调整区间大小时会影响极值数量，应使得每个子区间内都包含波峰和波谷
span = 66

for start in range(0, len(y), span):
    # 每个子区间的自变量与函数值
    sectionY = y[start:start+span]
    sectionX = x[start:start+span]
    # 局部最大值和局部最小值
    localMax = sectionY.max()
    localMin = sectionY.min()

    # 方案一：
    # 按值大小升序排序的索引
    argsort_result = sectionY.argsort()
    # 区间内所有最大值的索引和所有最小值的索引
    args_max = argsort_result[-len(sectionY[sectionY==localMax]):]
    args_min = argsort_result[:len(sectionY[sectionY==localMin])]
    # 去除子区间端点
    args_max = list(set(args_max)-{0,span-1})
    if args_max:
        s1 = plt.scatter(sectionX[args_max], sectionY[args_max], marker='*', c='b')
    
    args_min = list(set(args_min)-{0,span-1})
    if args_min:
        s2 = plt.scatter(sectionX[args_min], sectionY[args_min], marker='*', c='g')

    # 方案二：
##    for index, yy in enumerate(sectionY):
##        if yy==localMax and index not in (0, span-1):
##            # 在极大值处绘制一个蓝色五角星
##            s1 = plt.scatter(sectionX[index], yy, marker='*', c='b')
##        elif yy==localMin and index not in (0, span-1):
##            # 在极小值处绘制一个绿色五角星
##            s2 = plt.scatter(sectionX[index], yy, marker='*', c='g')

# 创建图例
plt.legend([s,s1,s2], ['curve','local max','local min'])
#显示绘制的结果
plt.show()
