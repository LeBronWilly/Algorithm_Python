# ch13_6.py                 
def bfs(graph, start):
    ''' 寬度優先搜尋法 '''
    visited = []                            # 拜訪過的頂點
    queue = [start]                         # 模擬佇列
    while queue:        
        node = queue.pop(0)                 # 取索引0的值
        visited.append(node)                # 加入已拜訪行列
        neighbors = graph[node]             # 取得已拜訪節點的相鄰節點           
        for n in neighbors:                 # 將相鄰節點放入佇列
            queue.append(n)
    return visited

graph = {'A':['B', 'C', 'D'],
         'B':['E'],
         'C':['F'],
         'D':['G', 'H'],
         'E':[],
         'F':['I', 'J'],
         'G':[],
         'H':[],
         'I':[],
         'J':[]
        } 
print(bfs(graph,'A'))





