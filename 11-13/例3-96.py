import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

# 生成测试数据
np.random.seed(20220709)
x = np.random.randint(0, 40, 30)
y = np.random.randint(0, 40, 30)
z = np.random.randint(0, 40, 30)

# 创建三维图形
ax = plt.subplot(projection='3d')
# 绘制三维散点图
# 逐个散点绘制
##for xx, yy, zz in zip(x, y, z):
##    color = 'r'
##    if 10<zz<20:
##        color = 'b'
##    elif zz>=20:
##        color = 'g'
##    ax.scatter(xx, yy, zz, c=color, marker='*',
##               s=160, linewidth=1, edgecolor='b')
# 生成指定颜色
color = np.empty((len(z),3))
color[z<=10] = (1,0,0)
color[(z>10)&(z<20)] = (0,1,0)
color[z>=20] = (0,0,1)
# 生成颜色的另一种方法
##color = np.piecewise(z, [z<10, (z>=10)&(z<20), z>20], [0,1,2])
# 一次绘制所有散点
ax.scatter(x, y, z, c=color, marker='*',  s=160,
           linewidth=1, edgecolor='b')

# 设置坐标轴标签和图形标题
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('三维散点图', fontproperties='simhei', fontsize=24)

plt.show()
