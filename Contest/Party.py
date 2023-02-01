from collections import deque
n=eval(input())
di={}
indegree={}
for i in range(1,n+1):
    inp=eval(input())
    if inp in di:
        di[inp].append(i)
    else:
        di[inp]=[i]

    if inp==-1:
        indegree[i]=0
    else:
        indegree[i]=1
# print(di)
# print(indegree)
queue=deque()
for i in indegree:
    if indegree[i]==0:
        queue.append((i,1))
level=0
while queue:
    popped=queue.popleft()
    if popped[1]>level:
        level+=1
    if popped[0] in di:
        for i in di[popped[0]]:
            indegree[i]-=1
            if indegree[i]==0:
                queue.append((i,popped[1]+1))
print(level)

