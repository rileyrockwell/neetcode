from typing import *

class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		# build the frequency dictionary
		a = {key: nums.count(key) for key in nums}
		
		return a

		return a, "nums[i]: frequency"

nums = [1,1,1,2,2,2,3]
k = 2

print(Solution().topKFrequent(nums, k))