class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        start=0
        end=len(nums)-1
        k=0
        
        if len(nums)==1:
            if nums[0]==target:
                return True
            
            return False
    
        
        while start<=end:
            
            mid=(start+end)//2
            # print(mid)
            if nums[mid-1]>nums[mid]:
                k=mid
                break
            
            elif nums[mid]>nums[end]:
                start=mid+1
                
            elif nums[mid]<nums[start]:
                end=mid-1 
            
            elif nums[mid]>nums[mid+1]:
                k=mid+1
                # print(k)
                break
            elif nums[mid]==nums[end] and nums[mid]>nums[start]:
                end=mid-1
                
            elif nums[mid]==nums[end] and nums[mid]<nums[start]:
                start=mid+1
                
            elif nums[mid]==nums[start] and nums[mid]>nums[end]:
                start=mid+1
                
            elif nums[mid]==nums[start] and nums[mid]<nums[end]:
                end=mid-1    
           
            else:
                k=self.check(start,mid,nums)
                break
    
        end=len(nums)-1
        start=0
        print(k)
        
        if nums[end]>target:
            start=k
               
        elif nums[end]<target:
            end=k-1
    
        else:
            return True
        
        
        while start<=end:
            
            mid=(start+end)//2
            
            if nums[mid]<target:
                start=mid+1
                
            elif nums[mid]>target:
                end=mid-1
                
            else:
                return True
                    
          
            
        return False
       
        
    def check(self,start,end,lst):
        
        for i in range(len(lst)-1):
            if lst[i]>lst[i+1]:
                return i+1
            
        return 0