class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mins) == 0:
            self.mins.append(val)
        elif self.getMin() > val:
            self.mins.append(val)
        else:
            self.mins.append(self.getMin())

    def pop(self) -> None:
        self.mins.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
