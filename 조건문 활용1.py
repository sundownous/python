import datetime

now=datetime.datetime.now()
print("현재는 {}년 {}월 {}일 {}시 {}분 {}초입니다".format(now.year, now.month, now.day,
                                              now.hour, now.minute, now.second))
if now.hour <12 :
    print("현재는 오전입니다")
if now.hour >=12 :
    print("현재는 오후입니다")

if 3 <= now.month <6 :
    print("현재는 봅임니다")
if 6 <= now.month < 9:
    print("현재는 여름임니다")
if 9 <= now.month < 11:
    print("현재는 가을임니다")
if 11 <= now.month <13 :
    print("현재는 겨울임니다")
if 1 <= now.month <3 :
    print("현재는 겨울임니다")
