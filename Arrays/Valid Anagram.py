# https://leetcode.com/problems/valid-anagram/


# solution 1
# Time Complexity : O(n log n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t) 
    

# solution 2
# Time complexity : O(n)
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq1 = Counter(s)
        freq2 = Counter(t)
        return freq1 == freq2
    
# solution 3
# Time complexity : O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS = {}
        countT = {}
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1 # if letter not in dict , get() return 0
            countT[t[i]] = countT.get(t[i], 0) + 1
        return countS == countT