# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/

# Brute Force
# Time Complexity: O(n*k)
# Space Complexity: O(1)

def NumOfSubArrays(arr, k, threshold):
        res = 0
        L = 0
        n = len(arr)
        
        for R in range(k-1, n):
            curr_sum = 0
            for i in range(L, R+1):
                curr_sum += arr[i]
            
            if curr_sum / k >= threshold:
                res += 1
            
            L += 1

        return res

print(NumOfSubArrays([2,2,2,2,5,5,5,8], 3, 4))
    
# Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(1)
def NumOfSubArrays(arr, k, threshold):
    res = 0
    curr_sum = sum(arr[:k]) # sum of first k elements
    
    if curr_sum / k >= threshold:
        res += 1
    
    for i in range(k, len(arr)):
        curr_sum += arr[i] - arr[i-k] # add the current element (end of the window) and remove the first element (start of the window) before the window moves forward

        if curr_sum / k >= threshold:
            res += 1
    
    return res
print(NumOfSubArrays([2,2,2,2,5,5,5,8], 3, 4))


# Another version without duplicate if condition but with sum of first k-1 elements
def NumOfSubArrays(arr, k, threshold):
    res = 0
    curr_sum = sum(arr[:k-1]) # sum of first k-1 elemnts

    for i in range(k-1, len(arr)):
        curr_sum += arr[i] # add the current element (end of the window)
        if curr_sum / k >= threshold:
            res += 1
        
        curr_sum -= arr[i - (k-1)] # remove the first element (start of the window) before the window moves forward
    
    return res
print(NumOfSubArrays([2,2,2,2,5,5,5,8], 3, 4))