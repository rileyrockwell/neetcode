class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t))

s = "rat"
t = "car"
print(Solution().isAnagram(s, t))

s = "ab"
t = "a"
print(Solution().isAnagram(s, t))