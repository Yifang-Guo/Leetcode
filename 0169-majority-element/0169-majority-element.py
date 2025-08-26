class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        val = nums[0]
        count = 0

        for n in nums:
            if n == val:
                count += 1
            else:
                count -= 1
                if count < 0:
                    val = n
                    count = 1

        return val
        