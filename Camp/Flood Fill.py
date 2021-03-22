class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        start=[sr,sc]
        value=image[sr][sc]
        visited=[]
        
        image[sr][sc]=newColor
        visited.append(start)
        self.dfs(image,directions,start,visited,newColor,value)
        
        # print(image)
        return image
        
    def dfs(self,image,directions,start,visited,newColor,value):
        
        for i in range(len(directions)):
            
            newStart=[]
            newStart.append(start[0]+directions[i][0])
            newStart.append(start[1]+directions[i][1])
            # print(newStart)
            if 0 <= newStart[0]<len(image) and 0 <= newStart[1]<len(image[newStart[0]]) and newStart not in visited:
    
                visited.append(newStart)
                if image[newStart[0]][newStart[1]]==value:
                    image[newStart[0]][newStart[1]]=newColor
                    self.dfs(image,directions,newStart,visited,newColor,value)

           
                
        return 