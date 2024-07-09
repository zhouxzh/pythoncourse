import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(20220630)
df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df.T.plot(kind='barh', stacked=True)
plt.show()
