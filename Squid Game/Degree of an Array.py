class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count=Counter(nums)
        index=defaultdict(list)
        for i in range(len(nums)):
            index[nums[i]].append(i)
        lst=[]
        for i in count:
            lst.append((count[i],i))
        lst.sort()
        length=float("inf")
        maxi=lst[-1][0]
        for i in range(len(lst)-1,-1,-1):
            if lst[i][0]==maxi:
                length=min(length,index[lst[i][1]][-1]-index[lst[i][1]][0]+1)
        return length