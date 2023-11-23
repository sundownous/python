list_a=[12,345,23,14,6]

try:
    number=int(input("정수를 입력해주세요>"))
    print("{}의 {}번째 요소는 {}입니다".format("list_a",number,list_a[number-1]))


except ValueError:
    print("정수만 입력하세요")
    
except IndexError:
    print("맞는 범위를  입력하세요")
    
