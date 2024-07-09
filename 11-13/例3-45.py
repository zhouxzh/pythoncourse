import pandas as pd
import matplotlib.pyplot as plt

# 读取文件中的数据
df = pd.read_csv(r'商场一楼手机信号强度.txt',
                 header=None, skipinitialspace=True,
                 names=['x','y','s']).dropna()
df['c'] = df['s'].map(lambda x: 'r' if x<40 else ('g' if x>70 else 'b'))
df['s'] = df['s'] * 3
df.plot(x='x', y='y', c='c', s='s', kind='scatter', marker='*')

plt.xlabel('长度坐标',
           fontproperties='simhei',   # 设置中文字体
           fontsize=14)               # 设置字号
plt.ylabel('宽\n度\n坐\n标',           # 每行显示一个字
           fontproperties='microsoft yahei',
           fontsize=14,
           labelpad=10,               # y轴标签与y轴之间的水平距离
           position=(0,0),            # y轴标签的垂直位置
           rotation='horizontal')     # 设置文字方向
plt.title('商场内信号强度',
          fontproperties='stkaiti', fontsize=18)
plt.show()
