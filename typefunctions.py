# Examples of type functions type(), isinstance, dir, hasattr, getattr, setattr

class Simple():
    # class properties
    myName = ""
    value = ""
    __id = 0

    # class methods
    def __str__(self):
        return self.myName + "[" + self.value + "]"

    def __init__(self,val1="default",val2="default"):
        print("Constructor called")
        self.myName = val1
        self.value = val2

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

# simple --> lesssimple
# Start examples
simple = Simple()
lsimple = LessSimple()
value = "123"
value2 = 123
value3 = (1,2,3)
value4 = 1.23

print(type(simple))
print(type(lsimple))
print(type(value))
print(type(value2))
print(type(value3))
print(type(value4))

print("isinstance examples")
print(isinstance(simple,Simple))
print(isinstance(lsimple,Simple))
print(isinstance(simple,LessSimple))
print(isinstance(lsimple,LessSimple))

print("isinstance native examples")
print(isinstance(value, str))
print(isinstance(value, int))

print("dir examples")
print(dir(simple))
print(simple.__str__())
print(simple.__class__())
print(simple.__sizeof__())

print("hasattr examples")
print(hasattr(lsimple,"address"))
print(hasattr(lsimple,"myName"))

print(hasattr(lsimple,"myAddress"))
print(hasattr(lsimple,"dump"))
print(lsimple.dump())


print(getattr(lsimple,"dump"))
print(getattr(lsimple,"address"))
setattr(lsimple,"address","New Value")
print(getattr(lsimple,"address"))
setattr(lsimple,"city","New York")
print(getattr(lsimple,"city"))

newfunc = lambda x: x + 1
setattr(lsimple,"addone",newfunc)
print(str(lsimple.addone(1)))
