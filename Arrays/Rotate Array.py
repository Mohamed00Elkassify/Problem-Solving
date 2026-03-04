# https://leetcode.com/problems/rotate-array/description/

# solution 1: using extra array
# time complexity: O(n)
# space complexity: O(n)
def rotate(nums, k):
    n = len(nums)
    rotated = [0] * n

    for i in range(n):
        rotated[(i + k) % n] = nums[i]

    nums[:] = rotated

    return nums

# solution 2: using reverse
# time complexity: O(n)
# space complexity: O(1)
def rotate(nums, k):
    n = len(nums)
    k = k % n

    # reverse the entire array
    nums.reverse()

    # reverse the first k elements
    nums[:k] = reversed(nums[:k])

    # reverse the remaining n-k elements
    nums[k:] = reversed(nums[k:])

    return nums
