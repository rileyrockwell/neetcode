from typing import *

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

s = "anagram"
t = "nagaram"

s = "the"
t = "car"

print(Solution().isAnagram(s, t))