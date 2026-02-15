# https://leetcode.com/problems/two-sum/description/

# solution 1: brute force
# time complexity: O(n^2)
# space complexity: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                

# solution 2
# time complexity: O(n^2)
# space complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target - nums[i] in nums[i+1:]:
                return [i, nums.index(target-nums[i], i+1)]

# solution 3: hash map
# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_idx = {}
        for i, num in enumerate(nums):
            if target - num in pair_idx:
                return [i, pair_idx[target-num]] # we can swap the order if we want to return the smaller index first
            pair_idx[num] = i
