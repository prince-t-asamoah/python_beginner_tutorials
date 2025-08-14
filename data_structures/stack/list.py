# Example to demonstrate stack implementation using list
stack = []

stack.append('a')
stack.append('a')
stack.append('c')

print('Initial stack', stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())

print('Stack after pop', stack)