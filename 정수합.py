def sum_all(n,m):
    value=0
    for i in range(n,m+1):
        value+=i
    return value


a=int(input("정수 범위시작을 입력해주세요:"))
b=int(input("정수 범위끝을 입력해주세요:"))
print(sum_all(a,b))
