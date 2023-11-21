circle=int(input("원판을 입력하세요:"))

def hanoi(n, 시작, 대상, 보조):
    global count
    if n==1:
        #print(시작,"->",대상)
        count+=1
    else:
        hanoi(n-1,시작,보조,대상)
        #print(시작,"->",대상)
        count+=1
        hanoi(n-1,보조,대상,시작)


count =0


hanoi(circle,"a","b","c")
print(count)
#근데 이거 걍 공식으로 구하는게 빠를듯
