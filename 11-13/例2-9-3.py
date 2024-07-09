import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(20220630)
df = pd.DataFrame(np.random.rand(10, 4),
                  columns=['a', 'b', 'c', 'd'])
# 堆叠的水平柱状图，每段长度表示数值大小
df.plot(kind='barh', stacked=True)
plt.show()
