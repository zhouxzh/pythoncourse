import numpy as np
import matplotlib.pyplot as plt

np.random.seed(20220713)
x = np.arange(20)
y = np.random.randint(20, 50, 20)
y[np.random.randint(0, 20, 5)] = 0

plt.bar(x, y)
plt.xticks(x[y>0])
plt.yticks(y)
plt.show()
