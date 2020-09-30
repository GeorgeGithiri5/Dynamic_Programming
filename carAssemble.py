def carAssembleTime(a,t,e,x):
    n = len(a[0])
    first = e[0] + a[0][0]

    second = e[1] + a[1][0]
    for i in range(1,n):
        up = min(first + a[0][i],second + t[1][i] + a[0][i])
        down = min(second + a[1][i],first + t[0][i] + a[1][i])
        first,second = up,down
    first += x[0]
    second += x[1]
    return min(first,second)

a = [[4,5,3,2],[2,10,1,4]]
t = [[0,7,4,5],[0,9,2,8]]
e = [10,12]
x = [18,7]
print(carAssembleTime(a,t,e,x))