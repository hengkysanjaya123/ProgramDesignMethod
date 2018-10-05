# 1 1 2 3 5 8 13 21 34
def Fibo(n):
    if n <= 1:
        return 1
    else:
        return Fibo(n - 1) + Fibo(n- 2)

def Fibo2(n):
     a = 0
     b = 1
     c = 1

print(Fibo(4))
