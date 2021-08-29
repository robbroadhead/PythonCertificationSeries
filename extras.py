import sys

# extra topics
# function params
# __doc__
# The function’s documentation string, or None if unavailable; not inherited by subclasses.
#
# Writable
# __name__
# The function’s name.
#
# Writable
# __qualname__
#
# The function’s qualified name.
#
# New in version 3.3.
#
# Writable
#
# __module__
#
# The name of the module the function was defined in, or None if unavailable.
#
# Writable
#
# __defaults__
#
# A tuple containing default argument values for those arguments that have defaults, or None if no arguments have a default value.
#
# Writable
#
# __code__
#
# The code object representing the compiled function body.
#
# Writable
#
# __globals__
#
# A reference to the dictionary that holds the function’s global variables — the global namespace of the module in which the function was defined.
#
# Read-only
#
# __dict__
#
# The namespace supporting arbitrary function attributes.
#
# Writable
#
# __closure__
#
# None or a tuple of cells that contain bindings for the function’s free variables. See below for information on the cell_contents attribute.
#
# Read-only
#
# __annotations__
#
# A dict containing annotations of parameters. The keys of the dict are the parameter names, and 'return' for the return annotation, if provided.
#
# Writable
#
# __kwdefaults__
# Special attributes: __name__ is the class name; __module__ is the module name in which the class was defined; __dict__ is the dictionary containing the class’s namespace; __bases__ is a tuple containing the base classes, in the order of their occurrence in the base class list; __doc__ is the class’s documentation string,

def myFunc(a=0,b=0):
    """A simple function that prints a + b and returns it"""
    name = "This Function"
    print(a + b)
    return a + b

myFunc(2,3)

print(myFunc.__str__())
print(myFunc.__doc__)
print(myFunc.__code__)
print(myFunc.__defaults__)
print(myFunc.__name__)
print(myFunc.__qualname__)
print(myFunc.__globals__)
print(__file__)
myFunc.__custom__ = "Custom Value"
print(myFunc.__dict__)
print(myFunc.__closure__)

print(myFunc.__kwdefaults__)


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


class EvenLessSimple(LessSimple,Simple):
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



print(EvenLessSimple.__bases__)
print(LessSimple.__bases__)
print(Simple.__bases__)

x = 0/1