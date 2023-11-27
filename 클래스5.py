class Student:
    def study(self):
        print("공부")

class Teacher:
    def teach(self):
        print("가르치기")

classroom=[Student(),Student(),Teacher(),Student(),Student()]

for person in classroom:
    if isinstance(person, Student):
        person.study()
    else:
        person.teach()
    #elif isinstance(person, Teacher):
     #   person.teach()
