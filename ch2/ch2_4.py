# ch2_4.py
from array import *
x = array('i', [5, 15, 25, 35, 45])     # 建立無號整數陣列

x.append(100)
for data in x:
    print(data)



print()
import numpy as np
y = np.array([5, 15, 25, 35, 45])
y = np.append(y,100)
for data in y:
    print(data)



