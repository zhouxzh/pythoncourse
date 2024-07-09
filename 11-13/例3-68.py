import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 模拟数据
N = 25
df = pd.DataFrame({'一班':np.random.randint(1,100,N),
                   '二班':np.random.randint(1,100,N),
                   '三班':np.random.randint(1,100,N)})
# 绘制图形
im = plt.imshow(df.values)
# 设置坐标轴标签和标题
plt.xticks([0,1,2], df.columns, fontproperties='simhei')
plt.yticks(range(25), [f'{i+1}号' for i in range(25)],
           fontproperties='simhei')
plt.title('学生成绩热力图', fontproperties='simhei',
          fontsize=18)
# 设置坐标轴纵横比
plt.gca().set_aspect(0.2)
for i, row in enumerate(df.values):
    for j, value in enumerate(row):
        plt.text(j, i, value, fontsize=8, color='r',
                 va='center', ha='center')
# 设置颜色条
plt.colorbar(im)

# 保存图形
plt.savefig('test.png', dpi=240)
