# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Sliding Window
# Time: O(n)
# Space: O(1)

def lengthOfLongestSubstring(s):
    n = len(s)
    L = 0
    longest = 0
    charset = set()

    for R in range(n):
        while s[R] in charset:
            charset.remove(s[L])
            L += 1
        charset.add(s[R])
        longest = max(longest, R - L + 1)
    return longest

s = "abcabcbb"
print(lengthOfLongestSubstring(s))
s = "bbbbb"
print(lengthOfLongestSubstring(s))
s = "pwwkew"
print(lengthOfLongestSubstring(s))

