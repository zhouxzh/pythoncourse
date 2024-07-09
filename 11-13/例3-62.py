import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1651239393)
plt.hlines(range(8),
           np.random.randint(0,10,8),
           np.random.randint(10,20,8),
           colors=np.random.random((8,3)))
plt.xlabel('水平起止位置', fontproperties='simhei')
plt.ylabel('高度', fontproperties='simhei')
plt.title('横线图', fontproperties='simhei', fontsize=16)

plt.show()
