# 1
class Worker:
    greeting = 'Sir'

    def __init__(self):
        self.elf = Worker

    def work(self):
        return self.greeting + ', I work'

    def __repr__(self):
        return Bourgeoisie.greeting


class Bourgeoisie(Worker):
    greeting = 'Peon'

    def work(self):
        print(Worker.work(self))
        return 'My job is to gather wealth'


class Proletariat(Worker):
    greeting = 'Comrade'

    def work(self, other):
        other.greeting = self.greeting + ' ' + other.greeting
        other.work()  # for revolution
        return other


jack = Worker()
john = Bourgeoisie()
jack.greeting = 'Maam'

Worker().work()
jack
jack.work()
john.work()[10:]
Proletariat().work(john)
john.elf.work(john)


# 4 Tree Time
class GrootTree(BinaryTree):
    """A binary tree with a parent"""

    def __init__(self, entry, left=BinaryTree.empty, right=BinaryTree.empty):
        BinaryTree.__init__(self, entry, left, right)
        self.parent = BinaryTree.empty
        for b in [left, right]:
            if b is not BinaryTree.empty:
                b.parent = self


def fib_groot(n):
    """Return a Fibonacci GrootTree"""
    if n == 0 or n == 1:
        return GrootTree(n)
    else:
        left, right = fib_groot(n - 2), fib_groot(n - 1)
        return GrootTree(left.entry + right.entry, left, right)


def paths(g, s):
    """The number of paths through g with entries s."""
    if g is BinaryTree.empty or s == [] or g.entry != s[0]:
        return 0
    elif len(s) == 1 and g.entry == s[0]:
        return 1
    else:
        extensions = [g.left, g.right, g.parent]
        return sum(paths(x, s[1:]) for x in extensions)


# linked list manipulation
def double_up(s):
    """Mutate s by inserting elements so that each element is next to an equal."""
    if s is Link.empty:
        return 0
    elif s.rest is Link.empty:
        s.rest = Link(s.first)
        return 1
    elif s.first == s.rest.first:
        return double_up(s.rest.rest)
    else:
        s.rest = Link(s.first, s.rest)
        return 1 + double_up(s.rest.rest)
