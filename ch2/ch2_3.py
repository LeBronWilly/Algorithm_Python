# ch2_3.py
from array import *
x = array('i', [5, 15, 25, 35, 45])     # 建立無號整數陣列

x.insert(2, 100)
for data in x:
    print(data)




import numpy as np
y = np.array([5, 15, 25, 35, 45])
y = np.insert(y,2, 100)
for data in y:
    print(data)



