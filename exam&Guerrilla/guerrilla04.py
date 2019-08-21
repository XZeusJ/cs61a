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


# 9b
class Plant:
    def __init__(self):
        self.materials = []
        self.height = 1
        self.leaf = [Leaf(self)]
        self.age = 0

    def abosrb(self):
        for l in self.leaf:
            l.absorb()
            l.age += 1

        self.age += 1


    def grow(self):
        for sugar in self.materials:
            sugar.activate()
            self.height += 1

        for l in self.leaf:
            l.age += 2
        self.age += 2

    def death(self):


class Leaf:
    def __init__(self, plant):
        self.alive = True
        self.sugars_used = 0
        self.plant = plant


    def absorb(self):
        if self.alive:
            self.plant.materials.append(Sugar(self, self.plant))

    def death(self):

    def __repr__(self):
        return '|Leaf|'
