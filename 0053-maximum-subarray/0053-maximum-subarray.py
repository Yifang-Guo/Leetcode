class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxCur = 0
        res = float("-inf")

        for n in nums:
            maxCur = max(maxCur+n, n)
            res = max(res, maxCur)

        return res
        