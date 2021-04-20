class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        
        # jumps=0
        queue=deque()
        queue.append((2,0,0))
        memo={}
        nums={1,2,3}
        
        while queue:
            
            popped=queue.popleft()
            # print(popped[2])
            for i in range(popped[1],len(obstacles)-1):
                
                if obstacles[i+1]==popped[0]:
                
                    if obstacles[i]==0:
                        for j in nums:
                            if j!=popped[0] and (j,i+1) not in memo:
                                queue.append((j,i+1,popped[2]+1))
                                memo[(j,i+1)]=popped[2]+1
                                
                        break
                                
                                
                    else:
                        for j in nums:
                            if j!=popped[0] and j!=obstacles[i] and (j,i+1) not in memo:
                                queue.append((j,i+1,popped[2]+1))
                                memo[(j,i+1)]=popped[2]+1
                                
                        break
                        
                        
                # print(popped[0],i+1)
                if (popped[0],i+1) in memo:
                    memo[(popped[0],i+1)]=min(memo[(popped[0],i+1)],popped[2])
                else:
                    memo[(popped[0],i+1)]=popped[2]
                    
        jumps=len(obstacles)
        # print(memo)
        if memo:
            for i in memo:
                if i[1]==len(obstacles)-2 and memo[i]<jumps:
                    jumps=memo[i]
                
                
            return jumps
                        
            
        return 0