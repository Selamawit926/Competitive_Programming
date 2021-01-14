nums=[5,7,1,8]
x=0
for i in range(0,len(nums)-1):
    if nums[i]>nums[i+1]:
        x+=1

if x>1:
    print(False)
else:
    print(True)

    # if nums[i]<nums[i+1] and nums[i]<nums[i-1]:
    #     nums[i]=nums[i+1]
    #     print(x)
    #     x+=1
    #     print(x)
    # elif nums[i]>nums[i+1]:
    #     nums[i]=nums[i+1]-1
    #     x+=1
    #     print(x)

    # if i==0 and nums[i]<nums[i+1]:
    #     break
    # if i==0 and nums[i]>nums[i+1]:
    #     nums[i]=nums[i+1]
    #     x+=1
    # if nums[i]<nums[i+1] and nums[i]<nums[i-1]:
    #     nums[i]=nums[i+1]
    #     x+=1
    # elif nums[i]>nums[i+1]:
    #     nums[i]=nums[i+1]
    #     x+=1

# if x>1:
#     print(False)
# elif len(nums)==1 or x<=1:
#     print(True)

