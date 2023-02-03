class Solution:
    def validPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        while left<=right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                fromLeft=self.isPalindrome(s,left+1,right)
                fromRight=self.isPalindrome(s,left,right-1)
                return fromLeft or fromRight
        return True
    def isPalindrome(self,s,left,right):
        while left<=right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                return False
        return True