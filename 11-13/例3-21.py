import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 20, 0.0005)
s1 = np.sin(2*np.pi*100*t)
s2 = 2 * np.sin(2*np.pi*400*t)
s2[(t<=10)|(t>=12)] = 0
# 设置随机数种子，使得运行结果可再现
np.random.seed(1650933454)
data = s1 + s2 + np.random.random(len(t))/100

_, (ax1, ax2) = plt.subplots(nrows=2)
# 数据点密集到一定程度，折线图呈现出矩形的图案
ax1.plot(t, data)
# 计算并绘制频谱
ax2.specgram(data,
             # 用来计算FFT的每个块中数据点数量，默认值为256
             NFFT=1024,
             Fs=8,   # 采样频率，默认值为2
             # 用来在每段数据计算FFT之前删除均值或线性趋势
             # 可用的值有'none','mean','linear'，默认值为'none'
             detrend='mean',
             # 每个块之间重叠的数据点数，默认值为0表示相邻块之间不重叠
             noverlap=2,
             Fc=5,   # 结果图形中的频率中心，用来调整图形中x轴刻度范围
             )
plt.suptitle('原始数据与频谱', fontproperties='simhei', fontsize=20)
plt.show()
