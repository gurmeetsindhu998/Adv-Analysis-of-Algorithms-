#set of all infinte number
#generator

def gene():
    i=0
    while True:
        yield i
        i+=1
            
if __name__=="__main__":
    for i in gene():
       print(i)
    
    
    
    


#class
"""
n =gene()
    print(next(n))
    print(next(n))
    print(next(n))
    print(next(n))
    
for i in gene():
    print(i)


can also use next()
print(55555 in gene())  op: True
print(55 in gene())       :T
print(5.4 in gene())   op: inf search

N= gene()
print(55 in N)   :T
print(5 in N)    : Inf bcz it is already at 55



ge = (s for s in {1,1,2,3,4,5,6} if s%2 == 0)       :generator expression, use ( )
print(list(ge))   op: [2,4,6]
ge = (s for s in {1,1,2,3,4,5,6} if s%2 == 0)      
print(list(ge))   op: blank     bcz already gone over it    only usable for one time


"""


"""
*****strange
l = [[2,3],[3,4]]
print(l[0][1])     :3
print([2,3][1])    :3    because [2,3] is a list and [1] is the index for it

"""