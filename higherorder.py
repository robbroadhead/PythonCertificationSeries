# Examples of map(), filter(), reduce(), reversed(), sorted() functions
from functools import reduce

def notBlank(x: str) -> bool:
    result = (len(x) > 0)
    return result


def addone(x: int) -> int:
    return x + 1


def addval(x: int, y: int) -> int:
    print("Called with: " + str(x) + " and " + str(y))
    return x + y


values = (2, 6, 4, 10, 8)

print("Example of Map")
results = map(addone, values)
print(results)
print(list(results))

values2 = ("2", "4", "", "6", "" , "8", "10")

print("Example of filter")
print("Example of not blank")
print(notBlank("qwerty"))
print("Example of is blank")
print(notBlank(""))
results = filter(notBlank, values2)
print(results)
print(list(results))
print("Example of sorted")
results = sorted(values)
print(results)
print(list(results))
results = sorted(values, reverse=True)
print(results)
print("Example of reversed")
results = reversed(values)
print(results)
print(list(results))


print("Example of Reduce")
results = reduce(addval, values)
print(results)
