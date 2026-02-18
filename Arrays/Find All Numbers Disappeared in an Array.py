# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# solution 1
# time complexity: O(n^2)
# space complexity: O(n)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(1, len(nums)+1):
            if i not in nums: # in operator costs O(n) time
                res.append(i)
        return res

# solution 2
# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        num_set = set(nums)
        for i in range(1, len(nums)+1):
            if i not in num_set: # in operator costs O(1) time
                res.append(i)
        return res
