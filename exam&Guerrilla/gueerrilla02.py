# Higher Order Functions
# Question 1
# Write a make_skipper , which takes in a number n and outputs a function. When this function
# takes in a number x , it prints out all the numbers between 0 and x, skipping every n th number
# (meaning skip any value that is a multiple of n).


def make_skipper(n):
    # “””
    # >>> a = make_skipper(2)
    # >>> a(5)
    # 1
    # 3
    # 5
    # “”””
    def skipper(k):
        for i in range(1, k + 1):
            if i % n != 0: print(i)

    return skipper


# a = make_skipper(2)
# a(5)

# EXTRA: Question 2
# Write make_alternator which takes in two functions, f and g, and outputs a function. When this
# function takes in a number x , it prints out all the numbers between 1 and x, applying the function
# f to every odd-indexed number and g to every even-indexed number before printing.
def make_alternator(f, g):
    # “””
    # >>> a = make_alternator(lambda x: x * x, lambda x: x + 4)
    # >>> a(5)
    # 1
    # 6
    # 9
    # 8
    # 25
    # >>> b = make_alternator(lambda x: x * 2, lambda x: x + 2)
    # >>> b(4)
    # 2
    # 4
    # 6
    # 6
    # “””
    def alternator(n):
        for i in range(1, n + 1, 2):
            print(f(i))
            if i + 1 < n + 1:  # last number is odd or even?
                print(g(i + 1))

    return alternator


# a = make_alternator(lambda x: x * x, lambda x: x + 4)
# a(5)
# b = make_alternator(lambda x: x * 2, lambda x: x + 2)
# b(4)


# RECURSION
# b) What does the following cascade2 do?
def cascade2(n):
    print(n)
    if n >= 10:
        cascade2(n // 10)
        print(n)


# cascade2(123456)


# c) Describe what does each of the following functions mystery and fooply do. Identify the three
# things from Q0a:
def mystery(n):
    if n == 0:
        return 0
    else:
        return n + mystery(n - 1)


# print(mystery(5))


def foo(n):
    if n < 0:
        return 0
    return foo(n - 2) + foo(n - 1)


# print(foo(5))


def fooply(n):
    if n < 0:
        return 0
    return foo(n) + fooply(n - 1)


# print(fooply(5))


# Question 2
# Mario needs to jump over a series of Piranha plants, represented as an integer composed of 0’s
# and 1’s. Mario only moves forward and can either step (move forward one space) or jump (move
# forward two spaces) from each position. How many different ways can Mario traverse a level
# without stepping or jumping into a Piranha plant? Assume that every level begins with a 1
# (where Mario starts) and ends with a 1 (where Mario must end up).
def mario_number(level):
    """
    Return the number of ways that Mario can traverse the level,
    where Mario can either hop by one digit or two digits each turn.
    A level is defined as being an integer with digits where a 1 is
    something Mario can step on and 0 is something Mario cannot step
    on.
    """
    # print("level is:", level)
    if level % 1000 == 111:
        return mario_number(level // 100) + 2
    elif level % 1000 == 101:
        return mario_number(level // 100)
    else:
        return 0


# print(mario_number(10101))  # Hops each turn: (1, 2, 2)
# print(mario_number(11101))  # Hops each turn: (1, 1, 1, 2), (2, 1, 2)
# print(mario_number(100101))  # No way to traverse through level
# print(mario_number(101101)) # should be 1


# EXTRA Challenge: Question 3
# Implement the combine function, which takes a non-negative integer n, a two-argument function
# f, and a number result. It applies f to the first digit of n and the result of combining the rest of the
# digits of n by repeatedly applying f (see the doctests). If n has no digits (because it is zero),
# combine returns result. Assume n is non negative.
from operator import add, mul


def combine(n, f, result):
    """
    Combine the digits in n using f.
    >>> combine (3, mul, 2) # mul (3, 2)
    6
    >>> combine (43, mul, 2) # mul (4, mul (3, 2))
    24
    >>> combine (6502, add, 3) # add (6, add (5, add (0, add (2 , 3)))
    16
    >>> combine (239, pow, 0) # pow (2, pow (3, pow (9, 0)))
    8
    """
    if n == 0:
        return result
    else:
        return f(n % 10, combine(n // 10, f, result))


print(combine(3, mul, 2))
print(combine(6502, add, 3))
