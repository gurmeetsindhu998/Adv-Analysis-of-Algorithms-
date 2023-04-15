
#sqrt in IxS
I = {n*n for n in range(10)}
S ={s for s in range(-9,10)}
IxS = {(i,s) for i in I for s in S}  #order pair all posiible cases
Q ={(i,s) for (i,s) in IxS if (i == s*s)}
"""
ans =dict()
for i in I:   #wrong
    for v,c in Q:
        if v == i:
            ans[i]= c
            ans[i].extend(c)
print(ans)


#class
"""
#After Q
#ig is value to display
P = {i:{s for (ig,s) in Q if i==ig } for i in I}
inP= lambda i, ss: all((i,s) in Q for s in ss)

inG = lambda i , ss: all((i,s) in Q for s in ss)
print(inP(81, {-9,9}))
print(inP(81, {-8,8}))