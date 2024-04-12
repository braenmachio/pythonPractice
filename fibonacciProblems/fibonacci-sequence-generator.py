from typing import Generator

def fib(n: int) -> Generator[int, None, None]:
    '''
    if the end of the function is reached and there are no more
    yiled statements, the loop finishes iterating
    '''
    yield 0             # special case
    if n > 0: yield 1   # another special case

    last: int = 0
    next: int = 1

    for _ in range(1, n):
        last, next = next, last+next
        yield next      # the main generation step

if __name__ == "__main__":
    for i in fib(50):
        print(i)