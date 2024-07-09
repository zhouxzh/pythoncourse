import matplotlib.pylab as pl

x = pl.arange(0, 2.0*pl.pi, 0.1)  # x轴数据
y = pl.cos(x)             # y轴数据
pl.scatter(x,             # x轴坐标
           y,             # y轴坐标
           s=40,          # 散点符号大小
           linewidths=2,  # 加号线条的线宽
           marker='+')    # 散点符号
pl.show()
