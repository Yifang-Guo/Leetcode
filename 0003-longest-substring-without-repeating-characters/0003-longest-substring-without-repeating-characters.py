class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = r = 0
        visited = set()

        for r in range(len(s)):
            if s[r] not in visited:
                visited.add(s[r])
                res = max(res, r - l + 1)
            else:
                while s[l] != s[r]:
                    visited.remove(s[l])
                    l += 1
                l += 1

        return res
        