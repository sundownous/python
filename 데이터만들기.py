import random

hangul = list("가나다라마바사아자차카타파하")

with open("info.txt","w") as file:
    for i in range(100):
        name = random.choice(hangul)+random.choice(hangul)
        mass = random.randrange(40, 100)
        kie = random.randrange(140, 200)

        file.write("{},{},{}\n".format(name,mass,kie))#데이터 생
