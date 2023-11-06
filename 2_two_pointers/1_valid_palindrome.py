import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")

        for char in string.punctuation:
            s = s.replace(char, '')

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

print(Solution().isPalindrome("hannah"))
print(Solution().isPalindrome("A man, a plan, a canal: Panama"))