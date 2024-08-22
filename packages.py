class ClassOne:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello from ClassOne, {self.name}!"
class ClassTwo:
    def __init__(self, number):
        self.number = number

    def display(self):
        return f"The number in ClassTwo is {self.number}."
from .class_one import ClassOne
from .class_two import ClassTwo
from mypackage import ClassOne, ClassTwo
obj1 = ClassOne(name="Alice")
print(obj1.greet())
obj2 = ClassTwo(number=42)
print(obj2.display())
mypackage/
    __init__.py
    class_one.py
    class_two.py
main.py
