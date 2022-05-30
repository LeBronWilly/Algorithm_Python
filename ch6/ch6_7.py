# ch6_7.py
class Node():    # 節點類別
    def __init__(self, data=None):
        ''' 建立二元樹的節點 '''
        self.data = data    # 父節點
        self.left = None    # 左子節點
        self.right = None   # 右子節點

    def insert(self, data):
        ''' 建立二元樹 '''
        if self.data:                           # 如果根節點存在
            if data < self.data:                # 如果插入值<目前節點值
                if self.left:                   # 如果左子節點存在
                    self.left.insert(data)      # 遞迴呼叫往下一層
                else:                           # 如果左子節點不存在
                    self.left = Node(data)      # 建立左子節點以存放資料
            else:                               # 如果插入值>目前節點值
                if self.right:                  # 如果右子節點存在
                    self.right.insert(data)     # 遞迴呼叫往下一層
                else:                           # 如果右子節點不存在
                    self.right = Node(data)     # 建立右子節點以存放資料
        else:                                   # 如果根節點不存在
            self.data = data                    # 建立根節點

    def search(self, val):
        ''' 搜尋特定值 '''                      
        if val < self.data:                     # 如果搜尋值<目前節點值
            if not self.left:                   # 如果左子節點不存在
                return str(val) + " 不存在"      # 此值不存在於樹中
            return self.left.search(val)        # 遞迴繼續往左子樹找尋
        elif val > self.data:                   # 如果搜尋值>目前節點值
            if not self.right:                  # 如果右子節點不存在
                return str(val) + " 不存在"      # 此值不存在於樹中
            return self.right.search(val)       # 遞迴繼續往右子樹找尋
        else:                                   # 如果搜尋值=目前節點值
            return str(val) + " 找到了"          # 此值已於樹中找到

tree = Node()                                   # 建立二元樹物件
datas = [10, 21, 5, 9, 13, 28, 2, 30, 23]       # 建立二元樹數據
for d in datas:
    tree.insert(d)                              # 分別插入數據

# n = eval(input("請輸入欲搜尋資料 : "))
for n in range(1, 14):
    print(tree.search(n))
