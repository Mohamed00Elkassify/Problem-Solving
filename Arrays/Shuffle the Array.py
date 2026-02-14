# https://leetcode.com/problems/shuffle-the-array/


# solution 1
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        #l = 0
        #r = l + n
        #res = []
        #for i in range(len(nums) // 2):
        #    res.append(nums[l])
        #    res.append(nums[r])
        #    l += 1
        #    r += 1
        res = []
        for i in range(len(nums) // 2):
            res += [nums[i], nums[i + n]]
        return res


# solution 2
# time complexity: O(n^2) - because insert and pop operations are O(n) in worst case
# Space complexity: O(1)

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n):
            nums.insert(2 * i + 1, nums.pop(n + i))
        return nums
nums = [2,5,1,3,4,7]
n = 3
print(Solution().shuffle(nums, n))
## Explanation of solution 2
'''The second solution uses an in-place approach to shuffle the array without using extra space for a new list. Here's how it works:
1. We iterate through the first half of the array (from 0 to n-1).
2. For each index i in the first half, we take the element from the second half (nums[n + i]) and insert it into the correct position in the first half.
3. The insert operation is done using the pop method to remove the element from its original position and then inserting it at the correct index (2 * i + 1) in the first half.
4. This way, we are effectively shuffling the array in place without needing additional space for a new list.
For example, if nums = [2,5,1,3,4,7] and n = 3:
- On the first iteration (i=0), we take nums[3] (which is 3) and insert it at index 1, resulting in [2,3,5,1,4,7].
- On the second iteration (i=1), we take nums[4] (which is 4) and insert it at index 3, resulting in [2,3,5,4,1,7].
- On the third iteration (i=2), we take nums[5] (which is 7) and insert it at index 5, resulting in [2,3,5,4,1,7].
This approach efficiently shuffles the array in place with a time complexity of O(n) and a space complexity of O(1).'''