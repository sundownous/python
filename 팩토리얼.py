#반복문으로 구하기
def factos(n):
    value=1
    for i in range(1,n+1):
        value*=i
    return value
foc=int(input("정수입력:"))
print(factos(foc))
#재귀함수로 구하기
def factos1(n):
    if n==1:
        return 1
    else :
        return n*factos1(n-1)

a=int(input("정수입력:"))
print(factos1(a))        

