import heapq
n= input().split(" ")
inp= input().split(" ")
lst=[int(x) for x in inp]
queries= int(n[2])
k=int(n[1])
heap=[]
output=[]
for i in range(queries):
    inp=input().split(" ")
    id=int(inp[0])
    index=int(inp[1])-1
    if id==1:
        heapq.heappush(heap,(-lst[index],index))
    else:
        count=0
        popped=[]
        ind=set()
        while count<k:
            if heap:
                online=heapq.heappop(heap)
                popped.append(online)
                ind.add(online[1])
            count+=1
        if index in ind:
            output.append("YES")
        else:
            output.append("NO")
        for item in popped:
            heapq.heappush(heap,item)
        
for i in output:
    print(i)