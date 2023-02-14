class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        num=str(n)
        count=Counter(num)
        for i in range(30):
            value=str(2**i)
            countV=Counter(value)
            if count==countV:
                return True
        return False