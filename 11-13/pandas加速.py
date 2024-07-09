from time import time
import swifter
import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randint(1, 100, (1000000, 100)))
start = time()
df.apply(sum)
print(time()-start)

start = time()
df.swifter.apply(sum)
# 下一行代码不显示进度条，但是也丧失了并行加速的作用
# df.swifter.progress_bar(False).apply(sum)
print(time()-start)
