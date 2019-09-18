class A:
    y = 1
    def __init__(self, y):
        self.y = y
    def f(self, x):
        self.y += x

a = A(0) # Ok or not okay?
a.f(6)   # Ok or not okay?
a.f(A, 9) # Ok or not okay?
A.f(a, 4) # Ok or not okay?
A.f(A, 4) # Ok or not okay?
