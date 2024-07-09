from pandas import cut, value_counts

scores = [89,70,49,87,92,84,73,71,78,81,90,37,
          77,82,81,79,80,82,75,90,54,80,70,68,61]
groups = value_counts(cut(scores,[0,60,70,80,90,101],
                          labels=['不及格','及格','中','良','优秀'],
                          right=False))
print(groups)
