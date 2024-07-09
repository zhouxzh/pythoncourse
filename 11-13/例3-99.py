import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-2*np.pi, 2*np.pi, 40)
y1 = np.exp(x1)
x2 = np.linspace(-2*np.pi, 2*np.pi, 100)
y2 = np.sin(x2) ** 2

fig = plt.figure()
ax1 = fig.gca()
ax1.set_xlabel('x')
s = ax1.scatter(x1, y1, color='red', marker='*')
ax1.set_ylabel('exp(x)', color='red')
# 设置y轴刻度标签颜色为红色
ax1.tick_params(axis='y', labelcolor='red')

# 创建新轴域，与ax1共享x轴
ax2 = ax1.twinx()
line, = ax2.plot(x2, y2, color='#0099ff')
ax2.set_ylabel('$sin^2(x)$', color='#0099ff')
# 设置y轴刻度标签颜色
ax2.tick_params(axis='y', labelcolor='#0099ff')
# 如果通过fig调用legend()，图例会放在图形窗口的左上角，而不是轴域的左上角
plt.legend([s,line], ['exp', 'sin^2'], loc='upper left')

plt.show()
