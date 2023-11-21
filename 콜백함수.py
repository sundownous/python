def power(item):
    return item*item#요소를 제곱하는 함수
def under_3(item):
    return item<3#3보다작은 요소를 리턴하는 함수

list_i=[1,2,3,4,5]

out_a=map(power,list_i)#함수를 매개변수로 넣음
print(out_a)#w제너레이터
print(list(out_a))
out_b=filter(under_3,list_i)
print(out_b)
print(list(out_b))
