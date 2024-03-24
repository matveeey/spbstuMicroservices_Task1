import time

from palindrome import pali_check

def ToF(func):
    def wrapper(*args, **kwargs):
        start_t = time.perf_counter()
        func(*args, **kwargs)
        end_t = time.perf_counter()
        total_t = end_t - start_t
        print(f'{func.__name__} was in run for {total_t:.6f} seconds')
    return wrapper

@ToF
def test_func(k):
    print(k)
    for i in range(2000000):
        i += 1
        i -= 2

@ToF
def test_func2():
    for i in range(4000000):
        i += 1
        i -= 2

if __name__ == '__main__':
    test_func(2)
    test_func2()