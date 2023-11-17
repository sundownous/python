dicton={
    "name" : "7d 건조망고",
    "type" : "당절임",
    "성분" : ["망고","설탕","메타중아황산나트륨","치자황색소"],
    "origin" : "필리핀"
}
print("name", dicton["name"])
print("type", dicton["type"])
print("성분", dicton["성분"])
print("origin", dicton["origin"])

dicton["name"]="8d 건조망고"
print("name", dicton["name"])

print("딕셔너리요소 추가 제거")

dicton["가격"]= 5000

print("요소추가 이후:", dicton)
del dicton["가격"]

print("요소삭제 이후:", dicton)

