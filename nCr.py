def nCrModp(n,r,p):
    if(r>n-r):
        r = n - r
    C = [0 for i in range(r+1)]
    C[0] = 1
    for i in range(1,n+1):
        for j in range(min(i,r),0,-1):
            C[j] = (C[j] + C[j-1]) % p
    return C[r]

n = 10
r =2
p = 13
print('Value of nCr % p is',nCrModp(n,r,p))       
