class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        tot=0
        count=0
        
        di={0:1}
        
        for i in range(len(nums)):
            
            tot+=nums[i]
            
            diff=tot-k
            
            if diff in di:
                count+=di[diff]
                
            if tot in di:
                di[tot]+=1
                
            else:
                di[tot]=1
                
        # print(count)
        return count