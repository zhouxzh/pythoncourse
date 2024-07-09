import numpy as np
import matplotlib.pyplot as plt

# 生成模拟数据
x = np.arange(0.0, 4.0*np.pi, 0.01)
y = np.sin(x)
z = np.cos(x)

# 绘制正弦曲线
plt.plot(x, y, 'r', lw=2)
plt.plot(x, z, 'g', lw=2)
# 绘制基准水平直线
plt.plot((x.min(),x.max()), (0,0))
# 设置坐标轴标签
plt.xlabel('x')
plt.ylabel('y')

# 填充两条曲线之间包围的部分
plt.fill_between(x, y, z, facecolor='purple', hatch='o')

plt.show()
