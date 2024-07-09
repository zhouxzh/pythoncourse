from itertools import groupby
import matplotlib.pyplot as plt

# 设置图形中使用中文字体
plt.rcParams['font.sans-serif'] = ['simhei']

# 每门课程的成绩
scores = {'数据结构': [89, 70, 49, 87, 92, 84, 73, 71, 78, 81, 90, 37,
                      77, 82, 81, 79, 80, 82, 75, 90, 54, 80, 70, 68, 61],
          '线性代数': [70, 74, 80, 60, 50, 87, 68, 77, 95, 80, 79, 74,
                      69, 64, 82, 81, 78, 90, 78, 79, 72, 69, 45, 70, 70],
          '英语': [83, 87, 69, 55, 80, 89, 96, 81, 83, 90, 54, 70, 79,
                   66, 85, 82, 88, 76, 60, 80, 75, 83, 75, 70, 20],
          'Python': [90, 60, 82, 79, 88, 92, 85, 87, 89, 71, 45, 50,
                     80, 81, 87, 93, 80, 70, 68, 65, 85, 89, 80, 72, 75]}

# 自定义分组函数，在下面的groupby()函数中使用
def splitScore(score):
    if score>=85:
        return '优'
    elif score>=60:
        return '及格'
    else:
        return '不及格'
    
# 统计每门课程中优、及格、不及格的人数
# ratios的格式为{'课程名称':{'优':3, '及格':5, '不及格':1},...}
ratios = dict()
for subject, subjectScore in scores.items():
    ratios[subject] = {}
    # groupby()函数需要对原始分数进行排序才能正确分类
    for category, num in groupby(sorted(subjectScore), splitScore):
        ratios[subject][category] = len(tuple(num))

# 创建4个子图，axs是包含4个子图的二维数组
fig, axs = plt.subplots(2, 2)
# 整个图形的标题
fig.suptitle('成绩分布图')
# 把axs改为一维数组
axs.shape = 4,
# 依次在4个子图中绘制每门课程的饼状图
for index, subjectData in enumerate(ratios.items()):
    # 选择子图
    plt.sca(axs[index])
    subjectName, subjectRatio = subjectData
    plt.pie(list(subjectRatio.values()),        # 每个扇形对应的数
            labels=list(subjectRatio.keys()),   # 每个扇形的标签
            explode=(0, 0, 0.2),                # 每个饼的第3个扇形偏离饼心
            pctdistance=0.6,                    # 百分比文本与饼心的距离
            autopct='{:.1f}%'.format,           # 百分比显示格式
            shadow=True,                        # 显示阴影
            )
    plt.xlabel(subjectName)
    plt.axis('equal')
# 4个饼状图共用一个图例
plt.legend(loc='upper right',
           bbox_to_anchor=(1.2,2.5))
    
plt.show()
