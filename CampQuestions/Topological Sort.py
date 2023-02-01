from collections import deque
from typing import Deque


def dfs(di,node,lst,visited,saved):
    for i in range(len(di[node])):
        if di[node][i] not in visited:
            lst.append(di[node][i])
            visited.add(di[node][i])
            dfs(di,di[node][i],lst,visited,saved)
        else:
            # print(di[node][i])
         
            if di[node][i] in saved:
                lst+=saved[di[node][i]]
       
            # print(lst)
    return

def sort(num,edges):
    di={}
    visited=set()

    for i in range(1,num+1):
        di[i]=[]
        for j in range(1,num+1):
            if i!=j:
                if (i,j) not in edges:
                    di[i].append(j)
    maxi=0
    final=[]
    saved={}
    for node in di:
        if node not in visited:
            lst=[node]
            visited.add(node)
            saved[node]=deque()
            count=dfs(di,node,lst,visited,saved)
            for num in lst:
                saved[node].append(num)
            print(lst," for: ",node)
            if len(lst)>=maxi:
                final=lst
                maxi=len(lst)
    print(final)

n=eval(input())
for i in range(n):
    test=input().split(" ")
    num=int(test[0])
    remove=int(test[1])
    edges=set()
    for j in range(remove):
        banned=input().split(" ")
        edges.add((int(banned[0]),int(banned[1])))
    # print(edges)
    sort(num,edges)