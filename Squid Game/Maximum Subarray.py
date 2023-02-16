class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=float("-inf")
        tot=0
        for i in range(len(nums)-1,-1,-1):
            tot=max(tot+nums[i],nums[i])
            maxi=max(tot,maxi)
        return maxi