# https://leetcode.com/problems/minimum-size-subarray-sum/description/


# Sliding window
# Time Complexity: O(n)
# Space Complexity: O(1)
def minSubArrayLen(target, nums):
    min_length = float('inf')
    L, curr = 0, 0
    n = len(nums)
    for R in range(n):
        curr += nums[R] # expand window

        while curr >= target: # shrink window until sum is less than target
            min_length = min(min_length, R - L + 1) # update min length
            curr -= nums[L] # shrink window
            L += 1 # move left pointer
    
    if min_length == float('inf'): # no valid subarray found
        return 0
    return min_length