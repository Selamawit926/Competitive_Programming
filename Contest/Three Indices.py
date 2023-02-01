import heapq
from os import popen

n=eval(input())
ans=[]
for i in range(n):
    num=input()
    line=input().split(" ")
    lst=[]
    for j in line:
        lst.append(int(j))
    #Simple implementation
    # first=0
    # second=1
    # third=2
    # found=False
    # while third<int(num):
    #     if lst[first]<lst[second] and lst[second]>lst[third]:
    #         found=True
    #         ans.append(["YES",[first+1,second+1,third+1]])
    #         break
    #     first+=1
    #     second+=1
    #     third+=1

    # if not found:
    #     ans.append(["NO"])

    #Heap implementation
    found=False
    heap=[]
    start=0
    end=len(lst)-1
    for i in range(len(lst)):
        heap.append((-lst[i],i))

    heapq.heapify(heap)
    while start<end:
        popped=heapq.heappop(heap)
        if popped[1]!=start and popped[1]!=end:
            ans.append(["YES",[popped[1],popped[1]+1,popped[1]+2]])
            found=True
            break
        else:
            if popped[1]==start:
                start+=1
            else:
                end-=1

    if not found:
        ans.append(["NO"])
        

count=0
for i in ans:
    if count>=1:
        print()
    for j in range(len(i)):
        if j==1:
            for num in i[j]:
                print(num, end=" ")
        else:
            print(i[j])
    count+=1
    
    
        
        