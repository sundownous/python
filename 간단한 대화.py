import datetime

now = datetime.datetime.now()

print("안녕 나는 파이썬 이야")
talk=input("입력:")
if "안녕" in talk :
    print("안녕~")
elif "몇 시" in talk :
    print("지금은 {} 시야".format(now.hour))
else :
    print("\"{}\"? 무슨 말인지 모르겠어.".format(talk))
    print("그 말을 알려줄 수 있니?")
    mins=input("뜻을 입력하시오")
    print("아하\"{}\"는 \"{}\"라는 뜻이구나!".format(talk, mins))
