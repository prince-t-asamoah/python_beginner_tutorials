# Using recursion
def factorial_1(n: int):
    print(f"factorial() called wih n = {n}")
    result = 1 if n <= 1 else n * factorial_1(n - 1)
    print(f"-> factorial({n}) returns {result}")
    return result


# Using Iteration
def factorial_2(n: int):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


from functools import reduce


def factorial_3(n: int):
    return reduce(lambda x, y: x * y, range(1, n + 1) or [1])


# Using in built factorial from math module
import math

print("Using recursion: ", factorial_1(4))
print("Using iteration:", factorial_2(4))
print("Using reduce function:", factorial_3(4))
print("Using math factorial module:", math.factorial(4))
