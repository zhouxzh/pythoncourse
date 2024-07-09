from itertools import count
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['axes.labelsize'] = 'larger'

df = pd.DataFrame({'height': [180,170,172,183,179,178,160],
                   'weight': [85,80,85,75,78,78,70]},
                  index=list('一二三四五六七'))
# 创建两个轴域，分别根据一列的数据绘制饼状图
# 默认以DataFrame对象的index作为每个扇形外侧的标签
ax1, ax2 = df.plot(kind='pie', autopct='{:.2f}%'.format, subplots=True, shadow=True)
# 设置轴域中的图形属性，设置扇形外面的文本
index = count(0, 1)
for child in ax1.get_children():
    if isinstance(child, matplotlib.patches.Wedge):
        child.set_label(f'{child.get_label()}-{df.height.values[next(index)]}')
ax1.legend(loc='upper right')

index = count(0, 1)
for child in ax2.get_children():
    if isinstance(child, matplotlib.patches.Wedge):
        child.set_label(f'{child.get_label()}-{df.weight.values[next(index)]}')
ax2.legend(loc='upper left')

plt.show()
