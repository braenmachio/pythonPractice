def fib(n: int) -> int:
    if n == 0: return n # special case
    last: int = 0 # initially set to fib(0)
    next: int = 1 # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last+next
    return next
if __name__ == "__main__":
    print(fib(5))
    print(fib(55))

'''
variable swap, btn last and next.
the for loop runs a max on n - 1 times 
'''