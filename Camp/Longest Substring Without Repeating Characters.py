class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        repeated=set()
        left=right=0
        length=0
        maxi=0
        i=0
        
        while left<len(s) and right<len(s):
            
            if s[right] in repeated:
                
                repeated.remove(s[left])
                length=right-left
                if length>maxi:
                    maxi=length
                    print(maxi)
                left+=1
                
                
            else:
                repeated.add(s[right])
                right+=1
                
                    
        if right-left> maxi:
            maxi=right-left
            
        return maxi