class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        seen=set()
        count=0
        nums.sort()
        i=len(nums)-1
        while i>=0:
            if nums[i] not in seen:
                seen.add(nums[i])
                count+=1
                if count==3:
                    return nums[i]
            i-=1
        return max(nums)