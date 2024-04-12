from typing import Dict
memo: Dict[int, int] = {0: 0,1: 1} # our base cases

def fib(n : int) -> int:
    if n not in memo:
        memo[n] = fib(n-1) + fib(n-2) # memoization
    return memo[n]

if __name__ == "__main__":
    print(fib(50))