import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['simhei']

# 某学生的课程与成绩
courses = ['C++', 'Python', '高数', '大学英语', '软件工程',
           '组成原理', '数字图像处理', '计算机图形学']
scores1 = [80, 95, 78, 85, 45, 65, 80, 60]
scores2 = [45, 77, 93, 60, 75, 90, 80, 90]
dataLength = len(courses)              # 数据长度

# angles数组把圆周等分为dataLength份
angles = np.linspace(0,                # 数组第一个数据
                     2*np.pi,          # 数组最后一个数据
                     dataLength,       # 数组中数据数量
                     endpoint=False)   # 不包含终点
scores1.append(scores1[0])
scores2.append(scores2[0])
angles = np.append(angles, angles[0])  # 闭合
# 绘制雷达图
plt.polar(angles,                      # 设置角度
          scores1,                     # 设置各角度上的数据
          'r*--',                      # 设置颜色、线型和端点符号
          linewidth=2,                 # 设置线宽
          label='张三')                # 设置在图例中显示的标签
# 填充雷达图内部
plt.fill(angles,
         scores1,
         facecolor='r',
         alpha=0.3)

# 绘制雷达图
plt.polar(angles,
          scores2,
          'g^--',
          linewidth=2,
          label='李四')
# 填充雷达图内部
plt.fill(angles,
         scores2,
         facecolor='g',
         alpha=0.3)

# 设置角度网格标签，两个同学共用
plt.thetagrids(angles[:8]*180/np.pi,
               courses)
# 设置图例位置
plt.legend(loc='upper right',
           bbox_to_anchor=(1.1,1.1))
plt.show()
