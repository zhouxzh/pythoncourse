import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,10))
data = [20, 30, 60, 70, 80, 110, 150, 200, 210, 230, 280,
        350, 360, 380, 390, 405, 450, 480, 490, 510]
data = range(100, 800, 20)
# 返回包含饼状图中扇形区域的列表和扇形区域标签的列表
patches, texts = plt.pie(data, labels=tuple(map(str,data)),
                         counterclock=False, startangle=90,
                         rotatelabels=True)
max_, min_ = max(data), min(data)
# 所有扇形的半径都限制到[0.35,1.35]之间
factors = [(float(text.get_text())-min_)/(max_-min_) + 0.35
           for text in texts[:len(data)]]
# 设置每个扇形的高度
for index, patch in enumerate(patches[:len(data)]):
    patch.set_radius(factors[index])
# 设置每个扇形标签的位置和字号
for index, text in enumerate(texts[:len(data)]):
    text.set_x(text._x*(factors[index]-0.1))
    text.set_y(text._y*(factors[index]-0.1))
    text.set_fontsize(4+factors[index]*10)
# 绘制空心圆
plt.pie([1], colors=['white'], radius=0.2)
plt.text(-0.18, -0.05, 'Origin', fontsize=24)
plt.savefig('test.png', dpi=480)
