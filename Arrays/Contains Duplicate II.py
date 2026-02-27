# https://leetcode.com/problems/contains-duplicate-ii/description/

# Sliding window
# Time Complexity: O(n)
# Space Complexity: O(min(n, k))

def containsNearbyDuplicate(nums, k):
    n = len(nums)
    window = set()
    L = 0

    for R in range(n):
        if R - L > k:
            window.remove(nums[L]) # maintain window size
            L += 1
        
        if nums[R] in window: # constant time lookup
            return True
        window.add(nums[R]) # expand window
    
    return False
