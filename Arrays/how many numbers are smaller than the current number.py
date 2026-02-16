# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

# solution 1
# time complexity: O(n^2)
# space complexity: O(n)
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        res = []
        for num in nums:
            res.append(sorted_nums.index(num)) # index() costs O(n) time
        return res

#nums = [8,1,2,2,3]
#print(Solution().smallerNumbersThanCurrent(nums))


# solution 2
# time complexity: O(nlogn)
# space complexity: O(n)
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        cnt_dict = {}
        for i, num in enumerate(sorted_nums):
            if num not in cnt_dict:
                cnt_dict[num] = i
        return [cnt_dict[num] for num in nums]


nums = [8,1,2,2,3]
print(Solution().smallerNumbersThanCurrent(nums))