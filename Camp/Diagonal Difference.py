def diagonalDifference(arr):
    # Write your code here
    
    if len(arr)==0 or len(arr)==1:
        return 0
    
    start1=arr[0][0]
    start2=arr[0][len(arr)-1]
    directions=[[1,1],[1,-1]]
   
    tot1=addDiagonals(start1,directions[0],arr,[0,0])
    tot2=addDiagonals(start2,directions[1],arr,[0,len(arr)-1])
        
    # print(tot1)
    # print(tot2)
    
    return abs(tot1-tot2)
        
def addDiagonals(tot,direction,arr,point):
    
    
    pos=[point[0]+direction[0],point[1]+direction[1]]
    
    if pos[0] >= len(arr):
        return tot
    
    tot = tot+ arr[pos[0]][pos[1]]
   
    diag=addDiagonals(tot,direction,arr,pos) 
    
    return diag
    