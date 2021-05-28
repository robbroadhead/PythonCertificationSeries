# Some examples of bitwise operators
# bitwise operators: ~ & ^ | << >>

print("Bitwise Operators Examples")
print("An example of ~ (flip bits)")
print("~4")
print("4 in bits 0100 flip to 1011")
print(format(4,'b'))
print(format(~4,'b'))
print("~5")
print("5 in bits 0101 flip to 1010")
print(format(5,'b'))
print(format(~5,'b'))
a = ~5
print(~a)

print("An example of & (bitwise and)")
print("4 in bits 00000100 5 is 00000101 & turns this into 00000100")
print(format(4 & 5,'b'))
print(format(5 & 4,'b'))
print("17 in bits 00010001 15 is 00001111 & turns this into 00011111")
print(format(17 & 15,'b'))
print(17 & 15)

