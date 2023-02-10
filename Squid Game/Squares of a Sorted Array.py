class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lst=deque()
        left=0
        right=len(nums)-1
        while len(lst)<len(nums):
            if abs(nums[left])>abs(nums[right]):
                lst.appendleft(nums[left]**2)
                left+=1
                
            else:
                lst.appendleft(nums[right]**2)
                right-=1
            
        return lst