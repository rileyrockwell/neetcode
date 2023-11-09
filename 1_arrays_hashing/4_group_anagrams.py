from collections import defaultdict
from typing import *


# Arrays & Hashing
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        temp_list = []

        for string in strs:
            character_list = tuple(map(str, string))

        for i in strs:
            temp_list = tuple(sorted(i))
            print(temp_list)

            # b/c the default dictionary already has int value 0 assigned to every key
            if result[temp_list] == 0:
                result[temp_list] += 1


        return result




strs = [["eat","tea","tan","ate","nat","bat"], [""], ["a"]]
for i in strs:
    print(Solution().groupAnagrams(i))