# https://leetcode.com/problems/reverse-string/description/

# Two Pointers
# Time Complexity : O(n)
# Space Complexity : O(1)
def reverseString(s):
    L, R = 0, len(s) - 1
    # while L < R:
    for i in range(len(s) // 2):
        s[L], s[R] = s[R], s[L]
        L += 1
        R -= 1
    return s

s = ["h","e","l","l","o"]
print(reverseString(s))