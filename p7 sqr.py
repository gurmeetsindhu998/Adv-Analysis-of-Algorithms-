def sqr(no):
    I = {n for n in range(10)}
    S ={s*s for s in I}
    IxS = {(i,s) for i in I for s in S}
    Q ={(i,s) for (i,s) in IxS if (i*i == s)}
    P = dict(Q)
    F = lambda n: P[n]
    return F(no)

print(sqr(3))