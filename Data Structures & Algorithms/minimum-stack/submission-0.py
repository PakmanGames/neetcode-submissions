class MinStack:

    def __init__(self):
        self.stuff = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stuff.append(val)
        if len(self.mins) <= 0:
            self.mins.append(val)
        elif self.getMin() > val:
            self.mins.append(val)
        else:
            self.mins.append(self.getMin())

    def pop(self) -> None:
        self.stuff.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stuff[len(self.stuff) - 1]

    def getMin(self) -> int:
        return self.mins[len(self.mins) - 1]
