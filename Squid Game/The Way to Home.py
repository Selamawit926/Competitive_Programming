from collections import deque
n=input()
lst=n.split(" ")
nums=input()
queue=deque([(0,0)])
home=False
d=int(lst[1])
while queue:
    curr=queue.popleft()
    if curr[0]==len(nums)-1:
        # print(curr)
        home=True
        print(curr[1])
        break
    for i in range(d,0,-1):
        ind=i+curr[0]
        if ind<len(nums) and nums[ind]=="1":
            queue.append((ind,curr[1]+1))
            break
if not home:print(-1)
            


