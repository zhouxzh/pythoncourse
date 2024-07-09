import matplotlib.pyplot as plt

plt.figure(1, figsize=(8,8))
ax = plt.subplot(111)

def drawNode(text, startX, startY, endX, endY, ann):
    # 绘制带箭头的文本
    ax.annotate(text,
                xy=(startX+0.01, startY), xycoords='data',
                xytext=(endX, endY), textcoords='data',
                arrowprops=dict(arrowstyle='<-',
                                connectionstyle='arc3'),
                bbox=dict(boxstyle='square', fc='r', alpha=0.6)
                )
    # 在箭头中间位置标记数字
    ax.text((startX+endX)/2+0.02, (startY+endY)/2, str(ann))
# 绘制树根
bbox_props = dict(boxstyle='square,pad=0.3', fc='cyan',
                  ec='b', lw=2)
ax.text(0.5, 0.97, 'A', bbox=bbox_props)
# 绘制其他节点
drawNode('B', 0.5, 0.97, 0.3, 0.8, 0)
drawNode('C', 0.5, 0.97, 0.7, 0.8, 1)
drawNode('D', 0.3, 0.8, 0.2, 0.6, 0)
drawNode('E', 0.3, 0.8, 0.4, 0.6, 1)
drawNode('F', 0.7, 0.8, 0.6, 0.6, 0)
drawNode('G', 0.7, 0.8, 0.8, 0.6, 1)
drawNode('H', 0.2, 0.6, 0.1, 0.4, 0)
drawNode('I', 0.4, 0.6, 0.3, 0.4, 0)
drawNode('J', 0.4, 0.6, 0.5, 0.4, 1)
drawNode('K', 0.6, 0.6, 0.7, 0.4, 1)

plt.show()
