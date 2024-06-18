class MyStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []
        self.index_top = -1

    def is_empty(self):
        return self.index_top == -1

    def is_full(self):
        return self.index_top == self.capacity - 1

    def pop(self):
        if self.is_empty():
            return "Stack is empty."
        self.index_top -= 1
        return self.items.pop()

    def push(self, value):
        if self.is_full():
            return "Stack is full."
        self.items.append(value)
        self.index_top += 1

    def top(self):
        return self.items[self.index_top]


stack1 = MyStack(capacity=5)
print(stack1.is_empty())
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.push(5)
print(stack1.is_full())
print(stack1.pop())
# print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.is_empty())
