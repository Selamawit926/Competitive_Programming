class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        cost=0
        maxLength=0
        queue=[]
        
        for i in range(len(s)):
            
            diff= abs(ord(s[i])-ord(t[i]))
            # print(str(diff) + " " + s[i] + " " + t[i])
            if cost+diff <= maxCost :
                cost+=diff
                queue.append(diff)
                # print(cost)
                print("first: "+str(queue))
                print("Cost: " + str(cost))
                
                if len(queue)> maxLength:
                    maxLength=len(queue)
                    # print(maxLength)
            else:
                print("first: "+str(queue))
                print("Cost: " + str(cost))
                
                if len(queue)> maxLength:
                    maxLength=len(queue)
                    # print(maxLength)

                if len(queue)!=0:
                    cost-=queue.pop(0)
                    
                i-=1
                    

        # print(maxLength)
        return maxLength