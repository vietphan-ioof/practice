def rec(n):
    if n >= 1:
        return n * rec(n - 1)
    else:
        return 1


print(rec(2))

# Fibonacci Sequence


def fib(x):
    if x >= 3:
        return fib(x - 1) + fib(x - 2)
    else:
        return 1


print(fib(3))
