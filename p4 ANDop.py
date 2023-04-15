#class

B ={0,1}
And = {(a,b,c,d): (1 if a and b and c and d else 0) for a in B for b in B for c in B for d in B}
print(And)

