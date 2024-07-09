import numpy as np
import matplotlib.pyplot as plt

x = np.arange(7)
y = x*3 + 1
plt.bar(x, y, color=list('bgrcmyk'))
plt.show()
