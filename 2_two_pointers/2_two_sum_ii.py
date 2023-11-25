from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    	# 1-index array: start left pointer at 1; right pointer at range(len), not range(len) - 1
    	left, right = 0, len(nums) - 1

    	while left < right:
    		current_sum = nums[left] + nums[right]

    		if current_sum == target:
    			# solved: return the indices
    			return [left + 1, right + 1]

    		# b/c 'nums' is sorted in increasing order
    		elif current_sum < target:
    			left += 1

    		# b/c 'nums' is sorted in increasing order
    		elif current_sum >= target:
    			right -= 1

    	# if no match found
    	return []


nums = [2, 7, 11, 15]
target = 9

nums = [2, 3, 4]
target = 6

nums = [-1, 0]
target = -1
print(Solution().twoSum(nums, target))