class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if s==t:
            return True
        
        elif len(s)>len(t):
            return False
      
        left=left1=0
        pos=[]
        newT=set(t)
        
        while left<len(s) and left1<len(t):
            
            if s[left] not in newT:
                return False
            
            if s[left]!=t[left1]:
                left1+=1
                
            else:
                pos.append(left1)
                if len(pos)>1:
                    if pos[-1]<pos[len(pos)-2]:
                        return False
            
            
                left+=1
                left1+=1
                
       
        if left<len(s):
            return False
        
        return True