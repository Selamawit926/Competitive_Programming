class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        if len(seats)==2:
            return 1
        
        di={}
        left=-1
        right=-1
        maxi=0
        
        for i in range(len(seats)):
            if seats[i]==1:
                left=i
                
            else:
                if left!=-1:
                    di[i]=i-left
                
        # print(di)
                
        
        
        for i in range(len(seats)-1,-1,-1):
            if seats[i]==1:
                right=i
                # print(right)
                
            else:
                if right!=-1:
                    if i in di:
    
                        di[i]=min(di[i],right-i)
                        
                    else:
                        di[i]=right-i
                # print(i)
                
        # print(di)
        # print(di.values())
        # print(max(di.values()))
            
        
        return max(di.values())
        