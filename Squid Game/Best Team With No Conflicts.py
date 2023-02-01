class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        tot=sum(scores)
        dp=[[-1 for x in range(len(scores))] for y in range(len(scores)+1)]
        lst=[]
        for i in range(len(scores)):
            lst.append((ages[i],scores[i]))
        lst.sort()
        return self.helper(lst,0,0,dp,-1)
        
    def helper(self,lst,i,maxScore,dp,prev):
        if i>=len(lst):
            return 0
        if dp[prev+1][i]!=-1:
            return dp[prev+1][i]
        included=0
        if lst[i][1]>=maxScore:
            included=lst[i][1]+self.helper(lst,i+1,max(maxScore,lst[i][1]),dp,i)
        excluded=self.helper(lst,i+1,maxScore,dp,prev)
        dp[prev+1][i]=max(included,excluded)
        return dp[prev+1][i]