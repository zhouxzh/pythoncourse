import matplotlib.pylab as pl

pl.seed(20220703)
x = pl.randint(10, 30, 50)
y = x + pl.randint(-10, 20, 50)
pl.scatter(x, y,
           s=x*y/2,    # 散点大小与位置有关
                       # 越往右上角越大
           c='r',      # 设置散点颜色
           marker='*') # 设置散点形状为五角星
pl.show()
