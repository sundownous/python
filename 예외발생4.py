list_a=[12,345,23,14,6]

try:
    number=int(input("정수를 입력해주세요>"))
    print("{}의 {}번째 요소는 {}입니다".format("list_a",number,list_a[number-1]))
    예외.일어나()#강제예외 정의되지 않은 예외

except ValueError as exc:
    print("정수만 입력하세요")
    print("exc",exc)
except IndexError as exc:
    print("맞는 범위를  입력하세요")
    print("exc",exc)
except Exception as exc:
    print("type(exc):",type(exc))
    print("exc",exc)
    print("파익하지 못한 예외입니다")
