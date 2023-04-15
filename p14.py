Z = {0, 1}
# A -> Y
allfun1 = [{0:y1, 1:y0} for y1 in Z for y0 in Z]
print(allfun1)



#HW
"""
Z = {0, 1}

(0,0) -> 0

(0,1) -> 0

(1,0) -> 0

(1,1) -> 1
"""

allfun = [{(0,0):y0, (0,1):y1,(0,1):y2,(1,1):y3} for y0 in Z for y1 in Z for y2 in Z for y3 in Z]
print(allfun)
andfun = allfun[1]
print(andfun([0][1]))