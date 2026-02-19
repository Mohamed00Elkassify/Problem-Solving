# https://leetcode.com/problems/valid-triangle-number/

# solution 1: O(n^2)
# Two-pointer
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        for k in range(2, n):  # k is the largest side
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += j - i
                    j -= 1
                else:
                    i += 1
        return count