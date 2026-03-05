# https://leetcode.com/problems/left-and-right-sum-differences/description

# prefix and postfix approach
# Time: O(n) and Space: O(n)
def leftRightDifference(nums):
    n = len(nums)
    res = [0] * n
    # Left-to-right pass: accumulate sum of elements on the left
    left_sum = 0
    for i in range(n):
        res[i] += left_sum
        left_sum += nums[i]
    # Right-to-left pass: accumulate sum of elements on the right
    right_sum = 0   
    for i in range(n-1, -1, -1):
        res[i] = abs(res[i] - right_sum)
        right_sum += nums[i]
    
    return res


# one pass approach decrementing the right sum and incrementing the left sum in the same loop
# Time: O(n) and Space: O(n)
def leftRightDifference(nums):
    n = len(nums)
    prefix = 0
    postfix = sum(nums)
    res = []

    for i in range(n):
        postfix -= nums[i] # the right sum is the total sum minus the current element
        res.append(abs(prefix - postfix)) # the difference between the left sum and the right sum is the absolute value of the difference between the prefix and postfix sums
        prefix += nums[i] # the left sum is the prefix sum plus the current element, so we add the current element to the prefix sum for the next iteration
    return res
