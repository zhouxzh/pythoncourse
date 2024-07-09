import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'height': [180,170,172,183,179,178,160],
                   'weight': [85,80,85,75,78,78,70]})
df.plot(x='height', y='weight', kind='scatter',
        marker='*', s=60, label='height-weight',
        title='height-weight').axes.title.set_size(20)    # 绘制散点图
plt.show()
