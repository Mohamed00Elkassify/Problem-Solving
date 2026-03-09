# https://leetcode.com/problems/maximum-frequency-stack/description/

# O(n) space
class FreqStack:
    def __init__(self):
        self.freq = {}
        self.stack = []

    # Time complexity: O(1)
    def push(self, x: int) -> None:
        self.stack.append(x)
        self.freq[x] = self.freq.get(x, 0) + 1 # Increment the frequency of x in the freq dictionary

    # Time complexity: O(n)
    def pop(self) -> int:
        max_freq = max(self.freq.values())
        i = len(self.stack) - 1 # Start from the end of the stack to find the most recent element with the maximum frequency
        
        while self.freq[self.stack[i]] != max_freq: # Move backwards through the stack until we find an element with the maximum frequency
            i -= 1
        
        self.freq[self.stack[i]] -= 1 # Decrement the frequency of the popped element in the freq dictionary
        return self.stack.pop(i) # Remove and return the element at index i from the stack
