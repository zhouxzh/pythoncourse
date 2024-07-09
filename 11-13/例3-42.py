import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = 'stkaiti'
np.random.seed(20220702)
x = np.arange(0, 150, 10)
y = x + np.random.randint(-40, 40, len(x))
# 根据原始数据绘制散点图
plt.scatter(x, y, c='b', s=100, marker='*', label='原始数据')

# 使用1次多项式拟合，返回多项式系数
p = np.polyfit(x, y, 1)
# poly1d()根据给定的系数创建多项式，然后计算多项式的值
plt.plot(x, np.poly1d(p)(x), 'r--', lw=2, label='1次多项式拟合')
# 使用7次多项式拟合
p = np.polyfit(x, y, 7)
plt.plot(x, np.poly1d(p)(x), 'c-.', lw=2, label='7次多项式拟合')
# 使用14次多项式拟合
p = np.polyfit(x, y, 14)
plt.plot(x, np.poly1d(p)(x), 'g-', lw=2, label='14次多项式拟合')
plt.legend()
plt.show()
