from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            # need at least 2 days: one to buy and one to sell
            return 0

        best_buy_index = 0
        max_profit = 0
        shift = 1
        for index, val in enumerate(prices[shift:]):
            shifted_index = index + shift
            if val < prices[best_buy_index]:
                best_buy_index = shifted_index

            current_profit = prices[shifted_index] - prices[best_buy_index]
            if shifted_index > best_buy_index and current_profit > max_profit:
                max_profit = current_profit

        return max_profit
