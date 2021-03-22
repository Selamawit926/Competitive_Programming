from collections import deque

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
#         with two pointers
        
        left=right=0
        cost=0
        queue=deque()
        maxi=0
        length=0
        
        while left<len(s) and right<len(s):
            
            diff=abs(ord(s[right])-ord(t[right]))
            
            if cost+diff>maxCost:
                if right-left>maxi:
                    maxi=right-left
                    
                if queue:
                    cost-=queue.popleft()
                else:
                    right+=1
                    
                left+=1
                
            else:
                cost+=diff
                queue.append(diff)
                right+=1
                
        # print(maxi)
        # print(right,left)
        if right-left>maxi and cost<=maxCost:
            maxi=right-left
        return maxi
    
    
    
    
        
#         cost=0
#         maxLength=0
#         queue=[]
        
#         for i in range(len(s)):
            
#             diff= abs(ord(s[i])-ord(t[i]))
#             # print(str(diff) + " " + s[i] + " " + t[i])
#             if cost+diff <= maxCost :
#                 cost+=diff
#                 queue.append(diff)
#                 # print(cost)
# #                 print("first: "+str(queue))
# #                 print("Cost: " + str(cost))
                
#                 if len(queue)> maxLength:
#                     maxLength=len(queue)
#                     # print(maxLength)
#             else:
#                 # print("first: "+str(queue))
#                 # print("Cost: " + str(cost))
                
#                 if len(queue)> maxLength:
#                     maxLength=len(queue)
#                     # print(maxLength)

#                 if len(queue)!=0:
#                     cost-=queue.pop(0)
                    
#                 i-=1
                    

#         # print(maxLength)
#         return maxLength
    