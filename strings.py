# strings in detail: ASCII, UNICODE, UTF-8, immutability,
# escaping using the \ character, quotes and apostrophes inside strings, multiline strings,
# copying vs. cloning, advanced slicing, string vs. string, string vs. non-string,
# basic string methods (upper(), lower(), isxxx(), capitalize(), split(), join(), etc.)
# and functions (len(), chr(), ord()), escape characters
x = "This is a simple string output\n"
x2 = "This is a simple string output"
y = "1234ABC"
x3 = "bob jones"
z = "ABCdef"
a = ""

myString = "today is hot|clear|windy"
print(x)
print("upper()")
print(x.upper())
print("lower()")
print(x.lower())
print("islower()")
print(x.lower().islower())
print("isdigit()")
print(x.isdigit())
print(y.isdigit())
print("isalpha()")
print(x.isalpha())
print(y.isalpha())
print(z.isalpha())
print(a.isalpha())
print("isalnum()")
print(x.isalnum())
print(y.isalnum())
print(a.isalnum())
print("isprintable()")
print(x.isprintable())
print(x2.isprintable())
print("capitalize()")
print(x.capitalize())
print(x3.capitalize())

print("split()")
result = myString.split("|")
print(myString)
print(result)
print(result[2])
print(result[0].split(" "))
m = "OOO"
n = "XXX"
q = "OP"
r = "XXXX"
print (m.join(n))
print(r)
print(q)
print("q.join(r)")
print(q.join(r))
print("r.join(q)")
print (r.join(q))

myString = "lazy dog jumps over log"
print("find()")
print(myString.find("o"))
print("rfind()")
print(myString.rfind("o"))



