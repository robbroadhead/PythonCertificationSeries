import sys

# Application for working with if, if-else, if-elif
print('Logical Options Example\n')
value = input('Provide the hour of the day (0-24):')

greeting = "Good {}"
day_text = ""
# Note that elif ends series if true
# note we can have multiple elif sections
if int(value) < 10:
    day_text = "Morning"
elif int(value) == 12:
    day_text = "Noon"
elif int(value) < 17:
    day_text = "Day"
else:
    day_text = "Evening"

#print("A" * 5)
print("\n" + greeting.format(day_text) + "\n")

print("\nApplication Ended.\n")