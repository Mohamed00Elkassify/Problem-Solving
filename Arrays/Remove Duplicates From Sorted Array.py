# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import List

# Solution 1
# Time complexity: O(n^3)
#class Solution:
#    def removeDuplicates(self, nums: List[int]) -> int:
#        for num in nums:
#            while nums.count(num) > 1:
#                nums.remove(num)
#        return len(nums)
#
#
#
## Solution 2
## Time complexity: O(n)
#class Solution:
#    def removeDuplicates(self, nums: List[int]) -> int:
#        if not nums:
#            return 0
#        start = 0
#        for i in range(1, len(nums)):
#            if nums[start] != nums[i]:
#                start += 1
#                nums[start] = nums[i]
#        return start + 1
#
#input = [2,10,10,30,30,30]
#print(Solution().removeDuplicates(input))



#solution 3
# Time complexity: O(n)
from collections import Counter

class Solution:
    def removeDuplicates(self, nums):
        cnt = Counter(nums)
        i = 0
        for num in cnt.keys():
            nums[i] = num
            i += 1
        return i

input = [2,10,10,30,30,30]
print(Solution().removeDuplicates(input))