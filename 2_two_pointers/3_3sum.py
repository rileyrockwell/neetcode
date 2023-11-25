from typing import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # neetcode
        res = []
        nums.sort()

        for i, a in enumerate(nums):
        	if i > 0 and a == nums[i - 1]:
        		



nums = [-1, 0, 1, 2, -1, -4]
