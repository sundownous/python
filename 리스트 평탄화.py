a=[1,2,[3,4], 5,[6,7],[8,9]]
b=[]

for i in a:
    if type(i)==list:
        for k in i:
            b.append(k)
    else :
        b.append(i)
print("{}를 평탄화 하면 {}입니다!".format(a,b))
