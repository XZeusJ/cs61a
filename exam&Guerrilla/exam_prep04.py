# 2
def f(it):
    it.append(it[1]())


def b(it):
    def steps():
        nonlocal it
        it = fit[0]
        return fit.pop()

    return steps


fit = [1, [2]]
bit = [fit, b(fit[1])]
f(bit)


# print(fit)
# print(bit)

# fall 2015, midterm 2, #3b
def adder(x, y):
    """Adds y into x for lists of digits x and y representing positive numbers"""
    carry, i = 0, len(x) - 1
    for d in reversed([0] + y):
        if i == -1:
            x.insert(0, 0)
            i = 0
        d = carry + x[i] + d
        carry = d // 10
        x[i] = d % 10
        i -= 1
    if x[0] == 0:
        x.remove(0)
    return x


# a = [3, 4, 5]
# print(adder(a, [5, 5]))
# print(a)
# print(adder(a, [8, 3, 4]))
# print(adder(a, [3, 3, 3, 3, 3]))


# sprint 2018, exam-prep 4, #1
# 1. lots of lists
a = [1, 2, 3, 4, 5]
a.pop(3)  # a -> [1,2,3,5]
b = a[:]  # b -> [1,2,3,5]
a[1] = b  # a -> [1,[1,2,3,5],3,5]
b[0] = a[:]  # b -> [[1,[...],3,5],2,3,5]
# a -> [1,[...],3,5]
b.pop()  # b-> [[1,[1,2,3,5],3,5],2,3]
b.remove(2)  # b-> [[1,[1,2,3,5],3,5],3]
c = [].append(b[1])  # c-> [3] wrong  /  c-> ??
a.insert(b.pop(1), a[-3:4:3])  # a -> [1,[[1,[1,2,3,5],3,5],3],3,[??],5]
# b -> [[1,[1,2,4,5],4,5]]
b.extend(b)  # b -> [[1,[1,2,3,5],3,5],[1,[1,2,3,5],3,5]]
if b == b[:] and b[1][1][0] is b[0][1][1]:
    a, b, c = [c] + a[-4:4:2]

# fall 2015, midterm 2, #3e
import math


def bits(nums):
    """A set of nums represented as a function that takes 'entry', 0, or 1"""

    def branch(last):
        if last == 'entry':
            return 0 in nums
        # translate number into reversed binary form
        return bits([k // 2 for k in nums if k % 2 == last])

    return branch


def int_set(contents):
    index = bits(contents)

    def contains(n):
        t = index
        while n:
            last, n = n % 2, n // 2
            t = t(last)
        return t('entry')

    return contains


# t = bits([4, 5])
# print(t(0)(0)(1)('entry'))
# print(t(0)(1)('entry'))
# print(t(1)(0)(1)('entry'))
#
# print(int_set([1, 2])(1))
# print(int_set([1, 2])(3))
# s = int_set([1, 3, 4, 7, 9])
# print([s(k) for k in range(10)])

# summer 2015, midterm 2, #5a
def naturals():
    i = 1
    while True:
        yield i
        i += 1


def filter_next(iterable, fn):
    items = iter(iterable)
    lst = []
    while True:
        try:
            i = next(items)
            if fn(i):
                # print(i)
                lst.append(i)
        except StopIteration:
            break
    return lst


def filter(iterable, fn):
    for x in iterable:
        if fn(x):
            yield x


# is_even = lambda x: x % 2 == 0
# print(list(filter(range(5), is_even)))
# all_odd = (2 * y - 1 for y in range(5))
# print(list(filter(all_odd, is_even)))
# s = filter(naturals(), is_even)
# print(next(s))
# print(next(s))

# sprint 2018, exam prep 4, #4
def ensure_consistency(fn):
    n = 0
    z = {}

    def helper(x):
        nonlocal n
        nonlocal z
        n += 1
        if n >= 20:
            return None
        val = fn(x)
        if x not in z:
            z[x] = [val]
        if val in z[x]:
            return val
        else:
            z[x].append(val)
            return None

    return helper


def consistent(x):
    return x


lst = [1, 2, 3]


def inconsistent(x):
    return x + lst.pop()


a = ensure_consistency(consistent)
print(a(5))
print(a(5))
print(a(6))
print(a(6))
b = ensure_consistency(inconsistent)
print(b(5))
print(b(5))
print(b(6))