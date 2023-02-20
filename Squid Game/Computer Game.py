from collections import deque
cases=eval(input())
output=[]
for i in range(cases):
    cols=eval(input())
    row1=input()
    row2=input()
    rows=[row1,row2]
    lst=[]
    for j in range(2):
        lst.append([])
        for k in range(cols):
            lst[-1].append(rows[j][k])
    directions=[[0,1],[1,0],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
    queue=deque([[0,0]])
    found=False
    visited=set()
    while queue:
        curr=queue.popleft()
        if curr==[1,cols-1]:
            output.append("YES")
            found=True
            break
        for direction in directions:
            newR=direction[0]+curr[0]
            newC=direction[1]+curr[1]
            if 0<=newR<2 and 0<=newC<cols and (newR,newC) not in visited:
                if lst[newR][newC]=="0":
                    visited.add((newR,newC))
                    queue.append([newR,newC])
    if not found:
        output.append('NO')
for i in output:
    print(i)