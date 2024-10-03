import math

# limit: ~ 300 digits
def fibo_binet(n: int) -> int:
    # Prototype:
    # choice 1 (with no hints)
    # pass
    # choice 2
    # return -1
    # choice
    #raise NotImplemented()

    # Impl: Binet formula
    phi = (1 + math.sqrt(5)) / 2
    fib_n = (phi**n - (-1 / phi)**n) / math.sqrt(5)
    return round(fib_n)

# limit: ~ 4000 digits
def fibo_iterative(n: int) -> int:
    x1 = 0
    if n == 0:
        return x1
    x2 = 1
    if n == 1:
        return x2
    # if n >=2, loop is done at least once
    for _ in range(n-1):
        x1, x2 = x2, x1 + x2
    return x2
        