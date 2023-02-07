class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # maxi=max(nums)
        # mini=min(nums)
        # ranges=maxi-mini
        # count=[0]*(ranges+1)
        # for i in nums:
        #     count[i+ranges]+=1
        # print(count)
        nums.sort()
        return nums[len(nums)-k]