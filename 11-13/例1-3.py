import numpy as np
from PIL import Image

fn = '彩色图像.jpg'
arr = np.array(Image.open(fn))
# 红绿蓝三分量加权平均，变为灰度图像
arr = np.average(arr, axis=2, weights=(0.3,0.59,0.11))
arr = np.int8(np.clip(arr*1.3, 0, 255))   # 灰度值变大，整体调亮，然后重建图像
im_gray = Image.fromarray(arr, 'L')
im_gray.show()                            # 显示图像
# im_gray.save('转换后的灰度图像.jpg')     # 保存图像文件
