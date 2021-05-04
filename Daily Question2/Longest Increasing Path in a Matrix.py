class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        memo={}
        maxi=1
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (i,j) not in memo:
                    leng=self.dfs(matrix,i,j,memo,directions,1)
                    if leng>maxi:
                        maxi=leng
                else:
                    if memo[(i,j)] > maxi:
                        maxi=memo[(i,j)]
                        
        return maxi
                        
                        
    def dfs(self,matrix,i,j,memo,directions,maxi1):
        
        if (i,j) in memo:
            return memo[(i,j)]
        
        
        for direction in directions:
            if 0<=direction[0]+i<len(matrix) and 0<=direction[1]+j<len(matrix[i]):
                newrow=direction[0]+i
                newcol=direction[1]+j
                if matrix[newrow][newcol]>matrix[i][j]:
                    length=self.dfs(matrix,newrow,newcol,memo,directions,1)+1
                    if length>maxi1:
                        maxi1=length
                        
        # print(maxi1)    
        memo[(i,j)]=maxi1
        return memo[(i,j)]