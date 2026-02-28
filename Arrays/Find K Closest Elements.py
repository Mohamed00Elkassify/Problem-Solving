# https://leetcode.com/problems/find-k-closest-elements/description/

# Two Pointers
# Time complexity : O(n - k)
# Space complexity : O(K)
def findClosestElements(arr, k, x):
    L, R = 0, len(arr) - 1

    while R - L >= k:
        if abs(x - arr[L]) <= abs(x - arr[R]):
            R -= 1
        else:
            L += 1
    
    return arr[L : R + 1]

arr = [2,4,5,8]
x = 6
k = 2
print(findClosestElements(arr, k, x))