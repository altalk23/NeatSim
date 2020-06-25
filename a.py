class A:
    def thing(self, t):
        self.t = t
    def print(self):
        print(self.t)

class B:
    def thing(self, t):
        self.t = t
    def print(self):
        print(self.t)

s = []
a = A()
a.thing(s)
b = B()
b.thing(s)
a.t += ['bbbb']
a.print()
b.print()
