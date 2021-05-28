import sys

# The main application section
print('Hello World!')
print('Arguments Sent:')
for item in sys.argv:
    if "-" in item:
        print("flag value {}".format(item))
    else:
        print("--> {}".format(item.replace("-","")))

# Some playing with numbers
x = 1 + 3 * 5 - 6 / 3 + (9*6)
1 + 15 - 2 + 54
16 - 2 + 54
14 + 54
68
