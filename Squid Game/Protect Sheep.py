def check(lst,i,j,directions,pos,visited):
    for direction in directions:
        newR=direction[0]+i
        newC=direction[1]+j
        if 0<=newR<len(lst) and 0<=newC<len(lst[newR]) and (newR,newC) not in visited:
            visited.add((newR,newC))
            if lst[i][j]=="W" and lst[newR][newC]=="S":
                pos[0]=False
                break
            if lst[newR][newC]==".":
                check(lst,newR,newC,directions,pos,visited)
            if lst[newR][newC]=="S":
                lst[i][j]="D"
    return

n=input()
num=n.split(" ")
row=int(num[0])
col=int(num[1])
lst=[]
for i in range(row):
    vals=input()
    lst.append([])
    for j in range(col):
        lst[-1].append(vals[j])
directions=[[0,1],[1,0],[-1,0],[0,-1]]
pos=[True]
visited=set()
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if lst[i][j]=="W":
            pos=[True]
            check(lst,i,j,directions,pos,visited)
            if not pos[0]:
                break
if not pos[0]:
    print('No')
else:
    print("Yes")
    for i in lst:
        print(i)