import sys

# Application for working with while, for and range
print('While-For Examples\n')
value = input('Provide the hour of the day (0-24):')

morning_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
day_arr = [11, 12, 13, 14, 15, 16, 17]
eve_arr = [18, 19, 20, 21, 22, 23, 24]
all_arr = morning_arr + day_arr + eve_arr
greeting = "{} o'clock and All is Well"
day_text = ""
count = 0

while count < int(value):
    count = count + 1
    print(greeting.format(str(count)))
else:
    print("End of Loop")

# infinite loop
while True:
    print(".")
    break
else:
    print("End of Infinite Loop")

count = 0
while count < int(value):
    count = count + 1
    print(count)
    if count < 5:
        continue
    print(" is a big number")
else:
    print("End of Infinite Loop")

colors = ['red', 'green', 'blue', 'white', 'black']
for x in colors:
    print(x)
else:
    print("End of for loop")

for x in range(5):
    print(str(x) + " is in the range")

print("\nApplication Ended.\n")