# https://leetcode.com/problems/sort-colors/description/

# Time: O(n) and Space: O(1)
def sortColors(nums):
        cnt = [0] * 3 # count of 0, 1, 2
        for num in nums:
            cnt[num] += 1  # increment count of each color
        
        idx = 0 # index to place the color
        for i in range(3): # iterate over colors
            while cnt[i]: # while count of color is not zero
                cnt[i] -= 1
                nums[idx] = i
                idx += 1
        return nums

nums = [2,0,2,1,1,0]
print(sortColors(nums))