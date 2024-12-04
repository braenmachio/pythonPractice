import time
from threading import Thread

count = 500000000

def countdown(n):
    while n > 0:
        n -= 1

t1 = Thread(target=countdown, args=(count//2,))
t2 = Thread(target=countdown, args=(count//2,))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print('Time taken: ', end - start)


# Time taken:  3.318697690963745 