class Solution:
    def tribonacci(self, n: int) -> int:
#         if n<=0:
#             return 0
        
#         if n==1 or n==2:
#             return 1
#         else:
#             return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)
        
        t0=0
        t1=1
        t2=1
        
        if n==0:
            return 0
        
        if n==1 or n==2:
            return 1
        
        
        else:
            i=3
            while i<=n:
                tn=t0+t1+t2
                t0=t1
                t1=t2
                t2=tn
                i+=1
            
        return tn