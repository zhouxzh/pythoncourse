import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 500)
y = np.sinc(x)
z = np.cos(x*x)
plt.figure(figsize=(8,4))

plt.plot(x,                  # x轴数据
         y,                  # y轴数据
         label='$sinc(x)$',  # 把标签渲染为公式
         color='red',        # 红色
         linewidth=2)        # 线宽为2个像素
plt.plot(x, z,
         'b--',              # 蓝色虚线
         label='$cos(x^2)$') # 把标签渲染为公式

plt.xlabel('Time(s)')
plt.ylabel('Volt')
plt.title('Sinc and Cos figure using pyplot')
plt.ylim(-1.2, 1.2)
plt.legend()
plt.show()
