from copy import deepcopy
from numpy import linspace, sin, absolute, pi
from numpy.fft import fft, ifft, fftfreq
import matplotlib.pyplot as plt

t = linspace(0, 2*pi, 500)
s1 = 30*sin(1*2*pi*t)
s2 = 10*sin(3*2*pi*t)
s3 = sin(5*2*pi*t)
s4 = s1 + s2 + s3
s5 = s1 + s3

# 离散傅里叶变换采样频率
w = fftfreq(t.size, d=t[1]-t[0])
# 计算每个信号的傅里叶变换
s1_fft = fft(s1)
s2_fft = fft(s2)
s3_fft = fft(s3)
s4_fft = fft(s4)
# 在s4_fft的基础上进行带通滤波得到s5_fft
# 滤除频率介于(2.5,3.5)区间的信号，也就是s2的数据
# 目的是对比滤波后信号与时域信号叠加的相似度
s5_fft = deepcopy(s4_fft)
s5_fft[(absolute(w)>2.5)&(absolute(w)<3.5)] = 0

s1_ifft = ifft(s1_fft)
s2_ifft = ifft(s2_fft)
s3_ifft = ifft(s3_fft)
s4_ifft = ifft(s4_fft)
s5_ifft = ifft(s5_fft)

# 5行3列15个轴域，设置相邻轴域之间的水平距离和垂直距离
fig = plt.figure(figsize=(16,9))
axs = fig.subplots(5, 3)
plt.tight_layout()
plt.subplots_adjust(wspace=0.15, hspace=0.2)
# 每一行3个轴域分别绘制原始信号图像、傅里叶变换频谱、
# 以及傅里叶反变换还原的信号图像
axs[0,0].plot(t, s1, color='r')
axs[0,1].plot(w, s1_fft.real, color='r')
axs[0,2].plot(t, s1_ifft.real, color='r')

axs[1,0].plot(t, s2, color='g')
axs[1,1].plot(w, s2_fft.real, color='g')
axs[1,2].plot(t, s2_ifft.real, color='g')

axs[2,0].plot(t, s3, color='b')
axs[2,1].plot(w, s3_fft.real, color='b')
axs[2,2].plot(t, s3_ifft.real, color='b')

axs[3,0].plot(t, s4, color='k')
axs[3,1].plot(w, s4_fft.real, color='k')
axs[3,2].plot(t, s4_ifft.real, color='k')

axs[4,0].plot(t, s5, color='y')
axs[4,1].plot(w, s5_fft.real, color='y')
axs[4,2].plot(t, s5_ifft.real, color='y')

plt.savefig('fft.jpg', dpi=480)
