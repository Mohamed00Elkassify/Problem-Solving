# https://leetcode.com/problems/implement-queue-using-stacks/description/


# use 2 stacks, use only standard stack operations (push, pop, peek, empty)
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # Time complexity: O(1)
    def push(self, x: int) -> None:
        self.stack1.append(x)

    # Time complexity: O(n) in the worst case, but amortized O(1)
    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
                
        return self.stack2.pop()

    # Time complexity: O(n) in the worst case, but amortized O(1)
    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        return self.stack2[-1]
    
    # Time complexity: O(1)
    def empty(self) -> bool:
        return not self.stack1 and not self.stack2