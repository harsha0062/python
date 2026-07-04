from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Return True if s is a palindrome after:
        - removing non-alphanumeric characters
        - converting letters to lowercase
        """
        res = ""

        for i in s:
            if i.isalnum():
                res += i.lower()

        rev = res[::-1]
        return res == rev


# Test cases inside the code
sol = Solution()

s1 = "A man, a plan, a canal: Panama"
print(sol.isPalindrome(s1))  # True

s2 = "race a car"
print(sol.isPalindrome(s2))  # False

s3 = " "
print(sol.isPalindrome(s3))  # True

s4 = "0P"
print(sol.isPalindrome(s4))  # False