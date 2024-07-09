import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1651229393)
plt.vlines(range(8),
           np.random.randint(0,10,8),
           np.random.randint(10,20,8),
           lw=30,
           colors=np.random.random((8,3)))
plt.xlabel('位置', fontproperties='simhei')
plt.ylabel('起止高度', fontproperties='simhei')
plt.title('竖线图', fontproperties='simhei', fontsize=16)

plt.show()