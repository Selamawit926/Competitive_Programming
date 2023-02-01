class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        # lst=[]
        # days=0
        # for i in range(len(plantTime)):
        #     lst.append((growTime[i],plantTime[i]))
        # lst.sort()
        # for i in range(len(lst)):
        #     days=max(days,lst[i][0])+lst[i][1]
        # return days
        lst=[]
        days=0
        for i in range(len(plantTime)):
            lst.append((growTime[i],plantTime[i]))
        lst.sort()
        lst.reverse()
        days=planting=0
        for i in range(len(lst)):
            planting+=lst[i][1]
            days=max(days,lst[i][0]+planting)
        return days