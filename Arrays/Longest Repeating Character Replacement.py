# https://leetcode.com/problems/longest-repeating-character-replacement/description/

# Sliding window
# Time Complexity: O(n)
# Space Complexity: O(1) since we are only storing frequency of characters in the current window, and there are only 26 uppercase English letters
def characterReplacement(s, k):
    cnt = {} # character frequency in current window
    L, longest = 0, 0
    n = len(s)

    for R in range(n):
        cnt[s[R]] = cnt.get(s[R], 0) + 1 # expand window

        while (R - L + 1) - max(cnt.values()) > k: # this formula is length of window - count of most frequent character in window, if this is greater than k, we need to shrink window
            cnt[s[L]] -= 1 # shrink window
            L += 1
        longest = max(longest, R - L + 1) # update longest length of valid window
    
    return longest

# optimized version without using max() function, we can keep track of the count of most frequent character in the window
def characterReplacement(s, k):
    cnt = {}
    L, longest, max_freq = 0, 0, 0
    n = len(s)

    for R in range(n):
        cnt[s[R]] = cnt.get(s[R], 0) + 1
        max_freq = max(max_freq, cnt[s[R]]) # update max frequency of any character in the window

        while (R - L + 1) - max_freq > k: # if we need to shrink window
            cnt[s[L]] -= 1
            L += 1
        
        longest = max(longest, R - L + 1) # update longest length of valid window
    
    return longest
