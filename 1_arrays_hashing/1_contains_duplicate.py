from typing import *

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp_set = set(nums)

        return len(nums) != len(temp_set)


nums = [1, 2, 2]
print(Solution().containsDuplicate(nums))