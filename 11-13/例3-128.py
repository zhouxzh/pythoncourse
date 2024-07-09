import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 101)
# 三次贝塞尔曲面的4个调和函数
b0 = (1-t) ** 3
b1 = 3 * (1-t)**2 * t
b2 = 3 * t**2 * (1-t)
b3 = t ** 3

fig, ax = plt.subplots()
# 使用Matplotlib内嵌的Latex排版，下划线表示下标
ax.plot(t, b0, 'r:', label='$B_{0,3}(t)$')
ax.plot(t, b1, 'g--', label='$B_{1,3}(t)$')
ax.plot(t, b2, 'b-.', label='$B_{2,3}(t)$')
ax.plot(t, b3, ls='-', color='#ffaaff', label='$B_{3,3}(t)$')
ax.set_xlabel('t')
ax.set_title('三次贝塞尔曲线的4个调和函数',
             fontproperties='simhei', fontsize=18)
# 定位图例位置
ax.legend(loc='lower left', bbox_to_anchor=(0.35,0.5))
# 绘制函数图像时应设置坐标轴纵横比相等，否则图像会比例不对
ax.set_aspect('equal')

# 绘制垂直直线
line_x = ax.axvline(x=0, ymin=0, ymax=1, visible=False,
                    ls='--', color='blue', alpha=0.6)
# 在图形顶部显示字符串，初始为空字符串
txt = ax.text(0.08, 0.99, '')

def mouse_motion(event):
    # 鼠标不在图形中，xdata和ydata的值为None，直接返回
    if not (event.xdata and event.ydata):
        return
    mouse_x = round(event.xdata, 2)
    # 曲线上没有鼠标当前位置对应的的点，直接返回
    if mouse_x not in t:
        return
    # 获取曲线上与当前鼠标x坐标对应的点
    index = t.tolist().index(mouse_x)
    b0_y = b0[index]
    b1_y = b1[index]
    b2_y = b2[index]
    b3_y = b3[index]
    # 输出文本，4个函数值的和恒等于1，与自变量t无关
    s = (f'{round(b0_y,5)}+{round(b1_y,5)}+{round(b2_y,5)}+{round(b3_y,5)}='
         f'{round(b0_y+b1_y+b2_y+b3_y,2)}')
    txt.set_text(s)
    # 修改垂直直线的位置，更新图形
    line_x.set_xdata(mouse_x)
    line_x.set_visible(True)
    fig.canvas.draw_idle()
# 绑定鼠标移动事件处理函数
fig.canvas.mpl_connect('motion_notify_event', mouse_motion)

plt.show()
