# https://leetcode.com/problems/subarray-sum-equals-k/

# brute force approach
# Time: O(n^2) and Space: O(1)
def subarraySum(nums, k):
        res = 0
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                if cur_sum == k:
                    res += 1
        return res


# prefix sum approach
# Time: O(n) and Space: O(n)
def subarraySum(nums, k):
    res, cur_sum = 0,  0
    prefix_sum = {0 : 1} # this is for the case when the subarray starts from index 0

    for num in nums:
         cur_sum += num
         diff = k - cur_sum # if there is a prefix sum that is equal to the current sum - k, then there is a subarray that sums to k

         res += prefix_sum.get(diff, 0) # if there are multiple prefix sums that are equal to the current diff, then there are multiple subarrays that sum to k
         prefix_sum[cur_sum] = prefix_sum.get(cur_sum, 0) + 1 # add the current prefix sum to the dictionary , so that it can be used for future subarrays

    return res