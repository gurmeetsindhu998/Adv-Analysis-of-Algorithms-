from bcom import *
E = 'even'
D = 'odd'

Q1q0 = E
df = {(E, 0) : (E, 0, R) , (E, 1) : (D, 1, R) , (E, b) : (h, 0, R) ,
 (D, 0) : (D, 0, R) , (D, 1) : (E, 1, R) , (D,b) : (h, 1 , R) }

Tins = "00010" 
run(Tins,df,q0 = Q1q0)
start(Tins,df,q0 = Q1q0)
