class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        lst=[]
        self.getCol(columnNumber,lst)
        lst.reverse()
        return "".join(lst)
        
    def getCol(self,num,lst):
        if num<=0:return
        num-=1
        lst.append(chr((num%26)+ord("A")))
        self.getCol(num//26,lst)
        return