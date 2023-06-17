class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


# Example usage
operations = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
values = [[], [-2], [0], [-3], [], [], [], []]

min_stack = MinStack()
output = []
for op, val in zip(operations, values):
    if op == "MinStack":
        output.append(None)
    elif op == "push":
        min_stack.push(val[0])
        output.append(None)
    elif op == "pop":
        min_stack.pop()
        output.append(None)
    elif op == "top":
        output.append(min_stack.top())
    elif op == "getMin":
        output.append(min_stack.getMin())

print("Result:", output)
