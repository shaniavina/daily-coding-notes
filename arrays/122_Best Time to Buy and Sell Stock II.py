class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalProfit = 0
        currentProfit = 0
        if len(prices) == 1:
            return 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                currentProfit += prices[i] - prices[i - 1]
                
            else:
                totalProfit += currentProfit
                currentProfit = 0
        return totalProfit + currentProfit