from collections import defaultdict
from typing import *

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for string in strs:
            character_list = tuple(map(str, string))

            dic[character_list] = string

        return dic

    def groupAnagrams(self, strs):
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for char in s:
                count[ord(char) - ord("a")] += 1

            result[tuple(count)].append(s)

        return result.values()


strs = [["eat","tea","tan","ate","nat","bat"], [""], ["a"]]
for i in strs:
    print(Solution().groupAnagrams(i))