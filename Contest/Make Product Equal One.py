n=input()
lst=input().split(" ")
nums=[]
for i in lst:
    nums.append(int(i))

coins=0
maxi=-(10**10)
negatives=0
zeros=0
for i in range(len(nums)):
    if nums[i]>0:
        coins+=nums[i]-1
    elif nums[i]==0:
        zeros+=1
    else:
        negatives+=1
        if nums[i]>maxi:
            if maxi!=-(10**10):
                coins+=abs(maxi+1)
            maxi=nums[i]
        else:
            coins+=abs(nums[i]+1)

if negatives%2!=0:
    if zeros > 0:
        coins+=zeros+(abs(maxi+1))
    else:
        coins+=abs(maxi-1)
else:
    if maxi!=-(10**10):
        coins+=abs(maxi+1)
    coins+=zeros

print(coins)

        

