class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        return self.helper(nums,k)-self.helper(nums,k-1)

    def helper(self,nums,k):
        left=good=right=0
        count=defaultdict(int)
        while right<len(nums):
            if count[nums[right]]==0:
                k-=1
            count[nums[right]]+=1
            while k<0:
                count[nums[left]]-=1
                if count[nums[left]]==0:
                    k+=1
                left+=1
            good+=right-left+1
            right+=1
        return good