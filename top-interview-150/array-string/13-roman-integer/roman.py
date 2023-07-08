# Problem: https://leetcode.com/problems/roman-to-integer/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        last_seen: str = s[0]
        num = symbols[last_seen]
        for letter in s[1:]:
            val = symbols[letter]
            if last_seen == "I" and letter in "VX":
                # -2 because we have already added 1
                num += val - 2
            elif last_seen == "X" and letter in "LC":
                # -20 because we have already added 10
                num += val - 20
            elif last_seen == "C" and letter in "DM":
                # -200 because we have already added 100
                num += val - 200
            else:
                num += val
            last_seen = letter

        return num
