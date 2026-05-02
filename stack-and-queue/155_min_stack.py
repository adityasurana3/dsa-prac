class MinStack:

    def __init__(self):
        self.items = []

    def push(self, val: int) -> None:
        if len(self.items) == 0:
            self.items.append([val, val])
        else:
            min_val = min(self.items[-1][1], val)
            self.items.append([val, min_val])

    def pop(self) -> None:
        if len(self.items) == 0:
            return None
        self.items.pop()

    def top(self) -> int:
        if len(self.items) == 0:
            return -1
        return self.items[-1][0]

    def getMin(self) -> int:
        if len(self.items) == 0:
            return 0
        return self.items[-1][1]

    def __repr__(self):
        return f"Stack({self.items})"


stack = MinStack()
stack.push(10)
stack.push(20)
stack.push(5)
stack.push(60)

# stack.pop()
print(stack)

print(stack.getMin())
print(stack.top())
