import numpy as np
import matplotlib.pyplot as plt

x = np.arange(7)
y = x*3 + 1
# 每个柱的左侧从x指定的位置开始
bars = plt.bar(x, y, width=0.4, align='edge',
               color=np.random.random((7,3)))
# 在每个柱的上方显示标签
# 默认显示每个柱的高度，可以使用labels参数指定显示其他内容
# 默认显示格式为fmt='%g'
# 默认显示位置为柱的顶部，加label_type='center'显示在柱的中间
plt.bar_label(bars)
plt.show()
