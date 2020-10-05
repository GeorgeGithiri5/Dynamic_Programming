MAX = 1000
lookup = [[0 for i in range(MAX)] for i in range(MAX)]

def countSeqUtil(n,diff):
    if abs(diff) > n:
        return 0
    if n == 1 and diff == 0:
        return 2
    if n == 1 and abs(diff) == 1:
        return 1
    if lookup[n][n+diff] !=-1:
        return lookup[n][n+diff]
    res = (countSeqUtil(n-1,diff+1) + 2*countSeqUtil(n-1,diff) + countSeqUtil(n-1,diff-1))

    lookup[n][n+diff] = res
    return res

def countSeq(n):
    global lookup
    lookup = [[-1 for i in range(MAX)] for i in range(MAX) ]
    res = countSeqUtil(n,0)
    return res

if __name__ == "__main__":
    n = 10
    print('Count of Seq is',countSeq(n))