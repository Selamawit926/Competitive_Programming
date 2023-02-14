class Solution:
    def sumZero(self, n: int) -> List[int]:
        mid=n//2
        lst=[]
        for i in range(1,mid+1):
            lst.append(i)
            lst.append(-i)
        if n%2!=0:
            lst.append(0)
        return lst