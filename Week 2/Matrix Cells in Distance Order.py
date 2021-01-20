class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        lst2=[]
        lst3=[]
        for i in range(0,R):
            for j in range(0,C):
                d=abs(r0-i)+abs(c0-j)
                # lst3.append(d)
                lst2.append([d,[i,j]])
              

        lst2.sort()
        for i in lst2:
            lst3.append(i[1])

                
        return lst3

