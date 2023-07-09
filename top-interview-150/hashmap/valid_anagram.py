# Problem: https://leetcode.com/problems/valid-anagram/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # find out how many times each letter in s occurs
        s_letters = dict()
        for c in s:
            if c in s_letters:
                s_letters[c] = s_letters[c] + 1
            else:
                s_letters[c] = 1
        print("S:", s_letters)

        # find out how many times each letter in t occurs
        t_letters = dict()
        for c in t:
            if c in t_letters:
                t_letters[c] = t_letters[c] + 1
            else:
                t_letters[c] = 1
        print("T", t_letters)

        # check if every letter in s is in t and occurs the same number of times
        for k, v in s_letters.items():
            if k not in t_letters:
                print(f"'{k}' not in t")
                return False

            if v != t_letters[k]:
                print(f"'{k}' appears {v} in s but {t_letters[k]} in t")
                return False

        return True
