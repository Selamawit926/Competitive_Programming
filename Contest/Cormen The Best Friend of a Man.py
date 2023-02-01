n=input().split(" ")
nums=input().split(" ")
k=int(n[1])
days=0
left=right=0
ans=[]
tot=count=0
diff=0
while right<len(nums):
    # print("Lso ",right,days)
    tot+=int(nums[right])
    # print("here: ",tot,nums[right])
    days+=1
    if days==2:
        if tot<k:
            # print("here: ",right," ",count," ",left)
            diff=k-tot
            tot+=diff
            count+=diff
            ans.append(int(nums[right])+diff)
        else:
            # print("whS ",tot,right)
            ans.append(int(nums[right]))
        days=1
        tot-=int(ans[left])
        # print("somthing, ",tot,right)
        left+=1
    else:
        ans.append(nums[right])
    right+=1

print(count)
for i in ans:
    print(i,end=" ")

