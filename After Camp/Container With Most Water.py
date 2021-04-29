class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        maxarea=0
        
        while left!=right:
            if height[left]>height[right]:
                if (right-left)*height[right]>maxarea:
                    maxarea=(right-left)*height[right]
                right-=1
                
            elif height[right]>height[left]:
                if (right-left)*height[left]>maxarea:
                    maxarea=(right-left)*height[left]
                    
                left+=1
                
            else:
                if (right-left)*height[left]>maxarea:
                    maxarea=(right-left)*height[left]
                    
                right-=1
                
        return maxarea