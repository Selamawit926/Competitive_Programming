from collections import deque
n=input()
inps=n.split(" ")
target=int(inps[1])
inp=input()
init=inp.split(" ")
lst=[int(i) for i in init]
lst.sort()
nums=deque(lst)
count=0
while nums:
    if nums[-1]>target:
        count+=1
        nums.pop()
    else:
        num=target//nums[-1]
        num+=1
        if len(nums)>=num:
            cnt=0
            while cnt<num-1:
                nums.popleft()
                cnt+=1
            count+=1
            nums.pop()
        else:
            break
print(count)