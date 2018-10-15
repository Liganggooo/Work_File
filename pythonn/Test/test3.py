import json
import numpy as np
from pandas import Series,DataFrame
from numpy import random
x = np.arange(12.).reshape(3,4)
# print(x)

frame = DataFrame(x,columns = list('abcd'),index = list('efg'))
# print(frame)

series = frame.ix[0]
# print(frame - series)

rando = np.random.randn(4,4)
print(rando)