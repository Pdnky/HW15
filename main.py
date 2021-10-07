import time

def timer(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print(f'Время выполнения функции: {end - start} секунд')
        return return_value

    return wrapper

@timer
def fib_plain(n):
    global counter
    counter += 1
    fib1 = fib2 = 1
    if n == 1 or n == 2:
        return fib1

    for i in range(n-2):
        time.sleep(0.1)
        fib1, fib2 = fib2, fib1 + fib2,

    return fib2


counter = 0
fibonachi = fib_plain(8)
print(fibonachi)