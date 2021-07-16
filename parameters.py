# Examples of parameter defaults, named, arbitrary, and recursion

def add(a,b):
    return a + b

def add2(a,b=2):
    return a + b

print(str(add(4,3)))

def address(zip="12345",city="Somewhere",state="IL"):
    retVal = "You are at {}, {}  {}".format(city,state,zip)
    return retVal

print("Empty values example")
print(address(state="OH"))

def Hello(name,time="a generic time of the day"):
    print("Hello {} it is {}".format(name,time))

Hello("Bob","morning")
Hello("Bob")

print(str(add2(3)))

def location(zip,city="Not Entered",state="Not Entered"):
    retVal = "You are at {}, {}  {}".format(city,state,zip)
    return retVal

print(location("12345"))
print(location("12345","Nowhere"))
print(location("12345",state="OH"))

def sum(*values):
    result = 0
    print(values)
    for item in values:
        result = result + item
    return result

def sum2(*values):
    result = 0
    print(values)
    for item in values:
        result = result + item
        yield result

print(str(sum(1,2,3,4,5)))
result = sum2(1,2,3,4,5)
for x in result:
    print(x)

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

print(str(factorial(5)))

def a():
    b()

def b():
    a()

