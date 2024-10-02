# https://leetcode.com/problems/valid-palindrome/description/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        front_idx = 0
        back_idx = len(s) - 1

        while front_idx < back_idx:
            front_val = s[front_idx].lower()
            back_val = s[back_idx].lower()

            if not front_val.isalnum():
                front_idx += 1  # skipping non letter/number at the front
                continue
            if not back_val.isalnum():
                back_idx -= 1  # skipping non letter/number at the back
                continue
            elif front_val != back_val:
                return False

            front_idx += 1
            back_idx -= 1

        return True
