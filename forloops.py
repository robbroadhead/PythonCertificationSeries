# Additional discussions: immutable (native and tuple, range), sep and end for print
# del lst[0:-2] del lst[-1]   a,b = 3,2    for item in dictionary
print("exponent examples (anything to the zero power is equal to 1), other than that 0 to any power is 0.  0 to a negative is an exception")
print(str(0**0))
print(str(0**1))
print(str(0**2))
#print(str(0**(-74)))
print(str(2**(-74)))
print(str(3**0))
print(str(10**0))
print(str(72349**0))

print("example 1")
print("1","2","3",end="")
print("example 2")
print("1a","2a","3a",end="eol")
print("")

print("1","2","3",sep="")
print("1","2","3",sep="|")

myList = [1,2,3]
print(myList,sep="|")
for x in myList:
    print(x,end="|")

sample = {'home': '123 Main street', 'office': '22 Baker Street', 'bill': '1 Financial Way'}

print(sample)
print(sample.keys())
print(sample.values())
for x in sample:
    print(sample[x])

sample2 = [['home','123 Main street'],['office','22 Baker Street'],['bill','1 Financial Way']]
sample3 = [['home','123 Main street'],['office','22 Baker Street'],['bill','1 Financial Way']]

for x in sample2:
    print(x)

for k, v in sample2:
    print("k is " + k)
    print("v is " + v)

print(sample2)
del sample2[0:-1]
print(sample2)
print(sample3)
del sample3[-2]
print(sample3)


#complex question
for r in range(3):
    print(r)

lst = [[c for c in range(r)] for r in range(3)]
for x in lst:
    for y in x:
        if y < 2:
            print('*', end='')

print("\nEnd Of Application")

print(str((2**3)**4))

exit(0)


# "ABCD" - in memory slots 0-3
# x = "ABCD"  x is a ptr to [0]
# XYZ - in memory slots 5-7
# x = "XYZ"


