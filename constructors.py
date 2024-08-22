from unicodedata import name
class A:
    def __init__(self):
     self.name = "durga"
    def print_A(self):
        print(self.name)
obj = A()
obj.print_A()

class B(A):
    def __init__(self):
     self.name = "KGF"
    def print_B(self):
        print(self.name)
obj1 = B()
obj1.print_B()

class C:
    name = None
    _roll = None
    __branch = None
    def __init__(self,name,roll,branch):
        self.name = name
        self._roll = roll
        self.__branch = branch
    def dsiplayName(self):
        print("Name:",self.name)
    def _displayRoll(self):
        print("Roll:",self._roll)
    def __displayBranch(self):
        print("Branch:",self.__branch)
    def access__displayBranch(self):
        self.__displayBranch()

class D(C):
    def __init__(self,name, roll, branch):
        super().__init__(name,roll, branch)
    def access_displayRoll(self):
        self._displayRoll()
obj = D("durga", 5 , "CSE")
obj.dsiplayName()
obj.access_displayRoll()
obj.access__displayBranch()