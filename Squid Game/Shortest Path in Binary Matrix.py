class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions=[[1,0],[0,1],[1,1],[-1,-1],[1,-1],[-1,1],[0,-1],[-1,0]]
        mini=float("inf")
        if grid[0][0]==0:
            visited={(0,0)}
            queue=deque([(0,0,1)])
            while queue:
                curr=queue.popleft()
                if curr[0]==len(grid)-1 and curr[1]==len(grid)-1:
                    return curr[2]
                for direction in directions:
                    newR=direction[0]+curr[0]
                    newC=direction[1]+curr[1]
                    if 0<=newR<len(grid) and 0<=newC<len(grid) and (newR,newC) not in visited:
                        if grid[newR][newC]==0:
                            visited.add((newR,newC))
                            queue.append((newR,newC,curr[2]+1))
                
        return -1