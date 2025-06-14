
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.appendleft(value)

    def dqueue(self):
        if len(self.queue) > 0:
            return self.queue.popleft()
        return "Empty Queue"
    def pop(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return "Empty Queue"

    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]
        return "Empty Queue"

    def size(self):
        return len(self.queue)

    def print_queue(self):
        print(f"Queue (front → rear): {list(self.queue)}")


if __name__ == "__main__":
    root = Queue()

    root.enqueue(value=5)
    root.enqueue(value=10)
    root.enqueue(value=15)
    root.enqueue(value=20)

    root.print_queue()

    print(root.dqueue())

    root.print_queue()

    print(root.peek())

    print(root.size())

    print(root.pop())

    root.print_queue()
