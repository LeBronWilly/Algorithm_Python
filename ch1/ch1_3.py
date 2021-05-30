# ch1_3.py
import itertools

x = ['1', '2', '3',"1"]
perm = itertools.permutations(x) # 排列(階層)
count=0
for i in perm:
    count+=1
    print(i)
print("count:",count)


















