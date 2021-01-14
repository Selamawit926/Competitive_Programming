def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    j=len(nums)-1
    for i in range(0,len(nums)):
        if nums[i]>nums[j]:
            nums[i],nums[j]=nums[j],nums[i]
            j-=1
            
            print(nums)

    
    print(nums)
        
sortColors([2,0,2,1,1])