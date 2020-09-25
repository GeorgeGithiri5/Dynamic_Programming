def permutationCoef(n,k):
    p = [[0 for i in range(k+1)] for j in range(n+1)]

    for i in range(n + 1):
        for j in range(min(i,k) + 1):
            if (j==0):
                p[i][j] = 1
            else:
                p[i][j] = p[i - 1][j] + (j*p[i - 1][j-1])

            if (j<k):
                p[i][j + 1] = 0
    return p[n][k]

n = 10
k = 2
print("Value of p(", n,",", k, ") is  ",permutationCoef(n,k),sep="")
