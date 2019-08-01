def reverse(lst):
    if len(lst) <= 1:
        return lst
    return reverse(lst[1:]) + [lst[0]]


lst = [1, [2, 3], 4]
rev = reverse(lst)


# print(rev)

def combine_skipper(f, lst):
    n = 0
    while n < len(lst) // 4:
        lst[n * 4:n * 4 + 2] = [f(lst[n * 4:n * 4 + 2])] + [n * 4 + 1]
        n += 1
    return lst


lst = [4, 7, 3, 2, 1, 8, 5, 6]
f = lambda l: sum(l)
lst = combine_skipper(f, lst)


# print(lst)


# abstruct data type
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def rational(n, d):
    g = gcd(n, d)
    return [n // g, d // g]


def numer(x):
    return x[0]


def denom(x):
    return x[1]


def mul_rational(x, y):
    return rational(numer(x) * numer(y),
                    denom(x) * denom(y))


def add_rational(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)


def print_rational(x):
    print(str(numer(x)) + '/' + str(denom(x)))


def rationals_are_equal(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)


def rational_pow(x, e):
    return rational(numer(x) ** e, denom(x) ** e)


# print_rational(rational_pow(rational(2, 3), 2))

def inverse_rational(x):
    """Returns the inverse of the given non-zero rational number"""
    return rational(denom(x), numer(x))


# print_rational(inverse_rational(rational_pow(rational(3, 4), 2)))

def div_rationals(x, y):
    return mul_rational(x, inverse_rational(y))


# print_rational(div_rationals(rational(2, 3), rational(3, 2)))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def approx_e(iter):
    r = rational(0, 1)
    for i in range(iter):
        r = add_rational(r, rational(1, factorial(i)))
    return r


# print_rational(approx_e(10))

# TREES
def tree(label, branches=[]):
    for b in branches:
        assert is_tree(b), 'branches must be trees'
    return [label] + list(branches)


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for b in branches(tree):
        if not is_tree(b):
            return False
    return True


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_leaf(tree):
    return not branches(tree)


# def is_min_heap(t):
#     sub_t = [is_min_heap(branch) for branch in branches(t)]
#     # print(sub_t)
#     return all([label(t) < label(branch) for branch in branches(t)]) and all(sub_t)

def is_min_heap(t):
    for branch in branches(t):
        if label(t) > label(branch) or not is_min_heap(branch):
            return False
    return True


t = tree(1, [tree(5, [tree(7)]), tree(3, [tree(9), tree(4)]), tree(6)])

# print(t)
# print(is_min_heap(t))
from functools import reduce


def largest_product_path(tree):
    if not tree:
        return 0
    if is_leaf(tree):
        return label(tree)
    else:
        paths = [largest_product_path(branch) for branch in branches(tree)]
        return max(paths) * label(tree)


# print(largest_product_path(None))
# print(largest_product_path(tree(3)))
# t = tree(3, [tree(7, [tree(2)]), tree(8, [tree(1)]), tree(4)])
# print(t)
# print(largest_product_path(t))

# Chanllenge Question
def level_order(tree):
    if not tree:
        return []
    current_level, next_level = [label(tree)], [tree]
    print(next_level)
    while next_level:
        find_next = []
        for b in next_level:
            find_next.extend(branches(b))
        print(find_next)
        next_level = find_next
        current_level.extend([label(t) for t in next_level])
    return current_level


t = tree(3, [tree(7, [tree(2)]), tree(8, [tree(1)]), tree(4)])
print(t)
print(level_order(t))
