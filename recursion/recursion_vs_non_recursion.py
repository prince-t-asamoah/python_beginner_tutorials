# With recursions
def countdown_1(n: int):
    print(n)
    if n == 0:
        return
    else:
        countdown_1(n - 1)

def countdown_2(n: int):
    print(n)
    if n > 0:
        countdown_2(n  - 1)

# No recursions
def countdown_3(n: int):
    while n >= 0:
        print(n)
        n -= 1
    
countdown_1(5)
countdown_2(5)
countdown_3(5)
