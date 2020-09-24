def maxDivide(a,b):
    while a % b == 0:
        a = a / b
    return a

def isUgly(no):
    no = maxDivide(no,2)
    no = maxDivide(no,3)
    no = maxDivide(no,5)

    return 1 if no == 1 else 0

def getNthUglyNo(n):
    i = 1
    count = 1
    while n > count:
        i += 1
        if isUgly(i):
            count += 1
    return i

no = getNthUglyNo(150)
print("150th ugly no. is ", no)

# Using Dynamic Programming
def getNthUglyNo(n):
    ugly = [0]
    ugly[0] = 1
    i2 = i3 = i5 = 0

    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5

    for z in range(1,n):
        ugly[1] = min(next_multiple_of_2,next_multiple_of_3,next_multiple_of_5)

        if ugly[1] == next_multiple_of_2:
            i2 += z
            next_multiple_of_2 = ugly[i2]*2
        if ugly[1] == next_multiple_of_3:
            i3 += z
            next_multiple_of_3 = ugly[i3]*3
        if ugly[1] == next_multiple_of_5:
            i5 += z
            next_multiple_of_5 = ugly[i5]*5

    return ugly[-z]

def main():
    n = 150
    print (getNthUglyNo(n))

if __name__ == "__main__":
    main()

