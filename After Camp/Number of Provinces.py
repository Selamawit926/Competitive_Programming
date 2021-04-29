class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        visited=set((0,0))
        count=0
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j]==1 and (i,j) not in visited :
                    # print((i,j))
                    visited.add((i,j))
                    self.dfs(isConnected,j,visited)
                    count+=1
                    
        return count
        
        
    def dfs(self,isConnected,i,visited):
        
        for j in range(len(isConnected[i])):
            if isConnected[i][j]==1 and (i,j) not in visited:
                visited.add((i,j))
                self.dfs(isConnected,j,visited)
                
        
        
        return