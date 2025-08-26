class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if sum(arr) % 3 != 0:
            return False

        subSum = sum(arr) // 3

        count = 0

        tempSum = 0

        for n in arr:
            tempSum += n

            if tempSum == subSum:
                tempSum = 0
                count += 1

        return count >= 3
        