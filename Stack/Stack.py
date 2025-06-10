
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return "Empty stack"

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        return "Empty stack"

    def is_empty(self):
        # if len(self.stack) == 0:
        #     return "Yes"
        # else:
        #     return "No"

        return "Yes" if len(self.stack) == 0 else "No"

    def print_stack(self):
        print("Stack (top → bottom):", list(reversed(self.stack)))

if __name__ == "__main__":
    root = Stack()

    root.push(data=5)
    root.push(data=10)
    root.push(data=15)
    root.push(data=20)

    root.print_stack()

    print(root.is_empty())

    print(root.peek())

    root.print_stack()

    root.pop()

    root.print_stack()