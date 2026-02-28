
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/

# Sliding window
# Time Complexity: O(n) where n is the length of the input string. We iterate through the string once.
# Space Complexity: O(1) since we are using only a constant amount of extra space
def maxVowels(s, k):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    L, cnt, res = 0, 0, 0

    for R in range(len(s)):
        if s[R] in vowels:
            cnt += 1
        
        if R - L + 1 > k:
            if s[L] in vowels:
                cnt -= 1
            L += 1

        res = max(res, cnt)
    
    return res