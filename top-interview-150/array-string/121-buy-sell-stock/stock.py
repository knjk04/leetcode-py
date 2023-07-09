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

            current_profit = prices[i] - prices[best_buy_index]
            if i > best_buy_index and current_profit > max_profit:
                max_profit = current_profit

        return max_profit
