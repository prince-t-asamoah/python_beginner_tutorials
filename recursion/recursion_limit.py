from sys import getrecursionlimit, setrecursionlimit
print(getrecursionlimit()) # Initial limit is 1000

setrecursionlimit(2000)
print(getrecursionlimit()) # Limit is now 2000