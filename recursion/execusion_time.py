# Determine the execution time of a function in seconds
from timeit import timeit

recursive_setup_string = """
print("Recursive:")
def factorial(n: int):
    return 1 if n <= 1 else n * factorial(n - 1) 
"""
print('Recursive: ', timeit('factorial(4)', setup=recursive_setup_string, number=10000000))

itrative_setup_string = """
print("Iterative:")
def factorial(n: int):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
"""

print('Iteration: ',timeit('factorial(4)', setup=recursive_setup_string, number=10000000))

reduce_setup_string = """
from functools import reduce

def factorial_3(n: int):
    return reduce(lambda x, y: x * y, range(1, n + 1) or [1])
"""

print('Reduce: ', timeit('factorial(4)', setup=recursive_setup_string, number=10000000))

math_factorial_setup_string = 'from math import factorial'
print('Math module Factorial: ', timeit('factorial(4)', setup=math_factorial_setup_string, number=10000000))

