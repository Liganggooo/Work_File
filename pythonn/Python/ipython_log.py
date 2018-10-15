# IPython log file

randn
from numpy.random import randn
import numpy as np
import os
os.getcwd()
os.chdir('desktop/pythonn/python')
os.getcwd()
get_ipython().magic('run test2.py')
c
c[-2:]
2**24
_i11
-27
_27
_11
get_ipython().magic('logstart')
get_ipython().magic('dirs')
get_ipython().magic('pwd')
print("hello pacong world")
print("hello pacong world")
list = [x for x in range(11)]
list
list = [x for x in range(11) if x//2]
list
list = [x for x in range(11) if x>=5]
list
_i23
get_ipython().magic('timeit [x for x in range(5)]')
x = randn(10,10)
x
get_ipython().magic('pinfo x')
x
print("hello pacong world")
data.shape
x.shape
x*10
lists = [i for i in range(20)]
lists
arr1 = np.array(lists)
arr1
data = [[4,6,5,2],[6,5,9,7]]
data
arr2 = np.array(data)
arr2
arr2.ndim
arr2.shape
np.ones(3,6)
np.ones(6)
np.ones((6,7))
np.sevens(6)
np.sixs(6)
np.zeros(6)
np.empty((3,10))
np.empty((3,3))
np.empty((3,6))
np.empty((3,6))
np.empty((3,6,2))
np.arange(10)
arr = np.arange(15)
arr
arr[5]
arr[5:8]
arr_slice = arr[5:8]
arr_slice[1]
arr[5:8] = 12
arr
arr_slice[1]
arr_slice = arr[5:8]
arr_slice[1]
arr_slice[1] = 12345
arr
arr_slice[:]
arr3d = [[1,2,3],[1,2,3]]
old_value = arr3d[0].copy()
arr3d[0]=3
arr3d
arr2d = np.array(arr3d)
arr3d = old_value
arr2d = np.array(arr3d)
arr2d
get_ipython().magic('save')
get_ipython().magic('save -r numpy.py')
get_ipython().magic('pinfo save')
get_ipython().magic('pwd')
get_ipython().magic('save -r numpy1.py 1-30,36')
get_ipython().magic('save -r numpy1.py')
get_ipython().magic('save -r numpy1.py')
exit()
