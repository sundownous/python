six = float(input("자연수를 입력해주세요:"))

if six <= 0:
    print("자연수를 입력하라고 기회는 없다")
    
if six % 1 !=0:
    print("선생님 소숫점이 있잖아요")
#whlie로 만들었으면 프로그램이 종료되게 할 수 ㅣ있을거같은데
if (six % 2 == 0 and six % 3 == 0) == True :
    print("{:g}는 6의 배수입니다".format(six))
else :
    print("{:g}는 6의 배수가 아닙니다".format(six))
