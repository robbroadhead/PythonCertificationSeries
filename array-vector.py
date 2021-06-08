import sys

# Application for working with if, if-else, if-elif
print('Array-Vector Example (part 1 array, part 2 vector)\n')
value = input('Provide the hour of the day (0-24):')

morning_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
day_arr = [11, 12, 13, 14, 15, 16, 17]
eve_arr = [18, 19, 20, 21, 22, 23, 24]
all_arr = morning_arr + day_arr + eve_arr
print(all_arr)
print("Here is an array example")
print(morning_arr[4])
print(morning_arr[4:])
print(morning_arr[:4])
print(morning_arr[0:4])
greeting = "Good {}"
day_text = ""
# Note that elif ends series if true
# note we can have multiple elif sections
if int(value) in all_arr[:10]:
    day_text = "Morning"
elif int(value) == all_arr[11]:
    day_text = "Noon"
elif int(value) in all_arr[16:20]:
    day_text = "Evening"
elif int(value) in all_arr[21:]:
    day_text = "Night"
else:
    day_text = "Day"

print("\n" + greeting.format(day_text) + "\n")

print("\nApplication Ended.\n")