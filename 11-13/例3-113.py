import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 20, endpoint=False)
y = 3 ** x
_, (ax1, ax2) = plt.subplots(1, 2)
line1, = ax1.plot(x, y, 'r-')
ax1.set_yscale('log', base=2)
ax1.tick_params(axis='y', colors='red')
ax1.set_aspect('equal')
ax1.set_title('base=2')

line2, = ax2.plot(x, y, 'b-.')
ax2.set_yscale('log', base=10)
ax2.tick_params(axis='y', colors='blue')
ax2.set_aspect('equal')
ax2.set_title('base=10')
plt.suptitle('y=3**x', fontsize=16)
plt.show()
