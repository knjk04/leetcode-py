# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed_to_reach_target = dict()
        for idx,val in enumerate(nums):
            off_by = target - val
            if val in needed_to_reach_target:
                return [needed_to_reach_target[val], idx]
            needed_to_reach_target[off_by] = idx

