from typing import Dict


class Solution:
    def is_closing(self, s):
        return s in {")", "}", "]"}

    def close_to_open_pair(self) -> Dict[str, str]:
        return {
            ")": "(",
            "}": "{",
            "]": "["
        }

    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        pairing = self.close_to_open_pair()
        open_stack = []  # LIFO
        for char in s:
            if self.is_closing(char):
                try:
                    actual = open_stack.pop()
                except IndexError:  # empty list
                    return False  # no opening found

                expected = pairing[char]
                print(
                    f"closing: {char}. Expecting: {expected}. Actual: {actual}")
                if expected != actual:
                    return False
            else:
                print(f"Opening: {char}")
                open_stack.append(char)

        return not open_stack  # all are paired

