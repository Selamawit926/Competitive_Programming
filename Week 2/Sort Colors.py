class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0,len(nums)):
            for j in range(len(nums)-1,-1,-1):
                if i==j:
                    break
                elif nums[i]>nums[j]:
                       nums[i],nums[j]=nums[j],nums[i]
                     