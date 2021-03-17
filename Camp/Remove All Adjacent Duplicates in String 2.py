class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack=[s[0]]
        count=1
        dic={s[0]:1}
        dic2={}
        
        for i in range(1,len(s)):
            if stack:
                if s[i]==stack[len(stack)-1]:
                    if s[i] in dic2 and dic[s[i]]==k: 
                        dic[s[i]]=dic2[s[i]]
                        del dic2[s[i]]
                        
                    dic[s[i]]+=1

                else:
                    if s[i] in dic:
                        dic2[s[i]]=dic[s[i]]
                        
                    dic[s[i]]=1
          
                
                if dic[s[i]]==k:
                    for i in range(k-1):
                        stack.pop()
                        


                else: 
                    stack.append(s[i])
                    
            else:
                stack.append(s[i])
                dic[s[i]]=1

            # print(dic2)
            
        final=""
        for i in stack:
            final+=i
            
        return final
            