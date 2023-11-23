list_a=[12,345,23,14,6]

try:
    number=int(input("정수를 입력해주세요>"))
    print("{}의 {}번째 요소는 {}입니다".format("list_a",number,list_a[number-1]))
except Exception as exc:
    print("type(exc):",type(exc))
    print("exc",exc)
