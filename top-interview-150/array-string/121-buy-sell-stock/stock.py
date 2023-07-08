from typing import List


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
        # # Sliding window: better to buy cheap (earlier in the list) and sell higher (later in the list)
        # lowest_buy_idx = 0
        #
        # if len(prices) < 2:
        #     # need at least 2 days: one to buy and one to sell
        #     return 0
        #
        # # default to 2nd day because you cannot sell on the first day (have to buy first)
        # highest_sell_idx = 1
        # # find highest price to sell at
        # for idx,val in enumerate(prices[2:]):
        #     print(f"Index={idx}, val={val}")
        #     if val > prices[highest_sell_idx]:
        #         # +2 because we are starting from index 2
        #         highest_sell_idx = idx + 2
        #
        # # find cheapest day to buy before the sell date
        # for idx, val in enumerate(prices[:highest_sell_idx]):
        #     if val < prices[lowest_buy_idx]:
        #         lowest_buy_idx = idx
        #
        #
        # max_profit = prices[highest_sell_idx] - prices[lowest_buy_idx]
        #
        # print(f"Lowest buy index: {lowest_buy_idx}")
        # print(f"Highest sell index: {highest_sell_idx}")
        # print(f"Max profit: {max_profit}")
        #
        # if max_profit < 0:
        #     return 0  # no profit
        #
        # return max_profit

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if len(prices) < 2:
#             # need at least 2 days: one to buy and one to sell
#             return 0
#
#         max_profit = 0
#
#         # default values lower and greater than constraints so they will get overwritten:
#
#         lowest_buy_day = 0
#         highest_sell_day = len(prices) - 1
#         shift = 1
#         for today, val in enumerate(prices[shift:]):
#             today += shift  # not starting at index 0
#             print(
#                 f"Today: {today}. Val: {val}. Lowest_buy_day: {lowest_buy_day}. Highest_sell_day={highest_sell_day}")
#             print(
#                 f"Price at lowest_buy_day: {prices[lowest_buy_day]} and highest_sell_day={prices[highest_sell_day]}")
#             # can only buy before selling
#             if today < highest_sell_day and val < prices[lowest_buy_day]:
#                 lowest_buy_day = today
#             # can only sell after buying
#             if today > lowest_buy_day and val > prices[highest_sell_day]:
#                 highest_sell_day = today
#
#             max_profit = max(max_profit, prices[highest_sell_day] - prices[lowest_buy_day])
#
#         print()
#         print(f"lowest_buy_day: {lowest_buy_day}")
#         print(f"highest_sell_day: {highest_sell_day}")
#         print(f"Max profit: {max_profit}")
#
#         return max_profit
#
