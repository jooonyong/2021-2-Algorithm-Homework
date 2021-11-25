import queue

n=4
W=9
p=[20,40,24,40]
w=[2,5,4,8]
maxp = 0
include = [0,0,0,0]
bestset = [0,0,0,0]
count_node = 0

def promising(i, weight, profit):
    global maxp
    if(weight > W):
        return False
    else:
        j = i+1
        bound = profit
        totweight = weight
        
        while(j<n and totweight+w[j] <=W):
            totweight = totweight+w[j]
            bound = bound +p[j]
            j+=1
        
        k = j
        
        if(k<n):
            bound = bound + (W-totweight) * p[k]/w[k]

        return bound > maxp
    

def knapsack(i, profit, weight):
    global bestset
    global maxp
    global count_node

    if(weight <= W and profit>maxp):
        maxp = profit
        bestset = include[:]
    
    if(promising(i,weight, profit)):
        include[i+1] = 1
        knapsack(i+1,profit+p[i+1], weight+w[i+1])
        include[i+1] = 0
        knapsack(i+1, profit, weight)
    
    count_node +=1

knapsack(-1,0,0)
print("MAX Profit: ",maxp)
print("BEST SET: ",bestset)
print("TOTAL NODE: ",count_node)
print("---------------------------")

n=4
W=9
p=[20,40,24,40]
w=[2,5,4,8]
maxProfit = 0
count_node = 1

class Node:
    def __init__(self,level,weight, profit,bound,include):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.bound = bound
        self.include = include
    def __lt__(self,other):
        return (self.bound > other.bound) - (self.bound < other.bound) 


def compBound(u):
    if u.weight >=W:
        return 0
    else:
        result = u.profit
        j = u.level +1
        totweight = u.weight
        while(j<n and totweight+w[j]<=W):
            totweight = totweight + w[j]
            result = result + p[j]
            j +=1
        k = j
        if(k<n):
            result = result + (W-totweight)*p[k]/w[k]
        return result


def kp_Best_FS():
    global maxProfit
    global bestset
    temp = n*[0]
    u = Node(0,0,0,0.0,temp)
    v = Node(-1,0,0,0.0,temp)
    v.bound = compBound(v)
    q = queue.PriorityQueue()
    q.put(v)

    while(not q.empty()):
        if not q.empty():
            node1 = q.get()
            global count_node
            count_node +=1

        if(node1.bound > maxProfit):
            u.level = node1.level +1
            u.weight = node1.weight + w[u.level]
            u.profit = node1.profit + p[u.level]

            if(u.weight <= W and u.profit > maxProfit):
                maxProfit = u.profit
            u.bound = compBound(u)
            if(u.bound > maxProfit):
                q.put(u)

            u.weight = node1.weight
            u.profit = node1.profit
            u.bound = compBound(u)
            if(u.bound > maxProfit):
                q.put(u)

kp_Best_FS()
print("MAX Profit: ",maxProfit)
print("Total Node: ",count_node)
