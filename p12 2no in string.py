#HW
from bcom import *

# 1 bit inputTM descriptions
T = "00_111001" # blankon left and on right #first bit is input and other bits are string to look in
rwh = 0 # rewrite head at index 0
q0 = 0
# instruction format: (ps, in): (ns, out, move)
df=0
"""
wrong
df = {
    (0,0):(1,0,R), (0,1):(2,1,R), (0,b):(h,b,R), 
(1,0):(3,0,R), (1,1):(4,1,R), (1,b):(h,b,R),
(2,0):(8,0,R),(2,1):(3,1,R),(2,b):(h,b,R),
(3,0):(3,0,R),(3,1):(3,0,R) ,(3,b):(5,0,R),
(4,0):(6,0,R),(4,1):(3,1,R),(4,b):(7,b,R),
(5,0):(h,1,R),(5,1):(h,1,R),(5,b):(h,1,R),
(6,0):(3,0,R),(6,1):(4,1,R) ,(6,b):(7,b,R),
(7,0):(h,0,R),(7,1):(h,0,R) ,(7,b):(h,0,R),
(8,0):(3,0,R),(8,1):(6,1,R) ,(8,b):(7,b,R)}
"""

if __name__=="__main__":
# put all your testing code within this if
    print(T,rwh)
    print(Utm(T,df))



"""
A 
diagram

"""
#B
#list comprihension(set)
#touring machine abstract problem 3bit number
#chalanging 
#generator: infinty num

#reverse string 
#prime num