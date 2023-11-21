file = open("basic.txt","w")#열기
file.write("hello petter")
file.close()#닫기

with open("basic.txt","r") as file:
    contents = file.read()
print(contents)
