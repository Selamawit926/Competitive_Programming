class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        tLst=[i for i in target]
        save=defaultdict(list)
        count=0
        for i in range(len(nums)):
            # numLst=[nums[i][j] for j in range(len(nums[i]))]
            for j in range(len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                    count+=1
                    
        return count