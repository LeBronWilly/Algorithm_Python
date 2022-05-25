# ch6_2.py
def create_btree(tree, data):
    ''' 使用data建立二元樹 '''
    for i in range(len(data)):
        level = 0                           # 程式的第0層相當於實體的第1層
        # data[0]
        if i == 0:                          # 第0索引資料放在第0層
            tree[level] == data[i] 
        # data[1]~data[-1]
        else:
# 當while迴圈結束表示找到存放數據的節點(索引)位置
            while tree[level]:              # 當陣列不是0表示這是有資料可以比較
                if data[i] > tree[level]:   # 如果資料大於節點索引, 往右找尋
                    level = level * 2 + 2   # 放在右子節點
                else:                       # 否則往左找尋
                    level = level * 2 + 1   # 放在左子節點
        tree[level] = data[i]               # 找到數據應存放的節點索引
        print(i, tree)                      # 取消此註解可以看到建立二元樹的過程
            
btree = [0] * 8                             # 二元樹陣列
data = [10, 21, 5, 9, 13, 28]
create_btree(btree, data)
for i in range(len(btree)):
    print("二元樹陣列btree[%d] = %d" % (i, btree[i]))

