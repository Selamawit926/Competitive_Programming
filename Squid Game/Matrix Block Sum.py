class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        answer=[]
        rowP=[]
        for i in range(len(mat)):
            rowP.append([mat[i][0]])
            for j in range(1,len(mat[i])):
                rowP[i].append(rowP[i][-1]+mat[i][j])
        for i in range(len(mat)):
            answer.append([])
            minRow=max(0,i-k)
            maxRow=min(len(mat)-1,i+k)
            for j in range(len(mat[i])):
                minCol=max(0,j-k)
                maxCol=min(len(mat[i])-1,j+k)
                answer[-1].append(self.helper(answer,mat,minRow,maxRow,minCol,maxCol,rowP))
        return answer
    def helper(self,answer,mat,minRow,maxRow,minCol,maxCol,rowP):
        tot=0
        currR=minRow
        while currR<=maxRow:
            if minCol-1>=0:
                tot+=rowP[currR][maxCol]-rowP[currR][minCol-1]
            else:
                tot+=rowP[currR][maxCol]
            currR+=1
        return tot