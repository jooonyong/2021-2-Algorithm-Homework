###(1) Dijkstra algorithm
inf = 1000
w=[[0,7,4,6,1],[inf,0,inf,inf,inf],[inf,2,0,5,inf],[inf,3,inf,0,inf],[inf,inf,inf,1,0]]
n=5
f=set()
touch=n*[0]
length=n*[0]
save_length = n*[0]

for i in range(1,n):
    length[i] = w[0][i]

for j in range(1,n):
    min = inf
    for i in range(1,n):
        if(length[i]>=0 and length[i]<min):
            min = length[i]
            vnear = i
    f.add((touch[vnear],vnear))
    save_length[vnear] = min

    for i in range(1,n):
        if(length[vnear] + w[vnear][i] < length[i]):
            length[i] = length[vnear] + w[vnear][i]
            touch[i] = vnear
    length[vnear] = -1

print(f)
print("각 노드별 최단거리:",save_length)


###(2) 7-Queens Problem
def promising(i,col):
    switch = True
    k = 0
    while(switch and k<i):
        if(col[i]==col[k] or abs(col[i]-col[k]) == i-k):
            switch = False
        k=k+1
    return switch

count = 0
newlist = []

def queens(n,i,col):
    if(promising(i,col)):
        if(i==n-1):
            global count
            count = count+1  
            if(count ==2):
                print("두번째 해:",col)       
        else:
            for j in range(0,n):
                col[i+1] = j 
                queens(n,i+1,col)
                              

N=7
col=N*[0]

print("-----------------------")
print("N-Queens 문제")
queens(N,-1,col)
print("해의 총 개수 :",count)
