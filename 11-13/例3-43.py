import numpy as np
import matplotlib.pyplot as plt

# 给定采样点坐标
x = np.arange(-1, 1, 0.1)
y = x + np.random.random(len(x))
# 使用散点图绘制采样点
plt.scatter(x, y, c='b', marker='+')
# 根据给定采样点，使用最小二乘法拟合5次埃尔米特多项式，得到多项式系数
coef = np.polynomial.hermite.hermfit(x, y, 5)
# 根据拟合得到的系数创建埃尔米特多项式
hp = np.polynomial.Hermite(coef, [-1,1])
# 使用折线图绘制拟合得到的5次埃尔米特多项式曲线
# linspace(100)用来在指定的区间中生成100个均匀分布的采样点坐标
plt.plot(*hp.linspace(100), 'r-')

plt.gca().set_aspect('equal')
plt.show()
