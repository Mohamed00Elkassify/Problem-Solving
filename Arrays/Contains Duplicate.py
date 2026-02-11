# https://leetcode.com/problems/contains-duplicate/

# solution 1
# Time complexity: O(n^2)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt = 0
        start = 0
        for i in range(1, len(nums)):
            if nums[start] in nums[start+1:]:
                cnt += 1
            start += 1
        return cnt > 0

# solution 2
# Time complexity: O(n)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

# solution 3
# Time complexity: O(n)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exist = set()
        for num in nums:
            if num in exist:
                return True
            exist.add(num)
        return False