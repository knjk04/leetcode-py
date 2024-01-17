from typing import List


class Solution:
    def _search(self, nums: List[int], target: int, start_index: int) -> int:
        if len(nums) == 1 and target != nums[0]:  # base case
            return -1

        mid = len(nums) // 2
        if target < nums[mid]:  # search left
            return self._search(nums[:mid], target, start_index)
        elif target == nums[mid]:
            return start_index + mid
        else:  # search right
            return self._search(nums[mid:], target, start_index + mid)

    def search(self, nums: List[int], target: int) -> int:
        return self._search(nums, target, 0)
