# recursive attempt - a fcn that calls itself
'''
the sum of any two numbers save the first two
is the sum of the two previous numbers
    fib(n) = fib(n-1) + fib(n-2)
'''

def fib(n: int) -> int:
    return fib(n-1) + fib(n-2)

if __name__ =="__main__":
    print(fib(5))
'''
Previous line repeated 996 more times
RecursionError: maximum recursion depth exceeded
'''