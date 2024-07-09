import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

np.random.seed(20220708)
x = np.random.randint(0, 40, 10)
y = np.random.randint(0, 40, 10)
z = 80 * abs(np.sin(x+y))
ax = plt.subplot(projection='3d')

# 依次绘制每个柱
# for xx, yy, zz in zip(x, y, z):
#     color = np.random.random(3)
#     ax.bar3d(xx,
#              yy,
#              0,
#              dx=1,
#              dy=1,
#              dz=zz,
#              color=color)
# 一次绘制多个柱
ax.bar3d(x, y, np.zeros_like(z),
         dx=1, dy=1, dz=z,
         color=np.random.random((10,3)))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
