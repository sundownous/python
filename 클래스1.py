students=[
    {"name":"이재명","korean":87,"math":98,"english":88,"science":95},
    {"name":"홍준표","korean":92,"math":98,"english":96,"science":90},
    {"name":"안철수","korean":88,"math":100,"english":77,"science":90},
    {"name":"유승민","korean":99,"math":87,"english":93,"science":79},
    {"name":"허경영","korean":77,"math":88,"english":66,"science":89}
    ]


print("이름","총점","평균",sep="\t")
for student in students:
    score_sum = student["korean"]+student["math"]+\
                student["english"]+student["science"]
    score_ave= score_sum/4

    print(student["name"], score_sum, score_ave, sep="\t")
