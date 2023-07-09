# Problem: https://leetcode.com/problems/valid-anagram/?envType=study-plan-v2&envId=top-interview-150
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_counter = Counter(s)
        t_counter = Counter(t)

        # # check if every letter in s is in t and occurs the same number of times
        for k, v in s_counter.items():
            if k not in t_counter:
                # letter in s but not in t
                return False

            if v != t_counter[k]:
                # a letter in s occurs a different number of times to the same letter in t
                return False

        return True
