from typing import List


# https://leetcode.com/problems/richest-customer-wealth/
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            current_wealth = 0
            for money in customer:
                current_wealth += money
            max_wealth = max(max_wealth, current_wealth)

        return max_wealth
