class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        currentProfit = 0

        if len(prices) == 1:
            return 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                currentProfit += prices[i] - prices[i - 1]
                maxProfit = max(maxProfit, currentProfit)
            elif prices[i] < prices[i - 1]:
                currentProfit = max(0, currentProfit + prices[i] - prices[i - 1])
                
        return maxProfit
