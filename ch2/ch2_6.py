# ch2_6.py
from array import *
x = array('i', [5, 15, 25, 35, 45])     # 建立無號整數陣列
n = x.pop()
print('刪除 ', n)
for data in x:
    print(data)

n = x.pop(2)
print('刪除 ', n)
for data in x:
    print(data)





print()
import numpy as np
y = np.array([5, 15, 25, 35, 45])
y[-1]
y=y[:-1]
for data in y:
    print(data)



