class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo={}
        first=self.dfs(0,memo,cost)
        print(first)
        second=self.dfs(1,memo,cost)
        print(second)
        
        return min(first,second)
        
        
    def dfs(self,i,memo,cost):
        
        if i>=len(cost):
            return 0
    
        if i in memo:
            return memo[i]
        
        
        first=cost[i]+self.dfs(i+1,memo,cost)
        second=cost[i]+self.dfs(i+2,memo,cost)
        
        memo[i]=min(first,second)
        
        return memo[i]