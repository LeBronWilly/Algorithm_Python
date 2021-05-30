# ch2_5.py
from array import *
x = array('i', [5, 15, 25, 35, 45])     # 建立無號整數陣列

x.remove(25)
for data in x:
    print(data)



print()
import numpy as np
y = np.array([5, 15, 25, 35, 45])
y = np.delete(y, np.argwhere((y == 25) & (y < 0))) # Method 1
y = y[y!=25] # Method 2
for data in y:
    print(data)




