# https://leetcode.com/problems/maximum-subarray/

# solution 1 : Brute Force
# Time Complexity : O(n^2)
# Space Complexity : O(1)

def maxSubArray(nums):
    max_sum = nums[0]
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            max_sum = max(curr_sum, max_sum)
    return max_sum


# solution 2 : Kadane's Algorithm
# Time Complexity : O(n)
# Space Complexity : O(1)
def maxSubArray(nums):
    max_sum = nums[0]
    curr_sum = nums[0]
    for i in range(1, len(nums)):
        #if curr_sum < 0:
        #    curr_sum = 0
        #curr_sum += nums[i]
        curr_sum = max(curr_sum + nums[i], nums[i]) # shorter version of the above if statement
        max_sum = max(curr_sum, max_sum)
    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))
nums = [1]
print(maxSubArray(nums))
nums = [5,4,-1,7,8]
print(maxSubArray(nums))




# suppose we want to find the start and end indices of the maximum subarray
# we can use the same logic as Kadane's Algorithm
# but we need to keep track of the start and end indices
# if curr_sum < 0, it means that the current subarray is not contributing to the maximum sum
# so we start a new subarray from the current index
# so we update also the start index to the current index
# when we update the maximum sum, we also update the end index to the current index

# Time Complexity : O(n)
# Space Complexity : O(1)
def maxSubArray(nums):
    max_sum = nums[0]
    curr_sum = nums[0]
    start = 0
    end = 0
    for i in range(1, len(nums)):
        if curr_sum < 0:
            curr_sum = 0
            start = i
        curr_sum += nums[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
            end = i
    return start, end

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))
nums = [1]
print(maxSubArray(nums))
nums = [5,4,-1,7,8]
print(maxSubArray(nums))