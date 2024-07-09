import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'height': [180,170,172,183,179,178,160],
                   'weight': [85,80,85,75,78,78,70]})
df.plot(kind='kde', style=['r-.', 'g--']) # 密度图

plt.show()
