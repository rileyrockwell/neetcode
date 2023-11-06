class Solution:
    def isValid(self, s: str) -> bool:
        return 1



s = ["()", "()[]{}", "(]"]
for i in s:
    print(Solution().isValid(i))