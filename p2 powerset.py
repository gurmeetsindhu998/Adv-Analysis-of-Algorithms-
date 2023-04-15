def powset(nums: set)-> set:
    result = [[]]
    for num in nums:
        result += [i + [num] for i in result]
    return result



 
print(powset({1,2,3}))



#class
'''
s= {1,2,3}
P = [set()]
Pp = [set()| {1}]
P = P+ Pp
Pp = [ p| {2} for p in P]
P += Pp
Pp = [ p| {3} for p in P]
P += Pp
print(P)

'''

def powerset(S:set)-> list:
    Ps = [set()]
    for s in S:
        Ps+=  [ p | {s} for p in Ps]
    return Ps
if __name__ == '__main__':
    print(powerset({1,2,3}))
