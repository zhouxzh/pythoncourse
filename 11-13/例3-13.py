import numpy as np
import matplotlib.pyplot as plt

def draw(a, b):
    plt.figure(figsize=(10, 200), dpi=240)
    t = np.arange(-1.55, 1.55, 0.01)
    x1 = a + b*np.cos(t)
    y1 = a*np.tan(t) + b*np.sin(t)

    x2 = a - b*np.cos(t)
    y2 = a*np.tan(t) - b*np.sin(t)

    plt.plot(x1, y1, x2, y2)
    plt.title(f'{a=},{b=}')
    plt.ylim(-10, 10)
    plt.gca().set_aspect('equal')
    plt.savefig('{},{}.jpg'.format(a,b))

draw(0.3, 0.8)
draw(2, 2)
draw(3, 1)
