# https://leetcode.com/problems/daily-temperatures/


# time complexity: O(n)
# space complexity: O(n)
def dailyTemperatures(temperatures):
    res = [0] * len(temperatures)
    stack = []

    for i, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            idx = stack.pop()
            res[idx] = i - idx
        
        stack.append(i)
    
    return res