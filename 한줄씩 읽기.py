with open("info.txt","r") as file:
    for line in file:
        (name, mass, kie) = line.strip().split(",")

        if (not name)or(not mass)or(not kie):
            continue
        bmi= int(mass)/((int(kie)/100)**2)
        result=""
        if 25<=bmi:
            result="과체충"
        elif 18.5<=bmi:
            result="정상체중"
        else:
            result="저체중"
        with open("정리표.txt","a") as file:
            file.write("이름:{} 몸무게:{} 키:{} bmi:{} 결과:{}\n".format(name,mass,kie,bmi,result))




       ###print('\n'.join([
            #"이름:{}",
            #"몸무게:{}",
            #"키:{}",
           # "bmi:{}",
          #  "결과:{}"
         #   ]).format(name, mass, kie, bmi, result))
        #print()###
            
#with open("정리표.txt","a") as file:
 #       file.write("이름:{} 몸무게:{} 키:{} bmi:{} 결과:{}".format(name,mass,kie,bmi,result))
