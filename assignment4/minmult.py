import utility
import numpy as np

def order(p,i,j):
    if i==j:
        print("A",i,end='')
    else:
        k=p[i][j]
        print("(",end='')
        order(p,i,k)
        order(p,k+1,j)
        print(")",end='')

d=[5,2,3,4,6,7,8]
n=len(d)-1  

m=[[0 for j in range(0,n+1)] for i in range(0,n+1)]
p=[[0 for j in range(0,n+1)] for i in range(0,n+1)]


for diagonal in range(1,n):
    for i in range(1, n-diagonal+1):
        j = i+diagonal
        arr = []
        for k in range(i,j):
            arr.append(m[i][k]+m[k+1][j]+d[i-1]*d[k]*d[j])
        m[i][j] = np.min(arr)
        p[i][j] = np.argmin(arr)+i


utility.printMatrix(m)
print()
utility.printMatrix(p)
order(p,1,6)
