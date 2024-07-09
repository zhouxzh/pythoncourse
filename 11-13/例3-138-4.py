import gif
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

r, c = 2, 30
positions = np.random.randint(-10, 10, (r,c))
stop_positions = np.random.randint(-39, 39, (r,c))
colors = np.random.random((c,3))

# 选择后端渲染引擎
# 这一句非常重要，否则会因为内存不足而中途结束
matplotlib.use('Agg')

@gif.frame
def draw():
    plt.scatter(*positions, marker='*', s=60, c=colors)
    plt.xlim(-40, 40)
    plt.ylim(-40, 40)

frames = []
while True:
    offsets = np.random.choice((1,-1), (r,c))
    offsets[positions==stop_positions] = 0
    if offsets.any():
        positions = positions + offsets
        positions[positions>39] = 39
        positions[positions<-39] = -39
        frame = draw()
        frames.append(frame)
    else:
        break

# 保存GIF动图，大约需要10-30分钟
gif.save(frames, 'brown1.gif')
