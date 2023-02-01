from collections import deque
from math import inf
n=eval(input())
ans=[]
for i in range(n):
    line=input()
    seen=set()
    passed=deque()
    mini=float("inf")
    left=0
    right=0
    count=[0,0,0]
    while left<=right:
        if min(count)!=0:
            mini=min(mini,right-left)
            count[int(line[left])-1]-=1
            left+=1
        else:
            if right<=len(line)-1:
                index=int(line[right])-1
                count[index]+=1
                right+=1
            else:
                left+=1

    if mini==float("inf"):
        mini=0
    ans.append(mini)

for i in ans:
    print(i)
