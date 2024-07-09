import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 20, 0.05)
s1 = np.sin(200*t)
s2 = np.sin(200*t) + np.cos(t)

# 创建图形和两个子图
_, (ax1, ax2) = plt.subplots(nrows=2)
# 同时绘制两条折线图，返回列表，在右下角显示图例
lines = ax1.plot(t, s1, t, s2)
ax1.legend(lines, ['s1', 's2'], loc='lower right')
# 绘制互谱密度
ax2.csd(s1, s2,
        # 每个用来计算FFT的块中数据点数量，默认值为256
        NFFT=32,
        Fs=8,   # 采样频率，默认值为2
        # 用来在每段数据计算FFT之前删除均值或线性趋势
        # 可用的值有'none','mean','linear'，默认值为'none'
        detrend='mean',
        # 每个块之间重叠的数据点数，默认值为0表示相邻块之间不重叠
        noverlap=2, 
        Fc=5,   # 结果图形中的频率中心，用来调整图形中x轴刻度范围
        )
plt.suptitle('原始数据与互谱密度', fontproperties='simhei', fontsize=20)
plt.show()
