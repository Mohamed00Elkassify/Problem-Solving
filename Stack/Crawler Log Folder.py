# https://leetcode.com/problems/crawler-log-folder/description/

# time: O(n) and space: O(n) 
def minOperations(logs):
    paths_stack = []
    for log in logs:
        if log == '../':
            if paths_stack: # if the stack is not empty, we can pop the last path to go back to the previous directory
                paths_stack.pop()
        elif log != './': # if the log is not './', we can add it to the stack as a new path
            paths_stack.append(log)
    
    return len(paths_stack)