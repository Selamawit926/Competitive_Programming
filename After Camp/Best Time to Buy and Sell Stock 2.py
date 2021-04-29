class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left=0
        right=1
        profit=0
        value=prices[left]
        
        while left<len(prices) and right<len(prices):
            # print(left,right)
            
            if right==len(prices)-1:
                if prices[right]>value:
                    profit+=prices[right]-prices[left]
                    
                else:
                    profit+=value-prices[left]
                    
                right+=1
                
            else:
                if prices[left]>prices[right] and right-left==1:
                    left+=1
                    value=prices[left]

                else:
                    if prices[right]>value:
                        value=prices[right]


                    else:
                        profit+=value-prices[left]
                        # print(profit)
                        left=right
                        value=prices[left]
                    
                right+=1
                
        
        
        # print(profit)
        return profit