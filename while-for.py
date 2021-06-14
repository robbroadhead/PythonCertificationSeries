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
    print(greeting.format(count) + "\n")
else:
    print("\nLoop Complete.\n")

# infinite loop
count = 1
flag = True
while flag:
    count = count + 1
    if count < 10:
        print(count)
        continue

    print("Check if complete")
    if count > 15:
        flag = False
else:
    print("Count:" + str(count))

# Example of break note break skips an else
while True:
    count = count + 1
    if count > 100:
        break

for x in day_arr:
    print(str(x) + " is in mid-day array")

sum = 0
for x in range(0):
    sum = sum + x
else:
    print(str(sum))

for x in range(1,5):
    print(str(x) + " is in the range")


print("\nApplication Ended.\n")