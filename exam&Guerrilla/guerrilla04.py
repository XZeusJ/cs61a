class Foo():
    x = 'bam'

    def __init__(self, x):
        self.x = x

    def baz(self):
        return self.x


class Bar(Foo):
    x = 'boom'

    def __init__(self, x):
        Foo.__init__(self, 'er' + x)

    def baz(self):
        return Bar.x + Foo.baz(self)


foo = Foo('boo')
Foo.x
foo.x
foo.baz()
# Foo.baz()
Foo.baz(foo)

bar = Bar('ang')
Bar.x
bar.x
bar.baz()


# q2: attend class
class Student:
    def __init__(self, subjects):
        self.current_units = 16
        self.subjects_to_take = subjects
        self.subjects_learned = {}
        self.partner = None

    def learn(self, subject, units):
        print("I just learned about " + subject)
        self.subjects_learned[subject] = units
        self.current_units -= units

    def make_friends(self):
        if len(self.subjects_to_take) > 3:
            print("Whoa! I need more help!")
            self.partner = Student(self.subjects_to_take[1:])
        else:
            print("I'm on my own now!")
            self.partner = None

    def take_course(self):
        course = self.subjects_to_take.pop()
        self.learn(course, 4)
        if self.partner:
            print("I need to switch this up!")
            self.partner = self.partner.partner
            if not self.partner:
                print("I have failed to make a friend :(")


tim = Student(["Chem1A", "Bio1B", "CS61A", "CS70", "CogScil"])
# tim.make_friends()
#
# print(tim.subjects_to_take)
# tim.partner.make_friends()
# tim.take_course()
# tim.partner.take_course()
# tim.take_course()
# tim.make_friends()

# Q3 nonlocol

ore = "settlers"


def sheep(wood):
    def ore(wheat):
        nonlocal ore
        ore = wheat

    ore(wood)
    return ore


sheep(lambda wood: ore)("wheat")


# Q4
def make_max_finder():
    list = []

    def max_finder(l):
        nonlocal list
        list += l
        return max(list)

    return max_finder


m = make_max_finder()
m([5, 6, 7])
m([1, 2, 3])
m([9])


# Q8
class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def is_leaf(self):
        return len(self.branches) == 0


def filter_tree(t, fn):
    # if calling fn on its label return False, then remove all branches of that node
    if not fn(t.label):
        t.branches = []
    else:
        for b in t.branches:
            if not fn(b.label):
                t.branches.remove(b)
            else:
                filter_tree(t, fn)


def nth_level_tree_map(fn, tree, n):
    def helper(tree, level):
        if level % n == 0:
            tree.label = fn(tree.label)
        for b in tree.branches:
            helper(b, level + 1)

    helper(tree, 0)


tree = Tree(1, [Tree(7, [Tree(3), Tree(4), Tree(5)]), Tree(2, [Tree(6), Tree(4)])])
nth_level_tree_map(lambda x: x + 1, tree, 2)
tree


class Plant:
    def __init__(self):
        self.leaf = Leaf(self)
        self.materials = []
        self.height = 1

    def absorb(self):
        self.leaf.absorb()

    def grow(self):
        for sugar in self.materials:
            sugar.activate()
            self.height += 1


class Leaf:

    def __init__(self, plant):
        self.alive = True
        self.plant = plant
        self.sugars_used = 0

    def absorb(self):
        if self.alive:
            self.plant.materials.append(Sugar(self, self.plant))
            Sugar.sugars_created += 1


class Sugar:
    sugars_created = 0

    def __init__(self, leaf, plant):
        self.leaf = leaf
        self.plant = plant

    def activate(self):
        self.plant.remove(self)

    def __repr__(self):
        return '|Sugar|'


p = Plant()
p.height
p.materials
p.absorb()
p.materials
Sugar.sugars_created
p.leaf.sugars_used
p.grow()
p.materials
p.height
p.leaf.sugars_used


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


# Q1:
def has_cycle(link):
    first = link
    while link != Link.empty:
        link = link.rest
        if link == first:
            return True
    return False


def seq_in_link(link, sub_link):
    if sub_link is Link.empty:
        return True
    if link is Link.empty:
        return False
    if link.first == sub_link.first:
        return seq_in_link(link.rest, sub_link.rest)
    else:
        return seq_in_link(link.rest, sub_link)


def g(n):
    while n > 0:
        if n % 2 == 0:
            yield n
        else:
            print('odd')
        n -= 1


t = g(4)
t
next(t)
# n
t = g(next(t) + 5)
next(t)


def gen_inf(lst):
    i = 0
    while True:
        yield lst[i % len(lst)]
        i += 1


def nested_gen(lst):
    for elem in lst:
        try:
            iter(elem)
            yield from nested_gen(elem)
        except TypeError:
            yield elem


def mutated_gen(lst):
    original = list(lst)

    def generator_maker(original, lst):
        curr = 0
        while curr < len(original):
            if len(original) != len(lst):
                break
            else:
                if original[curr] != lst[curr]:
                    yield lst[curr]
                curr += 1

    return generator_maker(original, lst)
