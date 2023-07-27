class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_letters = dict()
        for letter in magazine:
            if letter in magazine_letters:
                magazine_letters[letter] = magazine_letters.get(letter) + 1
            else:
                magazine_letters[letter] = 1

        ransom_letters = dict()
        for letter in ransomNote:
            if letter not in magazine_letters:
                return False

            if letter in ransom_letters:
                ransom_letters[letter] = ransom_letters.get(letter) + 1

                if ransom_letters.get(letter) > magazine_letters.get(letter):
                    return False
            else:
                ransom_letters[letter] = 1

        print("ransom letters", ransom_letters)
        print("magazine letters", magazine_letters)
        return True
