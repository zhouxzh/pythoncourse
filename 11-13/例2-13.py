import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'height': [180,170,172,183,179,178,160,2],
                   'weight': [85,80,85,75,78,78,70,150]})
df.plot(kind='box')   # 箱图，中间50%使用矩形
                      # 两端的四分之一使用线段
                      # 异常值使用'o'符号

plt.show()
