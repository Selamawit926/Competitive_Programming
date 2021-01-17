class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        i=0
        
        if len(s)==1:
            return False
        
        while i<len(s):
            if s[i]=="(" or s[i]=="[" or s[i]=="{":
                stack.append(s[i])
            else:
                if len(stack)!=0:
                    if self.check(stack[len(stack)-1],s[i]):
                        stack.pop()
                    else:
                        return False
                else:
                    return False
                
            i+=1 
            
        if len(stack)==1:
            return False
            
        if len(stack)!=0 and (stack[len(stack)-1]=="(" or stack[len(stack)-1]=="[" or stack[len(stack)-1]=="{"):
            return False
        
        return True
    
    def check(self,f,l):
        if l==")" and f=="(":
            return True
        elif l=="]" and f=="[":
            return True
        
        elif l=="}" and f=="{":
            return True
        
        return False
        