class Solution:
    def search(self, nums: List[int], target: int) -> int:
     #iterative 
    
        left=0
        right=len(nums)-1
        

        while left<=right:
            mid=(left+right)//2
            
            if nums[mid]>target:
                right=mid-1
                

            elif nums[mid]<target:
                left=mid+1
                

            else:
                return mid

        
        return -1


        #recursion
        
        left=0
        right=len(nums)-1

        return self.check(nums,target,left,right)
        
        
        
    def check(self,nums,target,left,right):
        
        if left<=right:
        
            mid=(left+right)//2

            if nums[mid]==target:
                return mid

            if nums[mid]<target:
                left=mid+1
                return self.check(nums,target,left,right)

            elif nums[mid]>target:
                right=mid-1
                return self.check(nums,target,left,right)
            
        else:
            return -1