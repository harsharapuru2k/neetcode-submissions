class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left_min=prices[0]
        profit=0
        for i in range(1,len(prices)):
            left_min=min(left_min,prices[i])
            if prices[i]>left_min:
                profit=max(profit,prices[i]-left_min)
        
        return profit

        