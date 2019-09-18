# 1.1
# lst1 = [1, 2, 3]
# lst2 = lst1
#
# print(lst1 is lst2)
#
#
# def show():
#     print(lst1)
#     print(lst2)
#
#
# lst2.extend([5, 6])
# print(lst1[4])
# show();
#
# lst1.append([-1, 0, 1])
# print(-1 in lst2)
# show();
#
# print(lst2[5])
#
# lst3 = lst2[:]
# lst3.insert(3, lst2.pop(3))
# print(len(lst1))

# 1.2
def add_this_many(x, el, lst):
    count = 0
    for i in range(len(lst)):
        if x == lst[i]:
            count += 1
    for i in range(count):
        lst.append(el)


lst = [1, 2, 4, 2, 1]
add_this_many(1, 5, lst)


# print(lst)


# 2.2
def bathtub(n):
    def ducky_annihilator(rate):
        def ducky():
            nonlocal n
            n = n - rate
            return str(n) + " rubber duckies left"

        return ducky

    return ducky_annihilator


# annihilator = bathtub(500)  # the force awakens...
# kylo_ren = annihilator(10)
# print(kylo_ren())
# rey = annihilator(-20)
# print(rey())
#
# print(kylo_ren())

# 3.1
# lst=[6,1,"a"]
# lst_iter = iter(lst)
# print(next(lst_iter))
# print(next(lst_iter))
# print(next(iter(lst)))
# print([x for x in lst_iter])

square = lambda x: x * x


def many_squares(s):
    yield from map(square, s)


# print(list(many_squares([1, 2, 3])))

# 3.2
def weird_gen(x):
    if x % 2 == 0:
        yield x * 2
    else:
        yield x
        yield from weird_gen(x - 1)


# print(next(weird_gen(2)))
# print(list(weird_gen(3)))

def greeter(x):
    while x % 2 != 0:
        print('hello!')
        yield x
        print('goodbye!')


# print(greeter(5))
#
# gen = greeter(5)
# print(next(gen))
# print(next(gen))


# 3.3
def gen_all_items(lst):
    for gen in lst:
        yield from gen


nums = [[1, 2], [3, 4], [[5, 6]]]
num_iters = [iter(l) for l in nums]
print(num_iters)
print(list(gen_all_items(num_iters)))
