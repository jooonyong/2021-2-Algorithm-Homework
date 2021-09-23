"""
다음과 같은 수열을 생성하는 알고리즘을 설계한다.
1  1  2  4  8  16  32  64  128  256  ...
이 수열은 n번째 값을 f(n)으로 표시하면, f(n)= 2^(n-2) for n>=3 임을 쉽게
알 수 있다. 그렇지만 실험계산을 위해 f(n) 계산 방법을 다음과 같이 정의한다.
"""
import time

def Recursion_algorithm(n):
    if(n==1 or n==2):
        return 1
    else:
        sum = 0
        for i in range(1,n):
            sum += Recursion_algorithm(i)
        
        return sum

def Array_algorithm(n):
    array = []
    array.append(1)
    array.append(1)

    sum = 2
    for i in range(2,n):
        array.append(sum)
        sum += array[i]

    return array[n-1]


print(Array_algorithm(4))
