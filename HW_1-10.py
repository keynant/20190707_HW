sliceString1 = "123456789"
sliceString2 = "987654321"

# slice returns a slice of the string. takes either 1 or 3 params, either STOP or START, STOP(ends on stop-1) and STEP.
print(sliceString1[2:len(sliceString1) + 1:3])

# technically, the slice function returns a slice object that can be run on any string.
slcObj = slice(0, -1, 3)
print(sliceString1[slcObj])
print(sliceString2[slcObj])

# concatenation is string addition. returns a string.

a = "Keynan"
b = "Tenenbom"
print(b + ", " + a + " " + b + ".")

# List comprehension is a way to parametrically create lists, using a for loop and an optional condition.
# returns a list.
lst1 = [num for num in range(10)]
print(lst1)

import random

lst2 = [random.randint(0, 100) for i in range(50)]
print(lst2)

# optional if statement allows filtering of the results:

lst3 = [x for x in lst2 if x % 2 == 0]  # takes only the even numbers from previous list
print(lst3)

# A dictionary is an unordered collection of key-and-value pairs ('entries'. the keys can only be of immutable types
# (if not, an uncareful user might change a key by accident), and values can be of any type. The keys must be unique.

dict1 = {"key1": "value1", "key3": "value3", "key4": ("value3", 1)}
print(dict1)
print(dict1['key3'])  # accessing a specific value
print(dict1["key4"][0])  # accessing a specific value in list value

dict1['key5'] = "Bananana"  # creating a new entry
print(dict1)
dict1['key5'] = "Banana"  # if key exists, updates the key.
print(dict1)

print(dict1.items())  # all entries
print(dict1.keys())  # all keys
print(dict1.values())  # all values

a = dict1.pop('key4')  # removes a specified key - allows saving that key
print(f'removed entry: {a}')
del dict1['key3']  # deletes an entry (or whole dictionary if key not provided)
print(dict1)



