# https://leetcode.com/problems/contains-duplicate/
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        elems = set()
        for n in nums:
            if n in elems:
                return True
            elems.add(n)
        return False
