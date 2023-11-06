from typing import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums[0]

        frequency_dict = {nums.count(num): num for num in nums}

        result = []
        temp_list = list(frequency_dict.values())

        for max_value in range(k):
            max1 = max(temp_list)    
            result.append(max1)
            temp_list.remove(max1)
        
        return result



nums, k = [1,1,1,2,2,3], 2
print(Solution().topKFrequent(nums, k))

nums, k = [1], 1
print(Solution().topKFrequent(nums, k))

nums, k = [1,1,2,3], 2
print(Solution().topKFrequent(nums, k))

nums, k = [1,1,1,2,2,3], 1
print(Solution().topKFrequent(nums, k))