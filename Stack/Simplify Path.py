# https://leetcode.com/problems/simplify-path/description/

# Stack
# time complexity: O(n) where n is the length of the input path
# space complexity: O(n) for the stack
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split("/")

        for p in paths:
            if p == "..": # move up to the parent directory
                if stack:
                    stack.pop() # move up to the parent directory by popping the last directory from the stack
            
            elif p != "." and p != "": # ignore current directory and empty strings
                stack.append(p)
        
        return "/" + "/".join(stack) # join the directories in the stack with "/" and prepend a "/" to form the simplified path