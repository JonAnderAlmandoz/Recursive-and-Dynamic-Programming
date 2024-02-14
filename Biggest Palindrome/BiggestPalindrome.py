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


# Recursive function to find the biggest palindrome
def b_pal(v):
    if len(v) == 0 or len(v) == 1:
        return v
    else:
        if v[0] == v[-1]:
            result = b_pal(v[1:-1])
            if len(result) == len(v[1:-1]):
                return v
        result_1 = b_pal(v[1:])
        result_2 = b_pal(v[:-1])
        if len(result_1) >= len(result_2):
            return result_1
        else:
            return result_2


def dyn_b_pal(v):
    return v


for i in range(10):
    list_ = []
    n = randint(0, 30)
    for j in range(n):
        list_.append(randint(0, 10))
    print("List: ", list_, ". Biggest pal.:", b_pal(list_))

