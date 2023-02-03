class Solution:

    def __init__(self, w: List[int]):
        self.prefix=[]
        self.tot=0
        for i in w:
            self.tot+=i
            self.prefix.append(self.tot)

    def pickIndex(self) -> int:
        rand=random.randint(1,self.tot)
        start=0
        end=len(self.prefix)-1
        while start<end:
            mid=(start+end)//2
            if self.prefix[mid]>=rand:
                end=mid
            else:
                start=mid+1
        return start