from typing import List


class Solution:
    idx = 0

    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            elem = nums[0]
            return self.idx if elem == target else -1

        mid = len(nums) // 2
        if target < nums[mid]:
            return self.search(nums[:mid], target)
        else:
            self.idx += mid
            return self.search(nums[mid:], target)
