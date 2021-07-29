# Python multiple inheritance examples

class Base1:
    # class properties
    value = "I am base 1"

    # class methods
    def __init__(self,val1="I am base 1"):
        print("Base 1 Constructor called")
        self.value = val1

    def display(self):
        print("Base 1 display called")


class Base2:
    # class properties
    value = "I am base 2"

    # class methods
    def __init__(self,val2="I am base 2"):
        print("Base 2 Constructor called")
        self.value = val2

    def display2(self):
        print("Base 2 display2 called")

    def display(self):
        print("Base 3 display called")


class Base3:
    # class properties
    value = "I am base 3"

    # class methods
    def __init__(self,val1="I am base 3"):
        print("Base 3 Constructor called")
        self.value = val1

    def display3(self):
        print("Base 3 display3 called")

    def display(self):
        print("Base 3 display called")


class MyClass(Base3, Base2, Base1):
    name = ""

    def newFunction(self):
        print("newFunction Called")

    def display(self):
        print("MyClass display called")


myclass = MyClass("test")
myclass.display()
