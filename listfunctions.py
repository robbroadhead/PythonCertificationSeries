import sys

# Application for working with lists: append, clear, copy, count, index, remove,
# insert, pop,
# reverse, sort, sorted, extend, find(), rfind(), in not in, len

morning_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
day_arr = [11, 12, 13, 14, 15, 16, 17]
eve_arr = [18, 19, 20, 21, 22, 23, 24]
colors = ['red', 'green', 'blue', 'white', 'black']
example = ['red', 'green', 'blue', 'red', 'green', 'blue', 'white', 'black']

# append
print("List")
print(colors)
print("List-append()")
colors.append("yellow")
print(colors)
colors.append(["purple", "pink"])
print(colors)
print("List-copy()")
colors2 = colors.copy()
print(colors2)
print("List-clear()")
colors2.clear()
print(colors2)
print(colors)
print("List-count()")
print(colors.count('red'))
print(colors.count('r'))
print(colors2.count('red'))
print(day_arr.count('1'))
print("List-index()")
print(colors.index('blue'))
print("List-remove()")
colors.remove('blue')
print(colors)
print(colors.index('white'))
print("List-insert()")
colors.insert(2, 'blue')
print(colors)
print("List-pop()")
print(colors.pop())
print(colors)
print(colors.pop())
print(colors)

# reverse, sort, sorted, extend, , in not in, len, find(), rfind()
example = ['red', 'green', 'blue', 'red', 'green', 'blue', 'white', 'black']
example2 = example
print("==================================================")
print("Example List for Below:")
print(example)
print("List-sort()")
def length(e):
  return len(e)

example.sort()
print(example)

print("List-reverse()")
example.reverse()
print(example)

example = example2
example.sort(key=length)
print(example)

print("sorted(list)")
example = ['red', 'green', 'blue', 'red', 'green', 'blue', 'white', 'black']
print(sorted(example))
print(example)

print("List-extend()")
colors = ['red', 'green', 'blue', 'white', 'black']
colors.append(["purple", "pink"])
print(colors)
colors = ['red', 'green', 'blue', 'white', 'black']
colors.extend(["purple", "pink"])
print(colors)

colors = ['red', 'green', 'blue', 'white', 'black']
example = ['red', 'green', 'blue', 'red', 'green', 'blue', 'white', 'black']
print(len(colors))
print(len(example))
if 'red' in colors:
    print("Its in there")
if 'purple' not in colors:
    print("Its not in there")

print("\nApplication Ended.\n")