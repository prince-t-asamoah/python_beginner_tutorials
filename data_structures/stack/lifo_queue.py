from queue import LifoQueue

stack = LifoQueue(maxsize=3)

print('Initial stack', stack.qsize())

stack.put('a')
stack.put('b')
stack.put('c')

print('Stack full: ', stack.full())
print('Stack size: ', stack.qsize())

print('Stack elements after popped from stack')
print(stack.get())
print(stack.get())
print(stack.get())

print('Stack Empty:', stack.empty())