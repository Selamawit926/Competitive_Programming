class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix=[]
        suffix=[]
        output=[]
        product=1
        
        for i in range(len(nums)):
            
            product*=nums[i]
            prefix.append(product)
            
        # print(prefix)
        product=1
        for i in range(len(nums)-1,-1,-1):
            product*=nums[i]
            suffix.append(product)
         
        suffix.reverse()
        # print(suffix)
        
        for i in range(len(nums)):
            if i==0:
                output.append(suffix[i+1])
                
            elif i==len(nums)-1:
                output.append(prefix[i-1])
                
            else:
                output.append(prefix[i-1]*suffix[i+1])
                
        # print(output)
        return output