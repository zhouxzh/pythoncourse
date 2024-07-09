import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

# 生成测试数据
np.random.seed(20220707)
x = np.random.randint(0, 40, 10)
y = np.random.randint(0, 40, 10)
z = 80 * abs(np.sin(x+y))

# 创建三维子图
ax = plt.subplot(projection='3d')
# 绘制三维柱状图
ax.bar3d(x,                 # 设置x轴数据
         y,                 # 设置y轴数据
         np.zeros_like(z),  # 设置柱的z轴起始坐标为0
         dx=1,              # x方向的宽度
         dy=1,              # y方向的厚度
         dz=z,              # z方向的高度
         color='red')       # 设置面片颜色为红色

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
