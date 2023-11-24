import random as rand

print("#랜덤모듈")

print("-random():", rand.random())#0<=x<1사이의 float를 랜덤리턴
print("- uniform(10,20):", rand.uniform(10,20))#지정한 범위사이의 float를 랜덤리턴
print("-randrange(10);", rand.randrange(10))#지정한 범위의 랜덤int를 리턴함 (max)0부터 max까지 (min,max)알죠?
print("-choice([1,2,3,4,5]):",rand.choice([1,2,3,4,5]))#리스트내부를 랜덤리턴
print("-shuffle([1,2,3,4,5]):",rand.shuffle([1,2,3,4,5]))#리스트내부를 랜덤하게 섞는다
print("-sample([1,2,3,4,5],k=2):",rand.sample([1,2,3,4,5],k=2))#리스트요소중 k개를 리턴
