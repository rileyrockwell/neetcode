class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp_set = set(nums)

        return len(nums) != len(temp_set)