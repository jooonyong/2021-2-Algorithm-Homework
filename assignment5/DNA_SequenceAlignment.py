import utility
import numpy as np

a=['C','A','C','A','T','T','A','C','C']
b=['C','A','C','G','T','C','C','A']

m = len(a)  #9
n = len(b)  #8
table = [[0 for j in range(0,n+1)] for i in range(0,m+1)]
minindex = [[(0,0) for j in range(0,n+1)] for i in range(0,m+1)]

###틈 행과 틈 열을 채워 넣는다.
for j in range(n-1,-1,-1):
    table[m][j] = table[m][j+1] + 2

for i in range(m-1,-1,-1):
    table[i][n] = table[i+1][n] + 2


for i in range(m-1,-1,-1):
    for j in range(n-1, -1,-1):
        if a[i] == b[j]:
            penalty = 0
        else:
            penalty = 1

        temparr = []
        temparr.append(table[i+1][j+1]+penalty)
        temparr.append(table[i+1][j]+2)
        temparr.append(table[i][j+1]+2)
        table[i][j] = np.min(temparr)

i =0
j = 0
temptuple = (0,0)
while(i<m and j<n):
    if a[i] ==b[j]:
        penalty =0
    else:
        penalty = 1

    if table[i][j] == table[i+1][j+1] + penalty:
        minindex[i][j] = tuple(sum(elem) for elem in zip(temptuple,(1,1)))
        temptuple =minindex[i][j]
        i = i+1
        j = j+1
    elif table[i][j] == table[i+1][j] +2:
        minindex[i][j] = tuple(sum(elem) for elem in zip(temptuple,(1,0)))
        temptuple = minindex[i][j]
        i = i+1
    else:
        minindex[i][j] = tuple(sum(elem) for elem in zip(temptuple,(0,1)))
        temptuple = minindex[i][j]
        j = j+1
     

utility.printMatrix(table)

x=0
y=0

while(x<m and y<n):
    tx = x
    ty = y
    print(minindex[x][y])
    (x,y) = minindex[x][y]
    if x==tx+1 and y==ty+1:
        print(a[tx]," ",b[ty])
    elif x==tx and y ==ty+1:
        print(" - "," ",b[ty])
    else:
        print(a[tx], " ", " -")