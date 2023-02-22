class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        lst=[int(i) for i in s]
        curr=[int(i) for i in s]
        lst.sort()
        lst.reverse()
        seconds=0
        while curr!=lst:
            seconds+=1
            i=0
            while i<len(curr)-1:
                if curr[i]==0 and curr[i+1]==1:
                    curr[i]=1
                    curr[i+1]=0
                    i+=2
                else:
                    i+=1
        return seconds