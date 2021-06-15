import sys
# import variants; advanced qualifying for nested modules
# dir(); sys.path variable
# math: ceil(), floor(), trunc(), factorial(), hypot(), sqrt();
# random: random(), seed(), choice(), sample()
# platform: platform(), machine(), processor(), system(), version(), python_implementation(), python_version_tuple()
# idea, __pycache__, __name__, public variables, __init__.py
# searching for modules/packages; nested packages vs directory tree


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
