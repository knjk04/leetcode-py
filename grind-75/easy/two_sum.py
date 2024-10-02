from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for idx,val in enumerate(nums):
            diff = target - val
            if diff in seen:
                return [idx, seen[diff]]
            seen[val] = idx
            
