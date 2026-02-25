

# https://leetcode.com/problems/trapping-rain-water/

# Suffix & Prefix arrays
# Time: O(n)
# Space: O(n)

# this solution is based on the fact that the amount of water trapped at each index is the minimum of the maximum height to the left and the maximum height to the right, minus the height of the current element
# water level = min(maxLeft, maxRight)
# trapped water = water level - height
# we use technique called suffix and prefix maximum
# suffix maximum is the maximum height to the right of each element
# prefix maximum is the maximum height to the left of each element

def trap(height):
    n = len(height)
    if n == 0:
        return 0
    
    maxLeft = [0] * n # stores the maximum height to the left of each element
    maxRight = [0] * n # stores the maximum height to the right of each element

    # calculate maxLeft of each element
    maxLeft[0] = height[0]
    for i in range(1, n):
        maxLeft[i] = max(maxLeft[i-1], height[i])

    # calculate maxRight of each element
    maxRight[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        maxRight[i] = max(maxRight[i+1], height[i])
    
    # calculate trapped water
    res = 0
    for i in range(n):
        res += min(maxLeft[i], maxRight[i]) - height[i]
    
    return res


height = [0,2,0,3,1,0,1,3,2,1] # 9
print(trap(height))