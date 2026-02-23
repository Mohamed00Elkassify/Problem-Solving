# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# Two Pointers
# Time: O(n)
# Space: O(1)
def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        res = numbers[left] + numbers[right]
        if res < target:
            left += 1
        elif res > target:
            right -= 1
        else:
            return [left+1, right+1]