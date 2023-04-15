from random import randrange

def randfind(alist)->(int,int):
    if alist == []:
        return None,None
    c=1
    max= alist[0]
    del alist[0]
    alist = list(enumerate(li))
    while alist != []:
        c +=1
        gi = randrange(len(alist))
        if max < alist[gi][1]:
            max= alist[gi][1]
            
        alist.pop(gi)
    return max,c



if __name__=="__main__":
    li =[1,2,3,6,23]
    print( randfind(li))
