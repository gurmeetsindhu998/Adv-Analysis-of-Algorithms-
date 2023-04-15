
"""
0 =={}
1== {{}}
2=={{},{{}}}

0 ==[]
1==[[]]
2==[[],[[]]]
3== [[],[[]], [[],[[]]]]
"""

def setpattern(n: int):
    ans = []
    li=[]

    for i in range(1,n+1):
        for j in range(1,i+1):
             p1 = j*'['
        for j in range(1,i+1):
             p2 = j*']'
        ans.append(p1+p2)
    
    return ans

#print(setpattern(3))


#class
def nsf(n: int):
    #ns = lambda n: [] if n<=0 else ns(n-1)+ [ns(n-1)]
    return [] if n<= 0 else nsf(n-1) + [nsf(n-1)]


print(nsf(4))


