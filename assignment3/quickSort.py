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