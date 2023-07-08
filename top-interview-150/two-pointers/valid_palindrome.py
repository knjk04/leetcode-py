# Problem: https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = ""
        for c in s:
            if c.isalnum():
                forward += c.lower()
        print(forward)

        start_idx = 0
        end_idx = len(forward) - 1

        while start_idx < len(forward) and end_idx > 0:
            if forward[start_idx] != forward[end_idx]:
                print(f"start index: {start_idx}. Val: {forward[start_idx]}")
                print(f"end index: {end_idx}. Val: {forward[end_idx]}")
                return False
            start_idx += 1
            end_idx -= 1

        # default of True also handles the empty string case
        return True
