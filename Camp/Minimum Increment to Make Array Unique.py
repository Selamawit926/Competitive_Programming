class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        
        A.sort()
        moves=0
        for i in range(1,len(A)):
            if A[i]<=A[i-1]:
                prev=A[i]
                A[i]= A[i-1]+1
                
                moves+=A[i]-prev
        
        
        return moves