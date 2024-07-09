import numpy as np
import matplotlib.pyplot as plt

# 所有配色方案的名称，需要的话可以把填充方向相反的一组放到一起方便对比
cmap_list = plt.colormaps()  # sorted(plt.colormaps())
# 创建17行10列共170个子图
nrows, ncols = 17, 10
fig, axes = plt.subplots(nrows=nrows, ncols=ncols)
# 设置图形窗口的边界
fig.subplots_adjust(top=0.95, bottom=0.01, left=0.01, right=0.99)
axes.shape = nrows * ncols,
# 创建模拟图像，1行256列像素
image = np.linspace(0, 1, 256).reshape(1,256)
for ax, name in zip(axes, cmap_list):
    # 在每个子图中显示图像，cmap指定配色方案，用来确定像素值与颜色之间的映射关系
    # 也可以直接设置cmap=name
    ax.imshow(image, aspect='auto', cmap=plt.get_cmap(name))
    # 当前子图的位置和大小
    left, bottom, width, height = ax.get_position().bounds
    # 计算并在指定的位置显示字符串，水平居中，垂直居中
    x_text = left + width/2
    y_text = bottom + height/2
    fig.text(x_text, y_text, name, va='center', ha='center', fontsize=6)

# 关闭所有子图的坐标轴刻度、网格线和坐标轴线
for ax in axes:
    ax.set_axis_off()
plt.suptitle('cmap kinds')

plt.savefig('e:\\result.png', dpi=640)
