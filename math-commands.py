import sys
import math
import random

# math: ceil(), floor(), trunc(), factorial(), hypot(), sqrt();
# random: random(), seed(), choice(), sample()

# The main application section
print('Math Commands')
print('ceil(), floor(), trunc(), factorial(), hypot(), sqrt()')
a = 2.4
b = 3.7
print("ceil(2.4):" + str(math.ceil(a)))
print("ceil(3.7):" + str(math.ceil(b)))
print("ceil(2):" + str(math.ceil(2.000001)))
print("ceil(3):" + str(math.ceil(3)))

print("floor(2.4):" + str(math.floor(a)))
print("floor(3.7):" + str(math.floor(b)))
print("floor(2):" + str(math.floor(2.000001)))
print("floor(3):" + str(math.floor(3)))

print("trunc(2.4):" + str(math.trunc(a)))
print("trunc(3.7):" + str(math.trunc(b)))
print("trunc(2):" + str(math.trunc(2.000001)))
print("trunc(3):" + str(math.trunc(3)))

print("factorial(3):" + str(math.factorial(3)))
print("factorial(4):" + str(math.factorial(4)))
print("factorial(5):" + str(math.factorial(5)))

print("hypot(2.4):" + str(math.hypot(2.4)))
print("hypot(3.7):" + str(math.hypot(3.7)))
print("hypot(-2.4):" + str(math.hypot(-2.4)))
print("hypot(-3.7):" + str(math.hypot(-3.7)))
print("hypot(3):" + str(math.hypot(3)))

print("sqrt(100):" + str(math.sqrt(100)))
print("sqrt(1024):" + str(math.sqrt(1024)))

# random.seed(1234) - forces the same random values or choices
print("random():" + str(math.ceil(100 * random.random())))
print("random():" + str(math.ceil(100 * random.random())))
print("random():" + str(math.ceil(100 * random.random())))
print("random():" + str(math.ceil(100 * random.random())))
print("random():" + str(math.ceil(100 * random.random())))

morning_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
colors = ['red', 'green', 'blue', 'white', 'black']
print(random.choice(morning_arr))
print(random.choice(morning_arr))
print(random.choice(morning_arr))

print(random.choice(colors))
print(random.choice(colors))
print(random.choice(colors))

print(random.sample(morning_arr, 3))
print(random.sample(morning_arr, 4))
print(random.sample(morning_arr, 1))
print(random.sample(morning_arr, 2))

print(random.sample(colors, 2))
