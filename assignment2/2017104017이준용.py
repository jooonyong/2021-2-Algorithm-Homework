S = [11,5,2,16,12,1,8,15,6,14,9,3,10,7,13,4]
extra1 = 0
extra2 = 0

#공간복잡도 = 2n인 mergesort
def merge1(list1, list2):
    result = []
    while len(list1)>0 or len(list2)>0:
        if len(list1) >0 and len(list2)>0:
            if list1[0]<=list2[0]:
                result.append(list1[0])
                list1 = list1[1:]
            else:
                result.append(list2[0])
                list2 = list2[1:]
        elif len(list1)>0:
            result.append(list1[0])
            list1 = list1[1:]
        elif len(list2)>0:
            result.append(list2[0])
            list2 = list2[1:]
    
    return result


def mergesort1(list):
    if len(list)<=1:
        return list
    mid = len(list)//2
    leftList = list[:mid]
    rightList = list[mid:]
    
    global extra1
    leftList = mergesort1(leftList)
    extra1 = extra1 + len(leftList)
    rightList = mergesort1(rightList)
    
    
    return merge1(leftList, rightList)

#공간복잡도 = n인 mergesort
def merge2(low,mid, high): 
    i = low
    j = mid+1
    k = low
    U = S[:]
    
    while(i<=mid and j<=high):
        if(S[i]<S[j]):
            U[k] = S[i]
            i = i+1
        else:
            U[k] = S[j]
            j = j+1
        k = k+1
   
    if(i>mid):
        while(j<=high):
            U[k] = S[j]
            k = k+1
            j = j+1
    else:
        while(i<=mid):
            U[k] = S[i]
            k = k+1
            i = i+1
    
    S[:] = U[:]
    return S

def mergesort2(low, high):
    if(low<high):
        mid = (low+high)//2
        mergesort2(low,mid)
        mergesort2(mid+1, high)
        merge2(low,mid,high)
    global extra2
    extra2 = high-low +1  

    
print("Before MergeSort1: ",S)
print("After MergeSort1: ",mergesort1(S))
print("MergeSort1 additionally used ",extra1)

print("Before MergesSort2: ",S)
mergesort2(0,15)
print("After MergeSort2: ",S)
print("MergeSort2 additionally used ",extra2)
