class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    #my way 
        for i,numi  in enumerate(nums):
            seek = target - numi
            array = nums
            array[i] = None # prevents looking at current
            if seek in array:
                return [i,nums.index(seek)]
            
#proper way

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i