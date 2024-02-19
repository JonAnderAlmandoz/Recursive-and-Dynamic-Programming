import time

import numpy as np

def iter_method(n):
    if n == 0 or n == 1:
        return n
    else:
        a = 0
        b = 1
        for i in range(2, n+1):
            result = a + b
            a = b
            b = result
    return result


def r_method(n):
    if n == 0 or n == 1:
        return n
    else:
        return r_method(n-1) + r_method(n-2)


def dyn_method(n):
    list_ = np.zeros(n+1, dtype=int)
    if n == 0 or n == 1:
        return n
    else:
        list_[0] = 0
        list_[1] = 1
        for i in range(2, n+1):
            list_[i] = list_[i-1] + list_[i-2]

        return list_[-1]






for i in range(10):
    n = np.random.randint(1000)

    start = time.time()
    result = iter_method(n)
    end = time.time()

    print("Iter Method Result: ", result, ". Execution time: ", end-start)

    start = time.time()
    result = r_method(n)
    end = time.time()

    print("Recu Method Result: ", result, ". Execution time: ", end - start)

    start = time.time()
    result = dyn_method(n)
    end = time.time()

    print("Dyna Method Result: ", result, ". Execution time: ", end - start)

    print("")



