import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(20220701)
df = pd.DataFrame({'A': np.arange(20),
                   'B': np.random.randint(5, 20, 20),
                   'C': np.random.randint(15, 40, 20)})
fig = df.plot(x='A', title='two curves')
fig.lines[0].set_linewidth(3)        # 修改线宽
fig.lines[0].set_linestyle('-.')     # 修改线型

plt.ylabel('value')
plt.legend()                         # 根据当前设置生成图例
plt.show()
