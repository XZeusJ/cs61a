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


# Return of the Digits
def complete(t, d, k):
    """Return whether t is d-k-complete."""
    if not branches(t):  # we check the relationship about tree deep and height
        return d == 0

    bs = [complete(branch, d - 1, k) for branch in branches(t)]
    print(bs, d)
    return len(branches(t)) == k and all(bs)


# print(complete(tree(1), 0, 5))
u = tree(1, [tree(1), tree(1), tree(1)])
print(u)
# print([complete(u, 1, 3), complete(u, 1, 2), complete(u, 2, 3)])
print(complete(tree(1, [u, u, u]), 2, 3))

# 1.Translating a List Diagram to Code
x, y, z = 1, 2, 3
# x = [2,[1,[2,[3,[]]]],[[]]]
# y = [1,[2,[3,[]]]]
y = [x, [y, [z, []]]]
x = [2, y, [[]]]
z = 0


# print(x)
# print(y)
# print(z)

def closest(t):
    """Return the smallest difference between an entry
    and the sum of the entries of its branches."""
    diff = abs(label(t) - sum([label(branch) for branch in branches(t)]))
    return min([diff] + [closest(branch) for branch in branches(t)])


# t = tree(8, [tree(4), tree(3)])
# print(closest(t))
# print(closest(tree(5, [t])))  # Same minimum as t
# print(closest(tree(10, [tree(2), t])))
# print(closest(tree(3)))
# print(closest((tree(8, [tree(1, [tree(5)])]))))
# print(sum([]))

def find_path(tree, x):
    """
    # t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    # find_path(t, 5)
    [2, 7, 6, 5]
    """
    if label(tree) == x:
        return [label(tree)]

    for branch in branches(tree):
        path = find_path(branch, x)
        # print(path)
        if path:
            return [label(tree)] + path


def is_path(t, path):
    """Return whether a given path exists in a tree, beginning
    at the root."""
    # we check node at each level if equal path[0]
    if label(t) != path[0]:
        return False
    if label(t) == path[0] and len(path) == 1:
        return True

    return any(is_path(branch, path[1:]) for branch in branches(t))

# t = tree(1, [
#     tree(2, [tree(4), tree(5,[tree(8)])]),
#     tree(3, [tree(6), tree(7)])
# ])
# print(t)
# print(is_path(t, [1, 2]))
# print(is_path(t, [1, 2, 5, 8]))
# print(is_path(t, [2, 4]))
