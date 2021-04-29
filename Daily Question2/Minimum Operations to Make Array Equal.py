class Solution:
    def minOperations(self, n: int) -> int:
        
        if n==1:
            return 0
        
        count=0       
        mid=n//2
        for i in range(mid):
            count+=(2*i)+1
        
        if n%2!=0:
            count+=mid
        
        return count