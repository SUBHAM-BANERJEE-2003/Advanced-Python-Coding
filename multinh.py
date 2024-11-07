class A:
    def m(self):
        print("m of A called")


class B(A):
    def m(self):
        print("m of B called")


class C(A):
    def m(self):
        print("m of C called")


class D(B, C):
    pass


a = A()
b = B()
c = C()
d = D()
print("a.m():", a.m())
print("b.m():", b.m())
print("c.m():", c.m())
print("d.m():", d.m())
