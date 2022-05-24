# ch5_5.py
def factorial(n):
    global fact
    """ 計算n的階乘, n 必須是正整數 """
    if n == 1:
        print("factorial(%d)呼叫前 %d! = %d" % (n, n, fact))
        print("到達遞迴條件終止 n = 1")
        fact = 1
        print("factorial(%d)返回後 %d! = %d" % (n, n, fact))
        return fact
    else:
        print("factorial(%d)呼叫前 %d! = %d" % (n, n, fact)) 
        fact = n * factorial(n-1)
        print("factorial(%d)返回後 %d! = %d" % (n, n, fact))
        return fact

fact = 0
# N = int(input("請輸入階乘數 : "))
N = 3
print(N, " 的階乘結果是 = ", factorial(N))


