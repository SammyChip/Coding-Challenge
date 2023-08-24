class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        testNums = []

        for n in nums:
            if n in testNums:
                return True
            testNums.append(n)
        return False
