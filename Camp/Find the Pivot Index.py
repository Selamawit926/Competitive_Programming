class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        
        tot=0
        toRight=[0]
        toLeft=[0]
        
        
        for i in range(len(nums)-1):
            
            tot+=nums[i]
            
            toRight.append(tot)
            
        tot=0
        # print(toRight)
        
        for i in range(len(nums)-1,0,-1):
            
            tot+=nums[i]
            
            toLeft.append(tot)
            
        toLeft.reverse()
        # print(toLeft)
                
            
        for i in range(len(toRight)):
            if toRight[i]==toLeft[i]:
                return i
            
         
        return -1