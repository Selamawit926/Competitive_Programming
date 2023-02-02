class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count=0
        while max(nums)!=0:
            mini=float('inf')
            count+=1
            for i in nums:
                if i>0:
                    mini=min(mini,i)
            for i in range(len(nums)):
                if nums[i]!=0:
                    nums[i]-=mini
        return count