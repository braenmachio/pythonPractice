from multiprocessing import Pool
import time
# from single_thread import countdown
count = 500000000

def countdown(n):
    while n > 0:
        n -= 1

countdown(count)

if __name__ == '__main__':
    pool = Pool(processes=2)

    start = time.time()
    r1 = pool.apply_async(countdown, [count//2])
    r2 = pool.apply_async(countdown, [count//2])
    pool.close()
    pool.join()
    end = time.time()

    print('Time taken in seconds: ', end - start)