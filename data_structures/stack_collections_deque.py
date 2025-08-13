# Example to demonstrate stack implementation using collections.deque

from collections import deque

stack = deque()

stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack: ', stack)

print('Items popped from stack')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('Current stack after pop:', stack)
