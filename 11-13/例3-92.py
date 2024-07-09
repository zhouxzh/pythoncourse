import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

# 4行4列控制点坐标
control_points = (((-2,-2,-4), (-1,-2,4), (1,-2,-4), (2,-2,-4)),
                  ((-2,-1,-1), (-1,-1,-1), (1,-1,-1), (2,-1,-1)),
                  ((-2,1,1), (-1,1,1), (1,1,1), (2,1,1)),
                  ((-2,2,4), (-1,2,-4), (1,2,4), (2,2,4)))
# 两个方向的参数取值范围
u, v = np.mgrid[0:1:30j, 0:1:30j]
# 调和函数的值
biu = ((1-u) ** 3, 3 * (1-u)**2 * u, 3 * u**2 * (1-u), u ** 3)
bjv = ((1-v) ** 3, 3 * (1-v)**2 * v, 3 * v**2 * (1-v), v ** 3)
x = np.zeros_like(u)
y = np.zeros_like(u)
z = np.zeros_like(u)
# 计算网格点坐标
for i, row in enumerate(control_points):
    for j, point in enumerate(row):
        x = x + point[0] * biu[i] * bjv[j]
        y = y + point[1] * biu[i] * bjv[j]
        z = z + point[2] * biu[i] * bjv[j]
# 创建三维子图，绘制贝塞尔曲面
ax = plt.subplot(111, projection='3d')
ax.plot_surface(x, y, z)

plt.show()
