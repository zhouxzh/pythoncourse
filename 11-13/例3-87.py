import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 单条三次Bezier曲线的4个控制点
P0, P1, P2, P3 = ((40, 20, -30), (50, 130, 10),
                  (120, 150, 0), (245, 30, 30))
# 参数取值范围
t = np.arange(0, 1, 0.01)
# Bernstein多项式，三次Bezier曲线的调和函数
a0 = (1-t) ** 3
a1 = 3 * (1-t)**2 * t
a2 = 3 * t**2 * (1-t)
a3 = t ** 3
# 三次Bezier曲线上与参数t对应的点
x = a0*P0[0] + a1*P1[0] + a2*P2[0] + a3*P3[0]
y = a0*P0[1] + a1*P1[1] + a2*P2[1] + a3*P3[1]
z = a0*P0[2] + a1*P2[1] + a3*P2[2] + a3*P3[2]

# 绘制三维曲线
ax = plt.axes(projection='3d')
ax.plot(x, y, z, lw=2, c='r')
ax.set_xlabel('X', labelpad=5)
ax.set_ylabel('Y', labelpad=5)
ax.set_zlabel('Z', labelpad=5)
ax.set_title('Bezier Curve')
plt.tight_layout()

plt.show()
