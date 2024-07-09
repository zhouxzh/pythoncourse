import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 7, 8]
y = [5, 5, 5, 5, 5, 5, 5, 6, 6, 7, 8, 9, 15]
# h是形状为(len(x_bins),len(y_bins))的二维数组
# 一个方向表示数据x的直方图，另一个方向表示数据y的直方图
# 图像根据xedges和yedges进行分块划分，每个分块的颜色与分块内数据数量对应
h, xedges, yedges, image = plt.hist2d(x, y, bins=[3,4])
# 转置后再垂直翻转，得到的数组与绘制的图像对应
h = h.T[::-1]
print(h, xedges, yedges, sep='\n')
plt.colorbar(image).set_label('counts in bins')
plt.show()
