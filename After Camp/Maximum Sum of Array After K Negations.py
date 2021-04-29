lass Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        
        A.sort()
        i=0
        
        while K>=1 and i<len(A):
            
            if A[i]<0:
                A[i]=-A[i]
                K-=1
                if A[i]>A[i+1] and i+1<len(A):
                    i+=1
                 
                
            else:
                while K>=1:
                    A[i]=-A[i]
                    K-=1
           
        print(A)
        return sum(A)