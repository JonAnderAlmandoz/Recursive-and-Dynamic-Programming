import numpy as np


def iter_method(n):
    temp_1 = 1
    for i in range(1, n+1):
        temp_1 *= i
    temp_2 = temp_1 * (i+1)

    temp_3 = temp_1
    for i in range(n+1, 2*n+1):
        temp_3 *= i

    return temp_3/(temp_1*temp_2)


def r_method(n):
    if n <= 1:
        return 1
    else:
        res = 0
        for i in range(n):
            res += r_method(i) * r_method(n-i-1)
        return res





print(iter_method(9))
print(iter_method(15))

print(r_method(9))
print(r_method(15))


