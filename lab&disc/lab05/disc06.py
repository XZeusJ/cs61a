# We now want to write three different classes, Mailman, Client, and Email to simulate
# email. Fill in the definitions below to finish the implementation! There are more
# methods to fill out on the next page.

class Email:

    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name


class Mailman:
    def __init__(self):
        self.clients = {}

    def send(self, email):
        client = self.clients[email.recipient_name]
        client.receive(email)

    def register_client(self, client, client_name):
        self.clients[client_name] = client


class Client:
    def __init__(self, mailman, name):
        self.inbox = []
        self.mailman = mailman
        self.name = name
        self.mailman.register_client(self, self.name)

    def compose(self, msg, recipient_name):
        self.mailman.send(Email(msg, self.name, recipient_name))

    def receive(self, email):
        self.inbox.append(email)


# Below is a skeleton for the Cat class, which inherits from the Pet class. To complete the implementation, override the init and talk methods and add a new
# lose_life method.


class Pet(object):
    def __init__(self, name, owner):
        self.is_alive = True  # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)


class Dog(Pet):
    def talk(self):
        print(self.name + ' says woof!')


class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self, name, owner)
        self.lives = lives

    def talk(self):
        return self.name + " says meow!"

    def lose_life(self):

        if self.lives > 0:
            self.lives -= 1
            if self.lives == 0:
                self.is_alive = False
        else:
            print("This cat has no more life to lose :(")


class NoisyCat(Cat):
    def talk(self):
        Cat.talk(self)
        Cat.talk(self)


class A:
    def f(self):
        return 2

    def g(self, obj, x):
        if x == 0:
            return A.f(obj)
        return obj.f() + self.g(self, x - 1)


class B(A):
    def f(self):
        return 4


# x, y = A(), B()
# print(x.f())
# print(B.f())

class Foo:
    def __init__(self, bar):
        self.bar = bar

    def g(self, x):
        return self.bar + x
