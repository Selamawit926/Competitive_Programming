class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        mins=0
        queue=deque()
        
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==2:
                    queue.append((i,j,1))
                    
                
        # print(queue)
                    
        while queue:
            current= queue.popleft()
            count=0
            
            for direction in directions:
                new=(current[0]+direction[0],current[1]+direction[1],current[2]+1)
                if 0<=new[0]<len(grid) and 0<=new[1]<len(grid[0]):
                    if grid[new[0]][new[1]]==1:
                        # print("from ",current , "to ", new)
                        count+=1
                        queue.append(new)
                        grid[new[0]][new[1]]=2
                    
            if count>0:
                mins=current[2]
                
                
            
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    return -1
                
                
        return mins