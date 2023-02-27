class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        lst=[]
        maxi=mYear=0
        logs.sort()
        for i in range(len(logs)):
            lst.append([0,logs[i][0]])
            for j in range(len(logs)):
                if logs[j][0]<=logs[i][0]<logs[j][1]:
                    lst[-1][0]+=1
        for year in lst:
            if year[0]>maxi:
                maxi=year[0]
                mYear=year[1]
        return mYear