from time import sleep
from datetime import datetime

def timeit(iters):
    def decorator(func):
        def timer(*args):
            start_time = datetime.now()
            for i in range(iters):
                func(*args)
            end_time = datetime.now()
            print('Execution time: ', end_time - start_time , '.s')
            print(func(*args))
            return func
        return timer
    return decorator




def main():
    num_1 = int(input('1-st number : '))
    num_2 = int(input('2-nd number : '))
    iters = int(input('Number of iterations: '))

    @timeit(iters)
    def slow_add(a: int, b: int) -> int:
        sleep(1)
        return a + b

    slow_add(num_1,num_2)


if __name__ == '__main__':
    main()
    print("-- Successfully Compiled")
else:
    print("-- Error")


# from time import sleep
# >>>
# >>> @timeit
# >>> def slow_add(a: int, b: int) -> int:
# ...     sleep(1)
# ...
# ...     return a + b
# >>>
# >>> slow_add(1, 2)
# Execution time: 1 s
# 3
# >>>
# >>> @timeit(7)
# >>> def slow_add(a: int, b: int) -> int:
# ...     sleep(1)
# ...
# ...     return a + b
# >>>
# >>> slow_add(1, 2)
# Execution time: 1 s +- 0.0003 s (mean ± std. dev. of 7 runs)