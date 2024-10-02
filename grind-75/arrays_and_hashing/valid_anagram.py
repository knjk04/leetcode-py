# https://leetcode.com/problems/valid-anagram/description/
from collections import defaultdict
from typing import Dict


class Solution:
    def count_occurrences(self, s: str) -> Dict[str, int]:
        occurrences = defaultdict(int)
        for letter in s:
            occurrences[letter] += 1
        return occurrences

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return self.count_occurrences(s) == self.count_occurrences(t)
