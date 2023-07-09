from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            # need at least 2 days: one to buy and one to sell
            return 0

        best_buy_index = 0
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[best_buy_index]:
                best_buy_index = i

            if i > best_buy_index:
                max_profit = max(max_profit, prices[i] - prices[best_buy_index])

        return max_profit
