n=input()
inp=input()
lst=inp.split(" ")
nums=[int(i) for i in lst]
days=eval(input())
dayslst=[]
for i in range(days):
    dayslst.append(eval(input()))
output=[]
nums.sort()
for i in range(len(dayslst)):
    for j in range(len(nums)):
        if nums[j]>dayslst[i]:
            output.append(j)
            break
    if dayslst[i]>=nums[-1]:
        output.append(len(nums))
    # if dayslst[i]<nums[0]:
    #     output.append(0)
    # else:
    #     start=0
    #     end=len(nums)-1
    #     while start<end:
    #         mid=int(start+(end-start)/2)
    #         if nums[mid]<dayslst[i]:
    #             start=mid+1
    #         else:
    #             end=mid
    #     output.append(start+1)
for i in output:
    print(i)

