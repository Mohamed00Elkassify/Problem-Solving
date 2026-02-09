# https://leetcode.com/problems/remove-element/

# solution 1
# Time complexity: O(n)
class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

nums = [1,1,2,3,4]
val = 1
print(Solution().removeElement(nums, val))

# solution 2
# Time complexity: O(n^2)
class Solution(object):
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)