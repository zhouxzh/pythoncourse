import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
# 绘制正弦曲线
plt.plot(x, y, 'r-', lw=2, label='sin')
# 在纵坐标-0.5和0.5处绘制两条水平直线，蓝色虚线
plt.axhline(-0.5, color='blue', ls='--', label='axhline')
plt.axhline(0.5, color='blue', ls='--')
# 在横坐标绘制垂直直线，绿色点划线
plt.axvline(np.pi, color='green', ls='-.', label='axvline')
# 设置y轴刻度位置和文本
plt.yticks([-1, -0.5, 0, 0.5, 1],
           ['-1', 'axhline', '0', 'axhline', '1'])
# 创建、显示图例
plt.legend()

plt.show()
