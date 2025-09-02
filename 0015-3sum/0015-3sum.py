class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            
            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                twoSum = nums[l] + nums[r]
                if twoSum == target:
                    res.append([nums[i], nums[l], nums[r]])

                    while l < r and nums[l+1] == nums[l]:
                        l += 1
                    while l < r and nums[r-1] == nums[r]:
                        r -= 1

                    l += 1
                    r -= 1

                elif twoSum < target:
                    l += 1
                else:
                    r -= 1

        return res
        