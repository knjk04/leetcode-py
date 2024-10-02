# https://leetcode.com/problems/group-anagrams/description/
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) # sorted str : List[str]
        # if sorted string not in dict, then it's a new anagram
        for s in strs:
            sorted_str = "".join(sorted(s))
            if sorted_str not in groups:
                groups[sorted_str] = [s] # new group
            else:
                groups[sorted_str].append(s)

        return groups.values()
