# https://leetcode.com/problems/number-of-subarrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/

# brute force
# Time Complexity: O(n*k) where n is the length of the input array and k
# is the size of the subarray. We iterate through the array once (O(n)) and for each starting index, we calculate the sum of the next k elements (O(k)).
# Space Complexity: O(1) since we are using only a constant amount of extra space   
def numOfSubarrays(arr, k, threshold):
    count = 0
    n = len(arr)
    for i in range(n - k + 1):
        if sum(arr[i:i+k]) / k >= threshold:
            count += 1
    return count