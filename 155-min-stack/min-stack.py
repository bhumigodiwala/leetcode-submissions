class MinStack:

    def __init__(self):
        # Create two stacks
        # 1. Normal stack to keep track of values entered in it
        # 2. Min stack to keep track of minimum value at every point in stack
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        (self.stack).append(val)
        if self.minStack:
            val = min(val, self.minStack[-1])
        else:
            val
        (self.minStack).append(val)

    def pop(self) -> None:
        # Approach 1: Using pop method
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()