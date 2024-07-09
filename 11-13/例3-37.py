from numpy.random import randint, seed
from pandas import DataFrame
from pandas.plotting import parallel_coordinates
from matplotlib.pyplot import legend, show, grid, xticks


N = 6
seed(20220703)
base = randint(80, 150, N)
df = DataFrame({'姓名': ['运动员'+str(i) for i in range(1, N+1)],
                '08岁': base,
                '10岁': base+randint(50, 100, N),
                '15岁': base+randint(50, 100, N),
                '20岁': base+randint(50, 100, N),
                '25岁': base+randint(50, 100, N)})
pc = parallel_coordinates(df, '姓名', color=list('rgbcmy'))
line_styles = ('-', ':', '-.', '--', '-', ':')
line_widths = (1, 1, 1, 1, 3, 3)
for child, ls, lw in zip(pc.get_children(), line_styles, line_widths):
    child.set_ls(ls)
    child.set_lw(lw)
xticks(label=df.columns[1:], fontproperties='simhei')
legend(prop='STKAITI', ncol=2)
grid(False)
show()
