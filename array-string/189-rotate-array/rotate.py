from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # use mod to wrap over list in case k > len(nums)
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
