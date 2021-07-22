# Python class inherit examples
from random import random

class Simple():
    # class properties
    myName = ""
    value = ""
    __id = 0

    # class methods
    def __init__(self,val1="default",val2="default"):
        print("Constructor called")
        self.myName = val1
        self.value = val2
        self.__id = int(100 * random())

    def display(self):
        print("Base Display")
        print(self.myName)

    def dump(self):
        return "[" + str(self.__id) + "]" + self.myName + "==>" + str(self.value)


class LessSimple(Simple):
    # class properties
    address = "Not Entered"

    def display(self):
        super().display()
        print("Child Display")
        print(self.address)

    def dump(self):
        return super().dump() + " at " + self.address

    def myAddress(self):
        print(str(self.address))



simple = Simple()
simple.display()
print(simple.dump())
print("\n\n")
lsimple = LessSimple()
lsimple.myName = "ls name"
lsimple.value = "ls value"
lsimple.address = "ls address"
print(lsimple.dump())
lsimple.display()
simple.myAddress()
