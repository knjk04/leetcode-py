from typing import List


# Problem: https://leetcode.com/problems/two-sum/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    # O(N)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dict key: the number needed to reach the target when added to the value ...
        # ... at the index given by the dict val
        needed_to_reach_target = dict()
        for idx,val in enumerate(nums):
            off_by = target - val
            if val in needed_to_reach_target:
                return [needed_to_reach_target[val], idx]
            needed_to_reach_target[off_by] = idx


