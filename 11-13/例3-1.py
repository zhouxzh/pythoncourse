import matplotlib.pylab as pl

t = pl.arange(0.0, 2.0*pl.pi, 0.01)    # 自变量取值范围
s = pl.sin(t)                          # 计算正弦函数值
z = pl.cos(t)                          # 计算余弦函数值
pl.plot(t,                             # x轴坐标
        s,                             # y轴坐标
        label='正弦',                  # 标签
        color='red')                   # 颜色
pl.plot(t, z, label='余弦',
        lw=3, ls='--', color='blue')   # 3像素宽，虚线
pl.xlabel('x-变量',                    # 标签文本
          fontproperties='STKAITI',    # 字体
          fontsize=18)                 # 字号
pl.ylabel('y-正弦余弦函数值', fontproperties='simhei', fontsize=18)
pl.title('sin-cos函数图像',             # 标题文本
         fontproperties='STLITI',      # 字体
         fontsize=24)                  # 字号
pl.legend(prop='STKAITI')              # 创建、显示图例
pl.grid(alpha=0.7, ls='-.')            # 半透明网格线，点画线
pl.show()                              # 显示绘制的结果图像
