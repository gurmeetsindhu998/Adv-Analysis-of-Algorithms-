from bcom import *

# 1 bit inputTM descriptions
T = "011111" # blankon left and on right #first bit is input and other bits are string to look in
rwh = 0 # rewrite head at index 0
q0 = 0
df = {(0,0):(1,0,R), (0,1):(2,1,R), (0,b):(h,b,R), 
(1,0):(4,0,R), (1,1):(1,1,R), (1,b):(3,b,R),
(2,0):(2,0,R),(2,1):(4,1,R),(2,b):(3,b,R),(3,0):(h,0,R),(3,1):(h,0,R) ,(3,b):(h,0,R),
(4,0):(4,0,R),(4,1):(4,1,R),(4,b):(5,b,R),(5,0):(h,1,R),(5,1):(h,1,R),(5,b):(h,1,R) }

if __name__=="__main__":
# put all your testing code within this if
    print(T,rwh)
    print(Utm(T,df))