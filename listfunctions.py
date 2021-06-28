import sys

# Application for working with lists: append, clear, copy, count, index, remove,
# insert, pop,
# reverse, sort, sorted, extend,

morning_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
day_arr = [11, 12, 13, 14, 15, 16, 17]
eve_arr = [18, 19, 20, 21, 22, 23, 24]
colors = ['red', 'green', 'blue', 'white', 'black']

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

print("\nApplication Ended.\n")