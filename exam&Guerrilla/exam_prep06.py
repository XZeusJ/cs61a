class Tree:
    def __init__(self, entry, branches=[]):
        self.entry = entry
        for branch in branches:
            assert (isinstance(branch, Tree))
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.entry) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str

        return print_tree(self).rstrip()


def leaves(tree):
    "The leaf values in Tree instance"
    if tree.is_leaf():
        return [tree.entry]
    else:
        return sum([leaves(b) for b in tree.branches], [])


# 3. expression trees
def eval_with_add(t):
    if t.entry == '+':
        return sum([eval_with_add(b) for b in t.branches])
    elif t.entry == '*':
        total = 1
        for b in t.branches:
            total, term = 0, total
            for _ in range(eval_with_add(b)):
                total = total + term
        return total
    else:
        return t.entry


plus = Tree('+', [Tree(2), Tree(3)])
times = Tree('*', [Tree(2), Tree(3)])
deep = Tree('*', [Tree(2), plus, times])
# print(plus)
# print(times)
# print(deep)
# print(eval_with_add(plus))
# print(eval_with_add(times))
# print(eval_with_add(deep))
# print(eval_with_add(Tree('*')))

