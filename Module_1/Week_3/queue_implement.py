class MyQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.capacity

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty."
        return self.items.pop(0)

    def enqueue(self, value):
        if self.is_full():
            return "Queue is full"
        self.items.append(value)

    def front(self):
        return self.items[0]


queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
queue1.enqueue(2)
print(queue1.is_full())
print(queue1.front())
print(queue1.dequeue())
print(queue1.front())
print(queue1.dequeue())
print(queue1.is_empty())
