# ch4_3.py
from queue import Queue

q = Queue()
for i in range(23):
    q.put(i)

while not q.empty():
    print(q.get())
else:
    print("佇列已空")














