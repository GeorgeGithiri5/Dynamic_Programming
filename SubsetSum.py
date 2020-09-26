def isSubsetSum(set,n,sum):
    subset = ([[False for i in range(sum + 1)]
    for i in range(n+1) ])

    for i in range(n+1):
        subset[i][0] = True
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if j<set[i-1]:
                subset[i][j] = subset[i - 1][j]
            if j>=set[i-1]:
                subset[i][j] = (subset[i-1][j] or subset[i - 1][j-set[i-1]])
    return subset[n][sum]

if __name__ == '__main__':
    set = [3,34,4,12,5,2]
    sum = 7
    n = len(set)
    if (isSubsetSum(set,n,sum) == True):
        print("Found a subset with given sum")
    else:
        print("No subset with given sum")