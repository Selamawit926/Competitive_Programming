n=input()
nums=input().split(" ")
lst=[]
for i in nums:
    lst.append(int(i))
if len(lst)==1:
    print(1)
else:
    left=0
    right=1
    count=1
    maxi=0
    while right<len(lst):
        if lst[right]<=lst[left]:
            # print(count,lst[right],lst[left])
            maxi=max(maxi,count)
            left=right
            right+=1
            count=1
        else:
            right+=1
            count+=1
            left+=1

    maxi=max(count,maxi)
    print(maxi)