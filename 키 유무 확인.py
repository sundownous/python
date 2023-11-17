dicton={
    "name" : "7d 건조망고",
    "type" : "당절임",
    "성분" : ["망고","설탕","메타중아황산나트륨","치자황색소"],
    "origin" : "필리핀"
}
print("키 목록:", *dicton)

key = input("접근 하려는 키를 입력해주세요:")

if key in dicton:
    print(key, ":",dicton[key])
else:
    print("{}는 없는키다 애송아.".format(key))

value = dicton.get("존재하지않는 키")#존재하지 않는 키에 접근 여기 input으로 뭐시기 해도 되겠네
print("값", value)

if value == None:
    print("없는키에 접근했습니다.")
