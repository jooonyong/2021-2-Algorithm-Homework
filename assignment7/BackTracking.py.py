#부분집합의 합
number_of_element = 6
element = [1,2,3,4,5,6]
Sum = 11

def promising1(i,weight, total):
    if((weight+total >= Sum) and (weight == Sum or weight + element[i+1]<=Sum)):
        return True
    else:
        return False

#sum of set
def sum_of_set(i,weight, total, include):
    if(promising1(i,weight,total)):
        if(weight == Sum):
            print(include)
        else:
            include[i+1] = 1
            sum_of_set(i+1,weight+element[i+1],total-element[i+1],include)
            include[i+1] = 0
            sum_of_set(i+1,weight,total-element[i+1],include)


print("items = ",element, "W =", Sum)
include = number_of_element*[0]
total = 0
for k in element:
    total = total+k
sum_of_set(-1,0,total,include)


#M-Coloring Algorithm
n=5
W=[[0,1,1,0,1],[1,0,1,0,0],[1,1,0,1,1],[0,0,1,0,1],[1,0,1,1,0]]
vcolor = n*[0]
m=3     

def promising2(i, vcolor):
    switch = True
    j = 0
    while(j<i and switch):
        if(W[i][j] == 1 and vcolor[i]==vcolor[j]):
            switch = False
        j = j+1
    return switch

def color(i, vcolor):
    if(promising2(i,vcolor)):
        if(i == n-1):
            print(vcolor)
        else:
            for j in range(0,3):
                vcolor[i+1] = j
                color(i+1,vcolor)

print("---------------------")
print("3-Color promblem:")
color(-1,vcolor)