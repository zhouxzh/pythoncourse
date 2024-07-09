import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 20, 0.05)
data = np.sin(t*20) + np.cos(t)

_, (ax1, ax2) = plt.subplots(nrows=2)
# 绘制原始数据图像
ax1.plot(t, data)
# 计算并绘制相位谱
ax2.phase_spectrum(data)
plt.suptitle('原始数据与相位谱', fontproperties='simhei', fontsize=20)
plt.show()
