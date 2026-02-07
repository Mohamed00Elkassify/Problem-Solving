# https://leetcode.com/problems/concatenation-of-array/description/

from pyparsing import List

# solution 1
#* Time complexity: O(n)
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums
        ans.extend(nums)
        return ans


# solution 2
#* Time complexity: O(n)
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums


# solution 3 (2 iterations)
# Time complexity: O(n)
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans


# solution 4 (1 iteration)
# Time complexity: O(n)
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        for i, num in enumerate(nums):
            ans[i] = ans[i + n] = num
        return ans