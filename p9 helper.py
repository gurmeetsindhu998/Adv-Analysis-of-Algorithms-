from bcom import *
#eg TM file
# in the TM file
# from bcom import *

# TM descriptions
# eg: parity tm def 

# tape: require def T, rwh
T = "0111"
rwh = 0

q0 = 0 # startup
# req def df (ps,ins):(ns,outs,move)
df = {(0,0):(0,0,R), (0,1):(1,1,R), (0,b):(2,b,R), #delta function
(1,0):(1,0,R), (1,1):(0,1,R), (1,b):(3,b,R),
(2,b):(h,0,R), (3,b):(h,1,R)}

# testing
print(T,rwh)
print(Utm(T,df))


"""
testing for nand
print(T,rwh)
print(Utm(T,df))
"""

