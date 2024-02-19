# In order to create a recursive function to resolve this problem, we first need to declare the answers for the simplest cases:
# c1: v = [] -> b_pal(v) = [] = v
# c2: v = [x] -> b_pal(v) = [x] = v
# c3: v = [x, y] -> if x == y b_pal(v) = [x,y]
#                -> if x != y b_pal(v) = [x] | [y]
# c4: v = [x, y, z] -> if x == z b_pal(v) = [x, z]
#                   -> if x != z b_pal(v) = x_pal([x, y]) | x_pal([y, z])

# We can observe that the first two cases are straightforward, and that it does not matter what the value of x is,
# the answer will always be v.
# But, when we increase the number of elements in the list, it gets more complicated.
# The logic behind my algorithm lies in considering that when we have two elements or more, we need to verify that the
# first and last elements are equal, in case they are and the vector inside also is a palindrome,
# v itself is palindrome.
# But, if the palindrome of the v[1:-1] is not of the length of v[1,-1],
# even though v[0] == v[-1], the biggest palindrome is the palindrome of the inside list.
# In case v[0] != v[-1], the biggest palindrome will be inside v[1:] or v[:-1].
#
# We can observe that, this recursive function is not the best, as we need to execute the function
# once or twice, making the cost double.

from random import randint
import time
import numpy as np


# Recursive function to find the biggest palindrome
def r_b_pal(v):
    if len(v) == 0 or len(v) == 1:
        return v
    else:
        if v[0] == v[-1]:
            result = r_b_pal(v[1:-1])
            if len(result) == len(v[1:-1]):
                return v
        result_1 = r_b_pal(v[1:])
        result_2 = r_b_pal(v[:-1])
        if len(result_1) >= len(result_2):
            return result_1
        else:
            return result_2


# This function finds the biggest palindrome iteratively, starting with the biggest one possible.
# When a palindrome is found, the function finishes the execution,
# as the next found palindrome will never be bigger than the previous.
def i_b_pal(v):
    if len(v) == 0 or len(v) == 1:
        return v
    else:
        j = 0
        i = len(v)
        curr_b_pal = [v[0]]
        while i >= 1:
            for j in range(0, len(v)):
                if j+i > len(v):
                    break
                if is_pal(v[j:j+i]):
                    if len(v[j:j+i]) > len(curr_b_pal):
                        return v[j:j+i]
                    j += 1
                else:
                    j += i
            i -= 1
    return curr_b_pal


# This function finds the biggest palindrome using dynamic programming.
def dyn_b_pal(v):
    matr = np.identity(len(v))
    for i in range(0, len(matr)-1):
        for j in range(i+1, len(v)):
            if v[i] == v[j]:
                matr[i][j] = 1

    i_top = 0
    j_top = len(v)-1

    j_top_init = len(v) - 1


def dig_exists(matr, i, j):
    while j > i:
        if matr[i][j]:
            i += 1
            j -= 1
        else:
            return False
    return True





# This function is used by the iterative function to know whether a list is a palindrome.
def is_pal(v):
    length = len(v)
    if length == 0 or length == 1:
        return True
    else:
        left_i = 0
        right_j = length-1
        while v[left_i] == v[right_j] and left_i < right_j:
            left_i += 1
            right_j -= 1
        if left_i >= right_j:
            return True
        else:
            return False


# This function permits compare the execution times of the created methods.
# We can add infinite number of methods in this python file, but they must be called method_x.
def comp_method_times():
    avg_recursive = 0
    avg_iterative = 0

    for i in range(10):
        list_ = []
        for j in range(23):
            list_.append(randint(0, 10))

        start = time.time()
        v = r_b_pal(list_)
        end = time.time()

        print("Recursive exec time: ", end-start, "V_in: ", list_, "  V_out: ", v)
        avg_recursive += end-start

        start = time.time()
        v = i_b_pal(list_)
        end = time.time()

        print("Iterative exec time: ", end - start, "V_in: ", list_, "  V_out: ", v)
        avg_iterative += end - start

    print("Recursive avg exec time: ", avg_recursive/10)
    print("Iterative avg exec time: ", avg_iterative/10)


#comp_method_times()
print(dyn_b_pal([0,1,2,3,2,3]))
print(dyn_b_pal([1,2,3,2,3,2,5,6,5,7,8,7,6,5,4,5,6,5,4,3,2,3,4,3,2,3,4,5,4]))