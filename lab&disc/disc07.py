# Linked List Class
class Link:
    """A linked list.

    s = Link(1)
    s.first
    1
    s.rest is Link.empty
    True
    s = Link(2, Link(3, Link(4)))
    s.second
    3
    s.first = 5
    s.second = 6
    s.rest.rest = Link.empty
    s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    s.rest = Link(7, Link(Link(8, Link(9))))
    s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    @property
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


# Tree Class
class Tree:
    """
    t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    t.label
    3
    t.branches[0].label
    2
    t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        t1 = Tree(1)
        t1.map(lambda x: x + 2)
        t1.map(lambda x : x * 4)
        t1.label
        12
        t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        t2.map(lambda x: x * x)
        t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        t1 = Tree(1)
        1 in t1
        True
        8 in t1
        False
        t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        6 in t2
        False
        5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str

        return print_tree(self).rstrip()


# 2.1
def multiply_lnks(lst_of_lnks):
    product = 1
    for lnk in lst_of_lnks:
        if lnk is Link.empty:
            return Link.empty
        product *= lnk.first
    lst_of_lnks_rests = [lnk.rest for lnk in lst_of_lnks]
    return Link(product, multiply_lnks(lst_of_lnks_rests))


a = Link(2, Link(3, Link(5)))
b = Link(6, Link(4, Link(2)))
c = Link(4, Link(1, Link(0, Link(2))))
p = multiply_lnks([a, b, c])
print(p.first)


# 2.2
def remove_duplicates(lnk):
    while lnk is not Link.empty and lnk.rest is not Link.empty:
        if lnk.first == lnk.rest.first:
            lnk.rest = lnk.rest.rest
        else:
            lnk = lnk.rest


lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
remove_duplicates(lnk)
print(lnk)


# 3.1
def even_weighted(lst):
    return [i * lst[i] for i in range(0, len(lst), 2)]


x = [1, 2, 3, 4, 5, 6]
print(even_weighted(x))


# 3.2
def quicksort_list(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    less = [n for n in lst[1:] if n < pivot]
    greater = [n for n in lst[1:] if n > pivot]
    return quicksort_list(less) + [pivot] + quicksort_list(greater)


def max_product(lst):
    if lst == []:
        return 1
    return max(max_product(lst[1:]), lst[0] * max_product(lst[2:]))


print(max_product([10, 3, 1, 9, 2]))  # 10 * 9

print(max_product([5, 10, 5, 10, 5]))  # 5 * 5 * 5

print(max_product([]))

def redundant_map(t, f):
    t.label = f(t.label)
    new_f = lambda x: f(f(x))
    for b in t.branches:
        redundant_map(b, new_f)