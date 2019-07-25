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


def tree_max(t):
    """ Return the maximum label in a tree. """
    m = 0

    def helper(t):
        nonlocal m
        if label(t) > m: m = label(t)
        print("root", label(t))
        for branch in branches(t):
            if is_leaf(branch):
                if label(branch) > m: m = label(branch)
                print("leaf", label(branch))
            else:
                helper(branch)

    helper(t)
    return m


t = tree(1, [tree(3, [tree(4), tree(5), tree(6)]), tree(2)])
# print(t)
# print(branches(t))
print(tree_max(t))
