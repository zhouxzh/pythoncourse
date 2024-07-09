import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(20220630)
df = pd.DataFrame(np.random.randint(100,200,(5,3)),
                  columns=['A','B','C'])
df.plot(kind='area')     # 绘制面积图
plt.show()
