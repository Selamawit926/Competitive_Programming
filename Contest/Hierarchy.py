import heapq
n=eval(input())
qualifications=input().split(" ")
m=eval(input())
nums=set()
impossible=False
# heap=[]
# incoming={}
# edges={}
# for i in range(1,n+1):
#     incoming[i]=0
#     edges[i]=[]

di={}
for i in range(m):
    line=input().split(" ")
    first=int(line[0])
    second=int(line[1])
    cost=int(line[2])
    # if int(qualifications[first-1])<=int(qualifications[second-1]):
    #     impossible=True
    
    # cost=(int(line[2]),int(line[0]),int(line[1]))
    # incoming[int(line[1])]+=1
    # edges[int(line[0])].append(cost)
    nums.add(second)
    if second in di:
        di[second]=min(cost,di[second])
    else:
        di[second]=cost

# # print(incoming)
# # print(edges)
if len(nums)!=n-1:
    print(-1)
else:
    print(sum(di.values()))    









#     for i in incoming:
#         if incoming[i]==0:
#             for j in edges[i]:
#                 heap.append(j)

#     heapq.heapify(heap)
#     tot=0
#     while heap:
#         popped=heapq.heappop(heap)
#         incoming[popped[2]]-=1
#         if incoming[popped[2]]==0:
#             tot+=popped[0]
#             for i in edges[popped[2]]:
#                 heapq.heappush(heap,i)
#     print(tot)
