class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        if len(self.stack) <= 0:
            self.mins.append(val)
        elif self.mins[len(self.mins) - 1] < val:
            self.mins.append(self.mins[len(self.mins) - 1])
        else:
            self.mins.append(val)
        self.stack.append(val)
        

    def pop(self) -> None:
        self.mins.pop()
        self.stack.pop()

    def top(self) -> int:
        top = self.stack.pop()
        self.stack.append(top)
        return top

    def getMin(self) -> int:
        minimum = self.mins.pop()
        self.mins.append(minimum)
        return minimum
