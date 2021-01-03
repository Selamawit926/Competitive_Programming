def twoSum(nums,target):
        lst=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:  
                    lst.append(i)
                    lst.append(j)       
        return lst


inp=input("Enter numbers here: ")
target=eval(input("Enter target number: "))
inp2=inp.split()
nums=[eval(inp) for inp in inp2]

print(twoSum(nums,target))
