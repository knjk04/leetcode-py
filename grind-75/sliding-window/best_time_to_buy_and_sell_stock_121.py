# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy_index = 0
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[best_buy_index]:
                best_buy_index = i

            if i > best_buy_index:
                max_profit = max(max_profit,
                                 prices[i] - prices[best_buy_index])

        return max_profit
