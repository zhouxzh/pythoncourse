import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1651024751)
plt.stem(range(6), np.random.randint(1,10,6),
         linefmt='g-.', markerfmt='ro',
         basefmt='b-')
plt.show()