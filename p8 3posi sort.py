"""
ip:3 no(1,2,3)   repeat, unordered
op: non decening numbers

"""
#HW
#wrong
def posi(ip):
    I = {n for n in ip}
    S ={(a,b,c) for a in I for b in I for c in I}
    IxS = {(i,s) for i in I for s in S}
    Q ={(s) for (i,s) in IxS if (s[0]<=s[1]<=s[2])}
    return Q


if __name__ == "__main__":
    li= [1,2,3]
    #print(posi(li))
"""
form itertools import product
list(product('012',repeat =3))

"""
#class

I= {(a,b,c) for a in {1,2,3} for b in {1,2,3} for c in {1,2,3}  }
S= {(a,b,c) for (a,b,c) in I if (a<=b<=c)}
IxS= {(i,s) for i in I for s in S}
#Q ={(i,s) for (i,s) in IxS if tuple(sorted(i)) == s} 
Q ={((a,b,c),s) for ((a,b,c),s) in IxS if ((a,b,c)==s or(a,c,b)==s or (b,a,c) == s or (c,a,b)==s or (b,c,a)==s or (c,a,b)==s)}
# can use built in permutations from some lib
D= dict(Q)
F= lambda a,b,c: D[(a,b,c)]
print(F(1,3,2))
