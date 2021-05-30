# ch2_7.py
from array import *
x = array('i', [5, 15, 25, 35, 45])     # 建立無號整數陣列

i = x.index(35)
print(i)






print()
import numpy as np
y = np.array([5, 15, 25, 35, 45])
j = np.argwhere(y==35)[0][0]
j = np.argwhere(y==35).reshape(1)[0]
print(j)



