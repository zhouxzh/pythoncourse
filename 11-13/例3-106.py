import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2*np.pi, 0.01)
y = np.sin(x)
plt.plot(x, y)

plt.xticks(np.arange(0, 2*np.pi, 0.5))
plt.yticks([-1, -0.5, 0, 0.75, 1],
           ['负一', '负零点五', '零', '零点七五', '一'],
           fontproperties='STKAITI')

plt.show()
