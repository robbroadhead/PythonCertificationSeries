import sys

# Application for working with dictionaries
# dictionaries: building, indexing, adding and removing keys, iterating through dictionaries
# as well as their keys and values, checking key existence, keys(), items() and values() methods

sample = {'home': '123 Main street', 'office': '22 Baker Street', 'bill': '1 Financial Way'}

print(sample)
print(sample.keys())
print(sample.values())

print("\nAccess Item.\n")
print(sample['home'])
print(sample.get('home'))
print(sample.get('red'))

for key in sample.keys():
    print(key + " address is " + sample.get(key))

sample['home'] = "4321 lonesome range"
print(sample)
sample['vacation'] = "1 Sunshine Avenue"
print(sample)

print("\nFrom Blank\n")
blank = {}
blank["A"] = "Apple"
print(blank)
blank["B"] = "Banana"
print(blank)

print("\nDictionary items\n")
print(sample.items())

print("\nDictionary pop\n")
print(sample.pop('vacation'))
print(sample)

sample2 = sample.copy()

for item in sample.items():
    print("Next pair is " + str(item))

print("\nDictionary popitem\n")
print(sample.popitem())
print(sample)
print(sample.popitem())
print(sample)

sample.clear()
print(sample)

print(sample2)
if sample2['home']:
    print("That key exists")
if sample2.get('blue'):
    print("That key exists")
else:
    print("That key does not exist")

print(len(sample2))

print("\nApplication Ended.\n")