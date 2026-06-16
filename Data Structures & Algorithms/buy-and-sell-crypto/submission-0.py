class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pro = 0
        min_buy = prices[0]

        for sell in prices:
            max_pro = max(max_pro, sell - min_buy)
            min_buy = min(min_buy, sell)
        return max_pro