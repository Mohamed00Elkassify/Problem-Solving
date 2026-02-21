# https://leetcode.com/problems/3sum/description/

# Two Pointers
# Time: O(n^2)
# Space: O(1) without counting the space used for the output

def three_sum(nums):
    nums.sort()
    res = []
    for k in range(2, len(nums)):
        if k < len(nums) - 1 and nums[k] == nums[k+1]:
            continue
        i, j = 0, k-1
        while i < j:
            total = nums[i] + nums[j] + nums[k]
            if total == 0:
                res.append([nums[i], nums[j], nums[k]])
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i - 1]:
                    i += 1
                while i < j and nums[j] == nums[j + 1]:
                    j -= 1
            elif total < 0:
                i += 1
            else:
                j -= 1
    return res
nums = [0, 0, 0, 0]
print(three_sum(nums))