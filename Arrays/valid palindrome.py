# https://leetcode.com/problems/valid-palindrome/


# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        for c in s:
            if c.isalnum():
                res += c.lower()
        return res == res[::-1]

s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))  # True

s = "race a car"
print(Solution().isPalindrome(s))  # False
