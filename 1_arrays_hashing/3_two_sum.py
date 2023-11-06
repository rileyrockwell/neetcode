from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # data strcuture
        dic = {}

        for index, integer in enumerate(nums):
            complement = target - integer

            if complement in dic:
                return [dic[complement], index]

            dic[integer] = index

        return []



nums = [3, 2, 4]
target = 6
print(Solution().twoSum(nums, target))