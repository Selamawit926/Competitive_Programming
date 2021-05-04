class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # print(nums)
        if len(nums)<3:
            return 0
        count=0
        di={}
        prev=nums[0]
        prevdiff=0
        for i in range(1,len(nums)):
            diff=nums[i]-prev
            if diff in di:
                if diff==prevdiff:
                    count+=di[diff]
                    di[diff]+=1
                    
                else:
                    di[diff]=1
                
            else:
                di[diff]=1
                
            prev=nums[i]
            prevdiff=diff
            
        return count