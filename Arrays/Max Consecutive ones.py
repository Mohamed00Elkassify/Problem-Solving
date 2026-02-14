# https://leetcode.com/problems/max-consecutive-ones/

# solution 1
# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        maximum = 0
        for num in nums:
            if num == 1:
                curr += 1
            else:
                curr = 0
            maximum = max(curr, maximum)
        return maximum
