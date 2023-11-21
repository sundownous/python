diction={
    1: 1,
    2:1
    }
def pibo(n):
    if n in diction:
        return diction[n]
    else:
        out=pibo(n-1)+pibo(n-2)
        diction[n]=out
        return out
print(pibo(10))
print(pibo(15))
print(pibo(20))
print(pibo(25))
