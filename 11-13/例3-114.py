import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = x ** 2
# y = np.sin(6*x)
_, axes = plt.subplots(2, 3)
axes.shape = (6,)
for ax in axes:
    ax.plot(x, y)
# 默认坐标轴缩放类型为线性
axes[0].set_title('linear')
# 设置轴缩放比例类型
# symlog是symmetric log的缩写
axes[1].set_xscale('symlog')
axes[1].set_title('symlog')
axes[2].set_xscale('logit')
axes[2].set_title('logit')
axes[3].set_xscale('log')
axes[3].set_title('log')
# functions参数含义为(forward, inverse)
axes[4].set_xscale('function',
                   functions=[lambda v: 4*v, lambda v: 0.5*v])
axes[4].set_title('function')
axes[5].set_yscale('functionlog',
                   functions=[lambda v: v**2, lambda v: 10*v])
axes[5].set_title('functionlog')
plt.suptitle('y = x**2', fontsize=16)
# plt.suptitle('y = np.sin(6*x)', fontsize=16)
plt.show()
