#class
#problem Q is binary relation on a set I of instance and a set S of solution ,Q sebset of IxS or Q <=IxS
#odd numbers
I = {n for n in range(10)}
S ={"no","yes"}
IxS = {(i,s) for i in I for s in S}  #order pair all posiible cases
Q ={(i,s) for (i,s) in IxS if (i%2!=0 and s=="yes") or (i%2==0 and s=="no")}
P = dict(Q)
F = lambda n: P[n]
print(F(9))
odd= {i for (i,s) in Q if s=='yes'}


#HW prime number
I = {n for n in range(10)}
S ={"prime","non prime"}
IxS = {(i,s) for i in I for s in S}  #order pair all posiible cases
Q = {(i, s) if (lambda x: all(x % j for j in range(2, int(x**0.5) + 1))
 and s == "prime")(i) else (i, "non prime") for i in I for s in S}
P = dict(Q)
F = lambda n: P[n]
print(F(7))
