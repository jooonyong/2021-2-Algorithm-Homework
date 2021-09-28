import random
import numpy as np
from matplotlib import pyplot as plt

compare_count = 0

#QuickSort 알고리즘
def quickSort(s,low, high):
    if high>low:
        partition(s,low,high)
        quickSort(s,low, partition(s,low,high)-1)
        quickSort(s,partition(s,low,high)+1,high)
    
def partition(s,low,high):
    pivotitem = s[low]
    j = low
    for i in range(low+1,high+1):
        if s[i]<pivotitem:
            j=j+1
            temp = s[j]
            s[j] = s[i]
            s[i] = temp
            global compare_count
            compare_count = compare_count+1
    
    pivotpoint = j
    temp = s[low]
    s[low] = s[pivotpoint]
    s[pivotpoint] = temp
    return pivotpoint


numberOfData = [8,16,24,32,40]

arr=[]
compare_count_arr = []


for i in range(0,5):    #numberOfData 반복
    compare_count = 0
    for k in range(0,20):   #20번 반복
        arr =[]
        for j in range(numberOfData[i]):
            arr.append(random.randrange(numberOfData[i]))
        quickSort(arr,0,numberOfData[i]-1)

    average_compare_count = compare_count/20
    compare_count_arr.append(average_compare_count)

print(compare_count_arr)

plt.plot(numberOfData,compare_count_arr)
plt.show()



#행렬 곱셉을 위한 Strassen 알고리즘
def strassen(n,A,B,C):
    threshold = 2
    A11 = np.array([[A[rows][cols] for cols in range(int(n/2))]for rows in range(int(n/2))])
    A12 = np.array([[A[rows][cols] for cols in range(int(n/2), n)]for rows in range(int(n/2))])
    A21 = np.array([[A[rows][cols] for cols in range(int(n/2))]for rows in range(int(n/2),n)])
    A22 = np.array([[A[rows][cols] for cols in range(int(n/2),n)]for rows in range(int(n/2),n)])
    B11 = np.array([[B[rows][cols] for cols in range(int(n/2))]for rows in range(int(n/2))])
    B12 = np.array([[B[rows][cols] for cols in range(int(n/2),n)]for rows in range(int(n/2))])
    B21 = np.array([[B[rows][cols] for cols in range(int(n/2))]for rows in range(int(n/2),n)])
    B22 = np.array([[B[rows][cols] for cols in range(int(n/2),n)]for rows in range(int(n/2),n)])

    # print(A11,A12,A21,A22,B11,B12,B21,B22)
    if (n<=threshold):
        C = np.array(A) @ np.array(B)
    else:
        M1 = M2 = M3 = M4 = M5 = M6 = M7 = np.array([])
        M1 = strassen(int(n/2),(A11+A22),(B11+B22),M1)
        M2 = strassen(int(n/2),(A21+A22),B11,M2)
        M3 = strassen(int(n/2),A11,(B12-B22),M3)
        M4 = strassen(int(n/2),A22,(B21-B11),M4)
        M5 = strassen(int(n/2),(A11+A12),B22,M5)
        M6 = strassen(int(n/2),(A21-A11),(B11+B12),M6)
        M7 = strassen(int(n/2),(A12-A22),(B21+B22),M7)

        C = np.vstack([np.hstack([M1+M4-M5+M7,M3+M5]),np.hstack([M2+M4,M1+M3-M2+M6])])
    
    return C

    
n=4
A=[[1,2,0,2],[3,1,0,0],[0,1,1,2],[2,0,2,0]]
B=[[0,3,0,2],[1,1,4,0],[1,1,0,2],[0,5,2,0]]
C= np.array(A)@np.array(B)
D= [[0 for cols in range(n)] for rows in range(n)]
print(C)
D= strassen(n,A,B,D)
print(D)


