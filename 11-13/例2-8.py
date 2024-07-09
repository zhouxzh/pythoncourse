import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(20220630)
df = pd.DataFrame(np.random.randn(1000, 3), columns=list('ABC')).cumsum()
df.plot.line()     # 绘制折线图，以index为横坐标
plt.show()
