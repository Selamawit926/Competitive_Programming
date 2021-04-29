class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        memo = {}
        hi = self.dfs(grid,0,0,memo)
        # print(memo)
        return hi
    def dfs(self,grid,i,j,memo):
        
        if i==len(grid)-1 and j==len(grid[i])-1:
            memo[(i,j)]=grid[i][j]
            return grid[i][j]
        
        if i>=len(grid) or j>=len(grid[i]):
            return 10**5
        
        
        if (i,j) in memo:
            return memo[(i,j)]
        
        right=grid[i][j]+self.dfs(grid,i,j+1,memo)
        down=grid[i][j]+self.dfs(grid,i+1,j,memo)
        
        
        
        memo[(i,j)]=min(down,right)
        # print(memo)
        # print(right,down,memo[(i,j)])
        return memo[(i,j)]