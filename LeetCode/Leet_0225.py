"""
    @ Leet 0225. Implement Stack using Queues
    @ Prob. https://leetcode.com/problems/implement-stack-using-queues/
      Ref.
    @ Algo: Stack
    @ Start day: 20. 07. 27.
    @ End day: 20. 07. 27.
"""

from collections import deque

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        if __name__ == '__main__':
            self.q = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()