# Object Oriented Programming

class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    8
    """

    def __init__(self, value=0):
        self.value = value

    def next(self):
        "*** YOUR CODE HERE ***"
        if self.value == 0:
            result = Fib(1)
        else:
            result = Fib(self.value + self.prev)
        result.prev = self.value
        return result

    def __repr__(self):
        return str(self.value)


start = Fib()
start
start.next()
start.next().next()
start.next().next().next()
start.next().next().next().next()


class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"

    def __init__(self, name, n):
        self.name = name
        self.price = n
        self.stock = 0
        self.deposits = 0

    def restock(self, n):
        self.stock += n
        return 'Current {0} stock: {1}'.format(self.name, self.stock)

    def deposit(self, n):
        if self.stock == 0:
            return 'Machine is out of stock. Here is your ${0}.'.format(n)
        else:
            self.deposits += n
            return 'Current balance: ${0}'.format(self.deposits)

    def vend(self):
        if self.stock == 0:
            return 'Machine is out of stock.'
        if self.deposits > self.price:
            change = self.deposits - self.price
            self.deposits = 0
            self.stock -= 1
            return 'Here is your {0} and ${1} change.'.format(self.name, change)
        elif self.deposits == self.price:
            self.deposits = 0
            self.stock -= 1
            return 'Here is your {0}.'.format(self.name)
        else:
            return 'You must deposit ${0} more.'.format(self.price - self.deposits)
