# https://leetcode.com/problems/implement-stack-using-queues/description/

# using deque features

from collections import deque
class MyStack:
    def __init__(self):
        self.q = deque()

    # Time complexity: O(1)
    def push(self, x: int) -> None:
        self.q.append(x)
    
    # Time complexity: O(1)
    def pop(self) -> int:
        return self.q.pop()

    # Time complexity: O(1)
    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0


# using regular queue features
class MyStack:
    def __init__(self):
        self.q = deque()

    # Time complexity: O(1)
    def push(self, x: int) -> None:
        self.q.append(x)
    
    # Time complexity: O(n)
    def pop(self) -> int:
        for _ in range(len(self.q) - 1):
            self.push(self.q.popleft())
        return self.q.popleft()

    # Time complexity: O(1)
    def top(self) -> int:
        return self.q[-1]

    # Time complexity: O(1)
    def empty(self) -> bool:
        return len(self.q) == 0