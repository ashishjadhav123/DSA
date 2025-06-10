
stack = []

# Push elements
stack.append(5)
stack.append(10)
stack.append(15)
stack.append(20)

# Pop element
stack.pop()

# Peek
top = stack[-1]

# Check if empty
is_empty = len(stack) == 0

print(stack)

print(top)

print(is_empty)