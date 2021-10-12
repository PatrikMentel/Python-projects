import math
def comp(a1, a2):
    if a1 != None and a2 != None and len(a1) == len(a2):
        for numA in a1: 
            if numA**2 not in a2: return False
        for numB in a2:
            if math.sqrt(numB) not in a1: return False
        return True
    return False
	
a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
print(comp(a, b))

#return True if ([a**2 for a in l1]) in l2 else False