class area:
    def __init__(self,a,b):
        self.a = a
        self.b = b

def maxSurvival(A,B,X,Y,Z,last,memo):
    if (A<=0 or B<=0):
        return 0
    cur = area(A,B)
    for ele in memo.keys():
        if (cur.a == ele.a and cur.b == ele.b):
            return memo[ele]
    if (last == 1):
        temp = 1 + max(maxSurvival(A + Y.a,B + Y.b,X,Y,Z,2,memo),maxSurvival(A + Z.a,B+Z.b,X,Y,Z,3,memo))
    elif (last == 2):
        temp = 1 + max(maxSurvival(A + X.a,B+X.b,X,Y,Z,1,memo),maxSurvival(A+Z.a,B + Z.b,X,Y,Z,3,memo))
    elif (last == 3):
        