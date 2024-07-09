import numpy as np
import matplotlib.pyplot as plt

# 生成8个方向的角度
theta = np.linspace(0, 2*np.pi, 8, endpoint=False)
r = 1
# 每个风矢量的x、y位置
X = r * np.cos(theta)
Y = r * np.sin(theta)
# 每个风矢量表示的风向的x、y分量
# x、y分量的平方和的平方根（模长）表示风力，等于风标上所有数字之和
# 一个短线表示5，一个长线表示10，一个小三角形表示50
# 例如，第一个风矢量风向向量为10i+0j，模长为10，所以会显示1个长划线
# 第二个风矢量风向向量为21.2132034i+21.2132034j，模长为30，显示3个长划线
U = X * np.array([10,30,80,120,20,5,90,40])
V = Y * np.array([10,30,80,70,20,5,90,40])
print(U, V, sep='\n')
# 绘制风标图，蓝色倒钩，红色小三角
plt.barbs(X, Y, U, V, barbcolor='blue', flagcolor='red')

# 输出字符串显示风向风速
font = dict(fontproperties='simhei')
plt.text(0.8, -0.1, '西风2级', **font)
plt.text(0.55, 0.48, '西南风6级', **font, rotation=45)
plt.text(0.02, 0.73, '南风13级', **font, rotation=90)
plt.text(-0.83, 0.55, '东东南风20级', **font, rotation=-32)
plt.text(-1, 0.03, '东风4级', **font)
plt.text(-0.8, -0.7, '东北风1级', **font, rotation=45)
plt.text(-0.1, -1, '北风18级', **font, rotation=90)
plt.text(0.45, -0.85, '西北风8级', **font, rotation=-45)
plt.text(-0.5, -0.1, '风力风向示意图', **font, fontsize=20)
plt.gca().set_aspect('equal')
plt.show()
