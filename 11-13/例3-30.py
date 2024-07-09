import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

np.random.seed(165112733)

x, y = np.meshgrid(range(5), range(5))
u = np.random.random((len(x), len(x)))
v = np.random.random((len(x), len(x)))
mask = ((x-2)**2 + (y-2)**2) < 1
u = np.ma.masked_array(u, mask=mask)
v = np.ma.masked_array(v, mask=mask)
plt.quiver(x, y, u, v)
circle = patches.Circle((2,2), radius=1)
plt.gca().add_patch(circle)
plt.gca().set_aspect('equal')
plt.show()
