from collections import deque
n=input().split(" ")
start=[int(n[0]),int(n[1])]
end=[int(n[2]),int(n[3])]

rook=0
if start[0]-end[0] !=0:
    rook+=1
if start[1]-end[1]!=0:
    rook+=1

bishop=0
if abs(start[0]-end[0])==abs(start[1]-end[1]):
    bishop=1
elif abs(start[0]-end[0])==0 and abs(start[1]-end[1])%2==0:
    bishop=2
elif abs(start[1]-end[1])==0 and abs(start[0]-end[0])%2==0:
    bishop=2
elif abs(start[1]-end[1])%2==0 and abs(start[0]-end[0])%2==0:
    bishop=2
elif abs(start[1]-end[1])%2!=0 and abs(start[0]-end[0])%2!=0:
    bishop=2

king=0
directions=[[0,1],[1,0],[1,1],[-1,0],[0,-1],[-1,-1],[-1,1],[1,-1]]
queue=deque()
newStart=start
visited=set()
for direction in directions:
    newRow=newStart[0]+direction[0]
    newCol=newStart[1]+direction[1]
    queue.append([1,newRow,newCol])
    visited.add((newRow,newCol))
while queue:
    popped=queue.popleft()
    if [popped[1],popped[2]]==end:
        king=popped[0]
        break
    for direction in directions:
        newRow=popped[1]+direction[0]
        newCol=popped[2]+direction[1]
        if (newRow,newCol) not in visited:
            queue.append([popped[0]+1,newRow,newCol])
            visited.add((newRow,newCol))

        
# if abs(start[0]-end[0])==0:
#     king+=abs(start[1]-end[1])

# elif abs(start[1]-end[1])==0:
#     king+=abs(start[0]-end[0])
# else:
#     diff=[]
#     if start[0]>end[0] and start[1]>end[1]:
#         diff=[-1,-1]
#     elif start[0]<end[0] and start[1]>end[1]:
#         diff=[1,-1]
#     elif start[0]>end[0] and start[1]<end[1]:
#         diff=[-1,1]
#     else:
#         diff=[1,1]
#     while start[0]!=end[0] and start[1]!=end[1]:
#         start[0]+=diff[0]
#         start[1]+=diff[1]
#         king+=1
#     if start[0]==end[0]:
#         king+=abs(end[1]-start[1])

#     else:
#         king+=abs(end[0]-start[0])

print(rook,bishop,king)
