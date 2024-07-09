import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 6*np.pi, 0.05)
# 连续信号与数字信号的函数值
t_sin = np.sin(t)
t_digital1 = np.piecewise(t_sin, [t_sin>0, t_sin<0], [1,-1])
t_digital2 = np.round_(t_sin)

plt.plot(t, t_sin, label='$sin(x)$', color='red', lw=1)
plt.plot(t, t_digital1, 'b--', label='digital1')
plt.plot(t, t_digital2, 'g-.', label='digital2')
plt.ylim(-2.0, 2.0)
plt.legend()

plt.show()
