import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 时间轴
t = np.arange(0, 120, 0.5)
# 兔子的运行轨迹，分段函数
rabbit = np.piecewise(t,
                      [t<10, t>110],               # 兔子跑步的两个时间段
                      [lambda x:15*x,              # 兔子第一段时间的路程
                       lambda x:20*(x-110)+150,    # 第二个时间段的路程
                       lambda x:150]               # 兔子中间睡觉时的路程
                     )
tortoise = 3 * t                                   # 小乌龟一直在匀速前进
plt.plot(t, tortoise, label='乌龟', lw=3)
plt.plot(t, rabbit, label='兔子')
plt.title('龟兔赛跑', fontproperties='STKAITI', fontsize=24)
plt.xlabel('时间（秒）', fontproperties='STKAITI', fontsize=18)
plt.ylabel('与起点的距离（米）', fontproperties='simhei', fontsize=18)
myfont = fm.FontProperties(fname=r'C:\Windows\Fonts\STKAITI.ttf',
                           size=12)                # 设置图例中的中文字体和字号
plt.legend(prop=myfont)
plt.show()
