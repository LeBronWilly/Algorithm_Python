# ch3_1.py
class Node():      # 代表之後的大家都可以取用這個類別的設定，達到避免重複設定函式的目的
    ''' 節點 '''
    def __init__(self, data=None, name=None):  # 代表宣告時會自動執行的函式，也就是宣告類別的"起手式"，一般拿來放基礎的屬性設定
    # 因為self是class本身，所以第一個不用更動
        # 在這邊self.的設定，就代表你之後可以用的class屬性
        self.data = data            # 資料
        self.next = None            # 指標
        self.__name = name          # 如果變數不希望直接被取用，則可以給兩條底線
        # __name不能直接讀取，可以用來設定一些內部使用的函數

n1 = Node(23)                       # 節點 1
n2 = Node(6)                        # 節點 2
n3 = Node(24)                       # 節點 3
n1.next = n2                        # 節點 1 指向節點 2
n2.next = n3                        # 節點 2 指向節點 3
ptr = n1                            # 建立指標節點
while ptr:
    print(ptr.data)                 # 列印節點
    ptr = ptr.next                  # 移動指標到下一個節點

    








