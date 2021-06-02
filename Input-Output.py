# Some examples of input and output and formatting
# print() end, sep
# input()
# str(), int(), float()
x = "This is a simple string output"
print(x)
print(repr(x))

y = input("Enter a value: ")
z = input("Enter another value: ")
print("You entered {1} and {0}".format(y,z))

a = {1, 2, 3, 4}
print(1, 2, 3, 4, "red", "car", 3.4, sep='|', end="[eol]")
#print(1, 2, 3, 4, sep='#', end='&')
print("\n\n\n")
a = "1"
b = "2.5"
c = 2.5
print(int(a) + 1)
print(str(float(b)) + str(float(a)))

greeting = "Hello {0}! I hope you realize it is {1} out"
name = "Bob"
weather = "Sunny"
print(greeting.format(name,weather))
