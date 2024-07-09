from tkinter.messagebox import showinfo
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

r, c = 2, 30
fig, ax = plt.subplots()
positions = np.random.randint(-10, 10, (r, c))
colors = np.random.random((c,3))
scatters = ax.scatter(*positions, marker='*',
                      s=60, c=colors)
plt.xlim(-40, 40)
plt.ylim(-40, 40)

def init():
    showinfo('hi', 'a new animation - dongfuguo')
    global positions, stop_positions, scatters
    # 散点初始位置和预期停靠位置
    positions = np.random.randint(-10, 10, (r, c))
    stop_positions = np.random.randint(-39, 39, (r, c))
    scatters.set_offsets(positions.T)
    return scatters,
    
def update(i):
    global positions
    # 随机游走，两个方向随机加减1，都限定在[-39,39]区间内
    offsets = np.random.choice((1,-1), (r,c))
    # 已经到达指定坐标的散点不再移动
    offsets[positions==stop_positions] = 0
    if offsets.any():
        # 还有没到达预定停靠位置的散点
        positions = positions + offsets
        positions[positions>39] = 39
        positions[positions<-39] = -39
        # 更新散点位置
        scatters.set_offsets(positions.T)
        return scatters,
    else:
        # 全部到达预定停靠位置，开始一个新的动画
        init()

ani = animation.FuncAnimation(fig, init_func=init,
                              func=update, interval=0.5,
                              blit=False)
plt.show()
