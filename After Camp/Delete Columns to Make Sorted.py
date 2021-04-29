class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        di={}
        
        for i in range(len(strs)-1):
            for j in range(len(strs[i])):
        
                if strs[i][j]>strs[i+1][j]:
                    if j not in di:
                        di[j]=1
                        count+=1
                    
                    
                    
        return count