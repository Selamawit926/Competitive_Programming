class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        
        self.rectangle=rectangle
    
    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        visited=set()
        self.dfs(row1,col1,row2,col2,self.rectangle,newValue,visited)

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]

    def dfs(self,i,j,rowend,colend,rectangle,new,visited):
        
        if i>=len(rectangle) or j>=len(rectangle[i]):
            return
        
        if i>rowend or j>colend:
            return
        
        if (i,j) not in visited:
            rectangle[i][j]=new
            visited.add((i,j))
            self.dfs(i,j+1,rowend,colend,rectangle,new,visited)
            self.dfs(i+1,j,rowend,colend,rectangle,new,visited)
            
        return