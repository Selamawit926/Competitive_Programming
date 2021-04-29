class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count=0

        for i in range(len(grid)):
            
            if grid[i][0]<0:
                count+=len(grid[i])
                # print(i,count)
                continue
                
            start=0
            end=len(grid[i])-1
            
            while start<end:
                
                mid=(start+end)//2
                
                if grid[i][mid]>=0 and grid[i][mid+1]<0:
                    count+=len(grid[i])-(mid+1)
                    break
                    
                elif grid[i][mid]<0 and grid[i][mid-1]>=0:
                    count+=len(grid[i])-mid
                    break
                    
                elif grid[i][mid]<0 and grid[i][mid-1]<0:
                    end=mid-1
                    
                else:
                    start=mid+1
                        
                        
        return count