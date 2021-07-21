# Python simple class examples
def display(value):
    print("Different display " + value)


class Simple:
    # class properties
    myName = ""
    value = ""

    # class methods
    def __init__(self,val1="default",val2="default"):
        print("Constructor called")
        self.myName = val1
        self.value = val2

    def display3():
        print("Static Method")

    def display(self):
        print(self.myName)

    def display2(self, value):
        print(self.myName + " and here is the value:" + str(value))
        print(self.value)


class LessSimple:
    # class properties
    myName = "I am Less Simple"
    value = "Less Simple Value"

    # class methods
    def display2(self, value):
        print(self.myName + " and here is the value:" + str(value))
        print(self.value)


Simple.display3()
simple = Simple()
simple.display()
simple.display2("My Value")
simple2 = Simple()
print("\n\n")
simple2.myName = "Second Instance"
simple2.value = "Another value"
simple2.display()
simple2.display2("My Value")
print("\n\n")
simple3 = Simple()
simple3.myName = "I am 3rd"
simple4 = LessSimple()
instances = [simple,simple2,simple3]
for item in instances:
    item.display()

uninit = Simple()
uninit.display()
init = Simple("init name","init value")
init.display()
