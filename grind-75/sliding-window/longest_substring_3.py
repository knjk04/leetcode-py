# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1179058206/
# Not working
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        left, right, max_substr_len = 0, 1, 1
        seen = {s[left]}
        found_dup = False
        while left < len(s):
            if right == len(s) and ((left + right + 1) >= len(s)):
                break

            if s[right] in seen:
                found_dup = True
            else:
                seen.add(s[right])

            if found_dup or right + 1 == len(s):
                max_substr_len = max(len(seen), max_substr_len)
                seen = {s[
                            left]}  # reset. Only want to add this once per pass of string
                left += 1
                right = left + 1
                found_dup = False  # reset
            else:
                right += 1

        return max(len(seen), max_substr_len)
