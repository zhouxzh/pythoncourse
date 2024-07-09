import numpy as np
import matplotlib.pyplot as plt

# 生成模拟数据
x = np.arange(0.0, 4.0*np.pi, 0.01)
y = np.sin(x)

# 绘制正弦曲线
plt.plot(x, y)
# 绘制基准水平直线
plt.plot((x.min(),x.max()), (0,0), 'r', lw=2)
# 设置坐标轴标签
plt.xlabel('x')
plt.ylabel('y')
# 填充指定区间内的曲线与x轴包围的区域
plt.fill_between(x, y,
                 where=(2.3<x) & (x<4.3) | (x>10),
                 facecolor='purple')
# 可以填充多次
plt.fill_between(x, y,
                 where=(7<x) & (x<8),
                 facecolor='green')

plt.show()
