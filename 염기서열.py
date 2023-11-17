string_x=input("염기서열을 입력해주세요A T G C만 입력하세요 아니면 버그남:")
a_list=[]#이거 문자열을 분리해서 리스트에 넣는 함수 있던거 같은데 내가 까먹어서 걍 코드로 작성
for i in range(0,len(string_x)):
    a_list.append(string_x[i])

a_dic = {}

for k in a_list:
    if k in a_dic:
        a_dic[k]+=1
    else :
        a_dic[k]=1
for key, element in a_dic.items():
    print("{}: {}개".format(key, element))
