pi=3.14
circle_a=input("구의 반지름을 입력해주세요:")


if circle_a.isdigit():
    flo_cir=float(circle_a)
    vol=4/3*pi*flo_cir**3
    wid=4*pi*flo_cir**2

    print(" 구의 부피는",vol,"입니다.")
    print(" 구의 넓이는", wid,"입니다")
else:
    print("정수를 입력하라고!")
    


