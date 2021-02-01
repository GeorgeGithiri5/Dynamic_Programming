def productSub(arr, k):
    n = len(arr)
    dp = [[0 for i in range(n+1)] for j in range(k+1)]
    for i in range(1, k+1):
        for j in range()