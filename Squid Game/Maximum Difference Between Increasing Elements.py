class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mini=float("inf")
        diff=-1
        for i in range(len(nums)):
            mini=min(mini,nums[i])
            if nums[i]>mini:
                diff=max(diff,nums[i]-mini)
        return diff