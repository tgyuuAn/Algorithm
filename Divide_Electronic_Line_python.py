from collections import defaultdict

def findParent(parent,x):
    if x!=parent[x]:
        parent[x] = findParent(parent,parent[x])
    return parent[x]


def unionParent(parent,a,b):
    a = findParent(parent,a)
    b = findParent(parent,b)
    if a>b:
        parent[a] = b
    else:
        parent[b] = a

def solution(n, wires):
    answer = 101
    dic = {}
    dic2 = defaultdict(int)
    
    for i in range(len(wires)):
        temp = wires.pop(i)
        
        dic2.clear()
        
        for x in range(1,n+1):
            dic[x] = x
        
        for x in wires:
            unionParent(dic,x[0],x[1])

        for x in range(1,n+1):
            findParent(dic,x)

        for y in dic.values():
            dic2[y] += 1
        
        aa = list(dic2.values())
        answer = min(answer,abs(aa[1] - aa[0]))

        wires.insert(i,temp)
    
    return answer