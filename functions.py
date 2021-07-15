# Examples of functions, return and yield

def myFunc():
    print("This is a call to MyFunc()\n")

def myFunc2(value):
    print("This is a call to MyFunc() with value:" + value + "\n")

def myFunc3(value,value2):
    print("This is a call to MyFunc() with value:" + value + "\n")
    print("and value2:" + str(value2) + "\n")

def myFunc4(value,value2):
    print("This is a call to MyFunc() with value:" + value)
    for x in value2:
        print(x)

def add(a,b):
    return a + b

def address():
    returnValue = ['22 Baker Street','Somewhere','OH']
    return returnValue

def add2(a,b):
    yield a + b
    yield a * b
    yield a - b
    yield a / b

print("Walker example")
myArr = ['a','b','c']
def myPrint(value):
    return "Value:" + value

def walker(arr):
    for x in arr:
        yield myPrint(x)

for item in walker(myArr):
    print(item)
print("End of Walker example")

# call the function
myFunc()

myFunc2("My Value")

myFunc3("My Other Value", 2)

myFunc4("My 4th Value", ['a','b','c'])

print("Sum is:" + str(add(1, 2)))

print(address())

print("Sum is:" + str(add(1, 2)))
print("Sum is:" + str(add2(1, 2)))
for item in add2(1, 2):
    print(item)
