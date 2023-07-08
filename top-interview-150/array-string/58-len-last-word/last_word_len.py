# Problem: https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_len = 0
        for idx, c in enumerate(s[-1::-1]):
            if c.isspace():
                if word_len > 0:
                    return word_len
            else:
                word_len += 1

        return word_len
