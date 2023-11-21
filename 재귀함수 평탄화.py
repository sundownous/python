def plist(alist):
    out=[]
    for item in alist:
        if type(item)==list:
            out+=plist(item)
        else:
            out.append(item)
    return out
example = [1,2,[3,4,[5,6],7],8,[9,10]]
print(plist(example))
