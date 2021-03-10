def search(nums, target):
        
    start=0
    end=len(nums)-1
    k=0
    while start<=end:
        
        mid=(start+end)//2
        
        if nums[mid-1]>nums[mid]:
            k=mid
            break
        
        
        if nums[mid]>nums[end]:
            start=mid+1
            
            
        elif nums[mid]<nums[end]:
            end=mid-1
        
    
        
            
    
    
    end=len(nums)-1
    start=0
    print(k)
    
    if nums[end]>target:
        start=k
        
        
    elif nums[end]<target:
        end=k-1

    else:
        return True
    
    # print(start,end, end=" ")
    
    while start<=end:
        
        mid=(start+end)//2
        
        if nums[mid]<target:
            start=mid+1
            
        elif nums[mid]>target:
            end=mid-1
            
        else:
            return True
                
        
        
    return False


print(search([1,0,1,1,1],0))