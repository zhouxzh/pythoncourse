import numpy as np

def numpy_pi(times):
    x = np.random.rand(times)        # 第一象限随机点的x坐标，[0,1)区间
    y = np.random.rand(times)        # 第一象限随机点的y坐标，[0,1)区间
    hits = np.sum(x**2+y**2 <= 1)    # 落在四分之一单位圆周及内部的点的数量
    pi = hits / times * 4             # 圆周率近似值
    return pi

print(numpy_pi(10000))
print(numpy_pi(100000))
print(numpy_pi(100000000))
