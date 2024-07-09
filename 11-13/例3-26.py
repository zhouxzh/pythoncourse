import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1651020065)
x = np.arange(50)
y = np.random.randint(0, 50, (5,50))
plt.stackplot(x, y, labels=list('abcde'),
              colors=np.random.random((5,3)))
plt.legend()
plt.show()
