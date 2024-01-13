class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
            return
        prev_min = self.top_min()
        self.stack.append((val, min(val, prev_min)))

    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        top = (self.stack[-1])[0]
        return top

    def top_min(self) -> int:
        return (self.stack[-1])[1]

    def getMin(self) -> int:
        return self.top_min()


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
