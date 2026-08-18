class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mins) <= 0:
            self.mins.append(val)
        elif self.getMin() < val:
            self.mins.append(self.getMin())
        else:
            self.mins.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.mins[len(self.mins) - 1]
