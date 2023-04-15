from bcom import *

# 1 bit inputTM descriptions
T = "100" # blankon left and on right
rwh = 0 # rewrite head at index 0
q0 = 0
# instruction format: (ps, in): (ns, out, move)
df = delta = {(0,0):(1,0,R), (0,1):(2,1,R), (0,b):(h,b,R), 
(1,0):(3,0,R), (1,1):(3,1,R), (1,b):(h,b,R),
(2,0):(3,0,R),(2,1):(4,1,R),(2,b):(h,b,R),
(3,0):(h,1,R),(3,1):(h,1,R) ,(3,b):(3,1,R),
(4,0):(h,0,R),(4,1):(h,0,R),(4,b):(h,0,R)}
# testing
if __name__=="__main__":
# put all your testing code within this if
    print(T,rwh)
    print(Utm(T,df))