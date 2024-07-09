from math import sin
import numpy as np
import matplotlib.pyplot as plt
 
fig = plt.figure()

# 存放所有顶点的标注信息
annotations = []

# 绘制顶点并创建标注信息
xx = np.arange(0, 4*np.pi, 0.5)
for x in xx:
    y = sin(x)
    # 依次绘制正弦曲线上的每个顶点，每个点作为一条折线图来绘制
    # plot()函数的参数pickradius默认值为5
    point, = plt.plot(x, y, 'bo', markersize=5)
    # 为每个顶点创建隐藏的文本标注
    # 参数xy表示标注箭头指向的位置，xytext表示文本起始坐标
    # 参数arrowprops表示箭头样式
    # 参数bbox表示标注文本的背景色以及边框样式
    annot = plt.annotate(f'{x=},{y=}',
                         xy=(x+0.1, y+0.03), xycoords='data',
                         xytext=(x-2, y+0.2), textcoords='data',
                         arrowprops={'arrowstyle': '->',
                                     'connectionstyle': 'arc3,rad=-0.5'},
                         bbox={'boxstyle': 'round',
                               'facecolor': 'w',
                               'alpha': 0.6},
                         visible=False)
    annotations.append([point, annot])
 
def onMouseMove(event):
    changed = False
    # 遍历所有顶点，检查鼠标当前位置是否与某个顶点足够接近
    # 把足够接近的顶点的标注设置为可见，其他顶点的标注不可见
    for point, annotation in annotations:
        # point.contains()返回值形式如下：
        # (True, {'ind': array([0], dtype=int64)})
        # (False, {'ind': array([], dtype=int64)})
        # 其中True/False表示是否有点距离鼠标位置小于5个点
        # 后面的数组为这些点的下标
        visible = point.contains(event)[0]
        if visible != annotation.get_visible():
            annotation.set_visible(visible)
            changed = True
    if changed:
        # 只在某顶点标注的可见性发生改变之后才更新画布
        plt.draw()

# 响应并处理鼠标移动事件 
fig.canvas.mpl_connect('motion_notify_event', onMouseMove)
 
plt.show()
