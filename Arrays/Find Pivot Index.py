# https://leetcode.com/problems/find-pivot-index/description/


# prefix sum approach
# Time: O(n) and Space: O(1)
def pivotIndex(nums):
    total = sum(nums)
    left_sum = 0

    for i in range(len(nums)):
        right_sum = total - left_sum - nums[i]
        if left_sum == right_sum:
            return i
        left_sum += nums[i]

    return -1