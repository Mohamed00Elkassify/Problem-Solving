# https://leetcode.com/problems/set-mismatch/

# solution 1
# Time complexity: O(n log n)
# Space complexity: O(n)


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        expected = [num for num in range(1, len(nums)+1)]
        duplicate, missing = 0, 0

        # find duplicate
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                duplicate = nums[i]
                break
        
        # find missing
        nums_set = set(nums)
        for num in expected:
            if num not in nums_set:
                missing = num
                break
        
        return [duplicate, missing]


# solution 2 - using set and sum difference
# Time complexity: O(n)
# Space complexity: O(n)
class Solution2:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        unique_sum = sum(set(nums))
        
        duplicate = actual_sum - unique_sum
        missing = expected_sum - unique_sum
        
        return [duplicate, missing]


nums = [3,2,3,4,6,5]
solution = Solution()
print(solution.findErrorNums(nums))

solution2 = Solution2()
print(solution2.findErrorNums(nums))