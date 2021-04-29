class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums)==0:
            return [-1,-1]
        
        lst=[]
        
        start=0
        end=len(nums)-1
        
        while start<=end:
            
            mid=(start+end)//2
            
            if nums[mid]==target and mid==0:
                lst.append(mid)
                break
            
            elif nums[mid]==target and nums[mid-1]<target:
                lst.append(mid)
                break
                
            elif nums[mid]==target and nums[mid-1]==target:
                end=mid-1
                
            elif nums[mid]>target:
                end=mid-1
                
            else:
                start=mid+1
                
                
        if len(lst)==0:
            return [-1,-1]
        
        start=0
        end=len(nums)-1
        while start<=end:
            
            mid=(start+end)//2
            
            if nums[mid]==target and mid==len(nums)-1:
                lst.append(mid)
                break
            
            elif nums[mid]==target and nums[mid+1]>target:
                lst.append(mid)
                break
                
            elif nums[mid]==target and nums[mid+1]==target:
                start=mid+1
                
            elif nums[mid]>target:
                end=mid-1
                
            else:
                start=mid+1
                
   
    
        return lst