HW_SOURCE_FILE = 'hw04.py'


###############
#  Questions  #
###############

def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st + ave) * (st + ave + 1) // 2 + ave


def street(inter):
    return w(inter) - avenue(inter)


def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2


w = lambda z: int(((8 * z + 1) ** 0.5 - 1) / 2)


def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    # >>> times_square = intersection(46, 7)
    # >>> ess_a_bagel = intersection(51, 3)
    # >>> taxicab(times_square, ess_a_bagel)
    9
    # >>> taxicab(ess_a_bagel, times_square)
    9
    """
    "*** YOUR CODE HERE ***"
    return abs(street(a) - street(b)) + abs(avenue(a) - avenue(b))


def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    # >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    # >>> squares(seq)
    [7, 3, 1, 10]
    # >>> seq = [500, 30]
    # >>> squares(seq)
    []
    """
    "*** YOUR CODE HERE ***"

    def is_square(x):
        for i in range(0, x + 1):
            if i ** 2 == x:
                return i
        return False

    return [int(x ** (1 / 2)) for x in s if is_square(x)]


def g(n):
    """Return the value of G(n), computed recursively.

    # >>> g(1)
    1
    # >>> g(2)
    2
    # >>> g(3)
    3
    # >>> g(4)
    10
    # >>> g(5)
    22
    # # >>> from construct_check import check
    # # >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)


def g_iter(n):
    """Return the value of G(n), computed iteratively.

    # >>> g_iter(1)
    1
    # >>> g_iter(2)
    2
    # >>> g_iter(3)
    3
    # >>> g_iter(4)
    10
    # >>> g_iter(5)
    22
    # # >>> from construct_check import check
    # # >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    g1 = 1
    g2 = 2
    g3 = 3
    if n <= 3:
        return n
    i = 4
    while i <= n:
        g4 = g3 + 2 * g2 + 3 * g1
        g1 = g2
        g2 = g3
        g3 = g4
        i += 1
    return g4


def count_partition(n, m, s=""):
    if n == 0:
        print(s[1:])
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        return count_partition(n - m, m, str(s) + "+" + str(m)) + count_partition(n, m - 1, str(s))


# count_partition(5, 5)


def count_change(amount):
    """Return the number of ways to make change for amount.

    # >>> count_change(7)
    6
    # >>> count_change(10)
    14
    # >>> count_change(20)
    60
    # >>> count_change(100)
    9828
    # # >>> from construct_check import check
    # # >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"

    import math

    def count_helper(amount, change_pow):
        if amount == 0:
            return 1
        if amount < 0:
            return 0
        elif change_pow < 0:
            return 0
        else:
            return count_helper(amount, change_pow - 1) + \
                   count_helper(amount - 2 ** change_pow, change_pow)

    return count_helper(amount, int(math.log2(amount)))


# print(count_change(127))

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    # >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    # >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    # >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    aux = 6 - start - end
    if n == 1:
        print_move(start, end)
    else:
        move_stack(n - 1, start, aux)
        move_stack(1, start, end)
        move_stack(n - 1, aux, end)


move_stack(3, 1, 3)

###################
# Extra Questions #
###################

from operator import sub, mul


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    # >>> make_anonymous_factorial()(5)
    120
    # # >>> from construct_check import check
    # >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    # def f(n):
    #     if n == 1: return 1
    #     return mul(n, f(sub(n,1)))
    return (lambda a: lambda v: a(a, v))(lambda s, x: 1 if x == 0 else mul(x, s(s, sub(x, 1))))

# print(make_anonymous_factorial()(5))
