
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = float('inf')
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
                # print("new min price is", minPrice)
            elif prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice
                # print ("profit is ", maxProfit)
        
        return maxProfit