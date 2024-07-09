import numpy as np
import matplotlib.pyplot as plt

# 外接圆半径
r = 6
angles = np.linspace(0, 2*np.pi, 5,
                     endpoint=False)
x = r * np.cos(angles)
y = r * np.sin(angles)

plt.plot([x[2],x[0],x[3],x[1],x[4],x[2]],
         [y[2],y[0],y[3],y[1],y[4],y[2]],
         'r')
# 设置坐标轴纵横比相等
plt.gca().set_aspect('equal')
plt.show()
