import csv
import random
import datetime

fn = 'data.csv'

with open(fn, 'w', encoding='cp936', newline='') as fp:
    # 创建csv文件写入对象
    wr = csv.writer(fp)
    # 写入表头
    wr.writerow(['日期', '销量'])

    startDate = datetime.date(2022, 1, 1)
    # 生成365个模拟数据，可以根据需要进行调整
    for i in range(365):
        amount = 300 + i*5 + random.randrange(100)
        wr.writerow([str(startDate), amount])
        startDate = startDate + datetime.timedelta(days=1)
