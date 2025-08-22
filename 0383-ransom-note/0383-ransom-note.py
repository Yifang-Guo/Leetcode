class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = Counter(magazine)

        for c in ransomNote:
            if c not in magazine_count:
                return False
            magazine_count[c] -= 1
            if magazine_count[c] < 0:
                return False

        return True
        