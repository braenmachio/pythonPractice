from functools import lru_cache

@lru_cache(maxsize=None) # let the cache grow without bound

def fib(n: int) -> int:
    if n < 2: # base case
        return n
    return fib(n-1)+fib(n-2) # recursive case

if __name__ == "__main__":
    print(fib(5))
    print(fib(50))