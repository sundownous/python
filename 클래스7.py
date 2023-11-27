class Student:

    count=0
    students=[]

    @classmethod
    def print(cls):
        print("------학생목록-------")
        print("이름","총점","평균",sep="\t")
        for student in cls.students:
            print(str(student))
        print("-----------------------")
            
        
    def __init__(self,name,korean,math,english,science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        self.count +=1
        self.students.append(self)

    def get_sum(self):
        return self.korean+self.math+self.english+self.science
    def get_ave(self):
        return self.get_sum()/4

    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name, self.get_sum(), self.get_ave()
            )


Student("이재명", 87, 98, 88, 95)
Student("홍준표",92,98,96,90)
Student("안철수",88,100,77,90)
Student("유승민",99,87,93,79)
Student("허경영",77,88,66,89)

Student.print()
