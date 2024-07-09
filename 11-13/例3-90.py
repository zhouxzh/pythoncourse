import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

# 两个电荷分别位于(x1,0)和(x2,0)坐标
x1, x2 = -20, 20
# 两个电荷分别带Q和-Q的电量
Q = 600

x, y = np.mgrid[-50:50:50j, -50:50:50j]
# 计算x、y坐标位置的电位
z = Q*(1/(((x+x1)**2+y**2)**0.5)-1/(((x+x2)**2+y**2)**0.5))

ax = plt.subplot(projection='3d')
ax.plot_surface(x, y, z)

plt.show()
