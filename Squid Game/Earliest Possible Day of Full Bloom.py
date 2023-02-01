class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        lst=[]
        days=0
        for i in range(len(plantTime)):
            lst.append((growTime[i],plantTime[i]))
        lst.sort()
        for i in range(len(lst)):
            days=max(days,lst[i][0])+lst[i][1]
        return days