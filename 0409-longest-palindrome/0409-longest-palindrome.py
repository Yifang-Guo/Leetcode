class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_s = Counter(s)
        res = 0

        for c, count in count_s.items():
            if count % 2 == 0:
                res += count
            else:
                if count - 1 != 0:
                    res += count - 1
                    count_s[c] = 1

        for count in count_s.values():
            if count == 1:
                res += 1
                break

        return res
        