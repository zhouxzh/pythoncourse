import numpy as np
import matplotlib.pyplot as plt

y = np.arange(8)
x = y + 3

# 绘制左右对称的两组柱状图
plt.barh(y, -x, color='#ff000088')
plt.barh(y, x, color='#0000ff88')
plt.xlim(-10, 10)

plt.show()
