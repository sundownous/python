def creat_std(name,korean,math,english,science):
    return {"name":name,
            "korean":korean,
            "math":math,
            "english":english,
            "science":science
            }


students=[
    creat_std("이재명",87,98,88,95),
    creat_std("홍준표",92,98,96,90),
    creat_std("안철수",88,100,77,90),
    creat_std("유승민",99,87,93,79),
    creat_std("허경영",77,88,66,89)
    ]
print("이름","총점","평균",sep="\t")
for student in students:
    score_sum = student["korean"]+student["math"]+\
                student["english"]+student["science"]
    score_ave= score_sum/4

    print(student["name"], score_sum, score_ave, sep="\t")
