class Solution:
    def maximumSwap(self, num: int) -> int:
        number=str(num)
        lst=[(number[i],i) for i in range(len(number))]
        lst.sort()
        numL=[i for i in number]
        p1=len(lst)-1
        p2=0
        while p1>=0 and p2<len(numL):
            if lst[p1][0]!=numL[p2]:
                numL[p2],numL[lst[p1][1]]=numL[lst[p1][1]],numL[p2]
                break
            else:
                if lst[p1][1]==p2:
                    while p1>=0 and lst[p1][0]==numL[p2]:
                        p1-=1
                p2+=1
        return int("".join(numL))