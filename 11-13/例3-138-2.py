import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

r, c = 2, 80
positions = np.random.randint(-10, 10, (r, c))
colors = np.random.random((c,3))

fig, ax = plt.subplots()
scatters = ax.scatter(positions[0], positions[1],
                      marker='*', s=60, c=colors)
plt.xlim(-40, 40)
plt.ylim(-40, 40)
def update(i):
    global positions
    positions = positions + np.random.choice((1,-1), (r,c))
    positions[positions>39] = 39
    positions[positions<-39] = -39
    scatters.set_offsets(positions.T)
    yield scatters
    
# 创建并显示动画，需要把动画赋值给一个变量保存下来
# 否则动画会被删除从而无法显示
ani = animation.FuncAnimation(fig, update, interval=100,
                              blit=True)
plt.show()
