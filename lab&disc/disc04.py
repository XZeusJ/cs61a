# Trees

# Constructor
def tree(label, branches=[]):
    # for branch in branches:
    #     assert is_tree(branch)
    return [label] + list(branches)


# Selectors
def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


# For convenience
def is_leaf(tree):
    return not branches(tree)


def tree_max_rec1(t):
    """ Return the maximum label in a tree. """
    m = 0

    def helper(t):
        nonlocal m
        if label(t) > m: m = label(t)
        # print("root", label(t))
        for branch in branches(t):
            if is_leaf(branch):
                if label(branch) > m: m = label(branch)
                # print("leaf", label(branch))
            else:
                helper(branch)

    helper(t)
    return m


def tree_max_rec2(t):
    """ Return the maximum label in a tree. """
    # print(label(t))
    if is_leaf(t):
        return label(t)

    max = label(t)
    for branch in branches(t):
        sub_max = tree_max_rec2(branch)
        if max < sub_max: max = sub_max
    return max


def height(t):
    """Return the height of a tree"""
    if is_leaf(t):
        return 0

    h = 0
    for branch in branches(t):
        sub_h = height(branch)
        if h < sub_h: h = sub_h
    return h + 1


def square_tree(t):
    """Return a tree with the square of every element in t"""
    if is_leaf(t):
        return [label(t) ** 2]

    lst = []
    for branch in branches(t):
        lst.append(square_tree(branch))
    return [label(t)] + list(lst)


def find_path(tree, x):
    """
    # t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    # find_path(t, 5)
    [2, 7, 6, 5]
    # find_path(t, 10) # returns None
    """
    if label(tree) == x:
        return [label(tree)]

    for branch in branches(tree):
        path = find_path(branch, x)
        # print(path)
        if path:
            return [label(tree)] + path

def prune(t, k):
    pass

# t = tree(1, [tree(3, [tree(4), tree(5), tree(6)]), tree(2)])
# print(t)
# # print(tree_max_rec1(t))
# print("max label is ", tree_max_rec2(t))
# print("height is ", height(t))
# print("square tree is ", square_tree(t))

t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])]), tree(15)])
print(t)
print("height is ", height(t))
print(find_path(t, 5))
print(find_path(t, 6))
print(find_path(t, 10))  # returns None
print(prune(t,3))
