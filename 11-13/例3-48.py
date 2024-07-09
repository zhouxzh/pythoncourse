import numpy as np
import matplotlib.pyplot as plt

# 生成测试数据
x = np.linspace(0, 10, 11)
y = 11 - x

# 绘制柱状图
plt.bar(x,
        y,
        color='#772277',        # 所有柱的颜色相同
        alpha=0.8,              # 透明度
        edgecolor='blue',       # 边框颜色，呈现描边效果
        linestyle='--',         # 边框样式为虚线
        linewidth=1,            # 边框线宽
        hatch='*')              # 内部使用五角星填充

# 为每个柱形添加文本标注
for xx, yy in zip(x,y):
    plt.text(xx-0.2, yy+0.2, f'{yy:2.0f}', va='center')

plt.show()
