class A():
    def display(dp):
        print("Display Inside class A ")
    def show(self):
        print("Show Inside class A")
class B(A):
    def print(pt):
        print("Print Inside class B")

    def show(self):
        print("Show Inside class ")
class C(B):
    def show(self):
        print("Show Inside class C ")
s = A()
s.display()
k = B()
k.print()
g = C()
g.show()