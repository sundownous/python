#prmd=""
#for i in range(9):
#    prmd+="*"
#    print(prmd)

#prmd=""
#for i in range(9):
#    for k in range(0,i+1):
#        prmd+="*"
#    prmd+="\n"
#print(prmd)
    

prmd=""
for i in range(1,15):
    for k in range(14,i,-1):
        prmd+=" "
    for j in range(1,2*i-1):
        prmd+="*"
    prmd+="\n"
print(prmd)
    
