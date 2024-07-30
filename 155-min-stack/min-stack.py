class MinStack:

    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.main_stack:
            top = self.main_stack.pop()
            if top == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.main_stack:
            return self.main_stack[-1]
        return None

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()