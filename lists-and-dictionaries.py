#CHAPTER 2: Lists and dictionaries

#Item 11: Know how to slice sequences

# list, str, and bytes built in
# any class implementing  __getitem__ and __setitem__
#somelist[start:end], where start is inclusive and end is exclusive

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('Middle two: ', a[3:5])
print('All but ends:', a[1:7])

#reduce visual noise (leave out start and final)

assert a[:5] == a[0:5]
assert a[5:] == a[5:len(a)]

#Using negative numbers for slicing is helpful for doing offsets relative
#to the end of a list

print(a[-3:-1])
# ['f', 'g']

# -n, if n > 1 is fine. If n = 0 resuls in [:]

# when used in assignments replaces elements in the original list

print('Before ', a)
a[2:7] = [99, 22, 14]
print('After ', a)

                   #************************
#Before  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
                   #**99, 22, 14************, h     
#After  ['a', 'b', 99, 22, 14, 'h']

print('Before ', a)
a[2:8] = [72,33]
print('After ', a)

#Before  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#After  ['a', 'b', 72, 33]

# Opposite effect for bigger elements

# Item 12: Avoid Striding and Slicing in a Single Expression

# somelist[start:end:stride]. This lets you take every nth item
# when slicing a sequence

x = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = x[::2]
evens = x[1::2]
print(odds)
print(evens)

#['red', 'yellow', 'blue']
#['orange', 'green', 'purple']

#Here, ::2 means “Select every second item starting at the beginning.”
#Trickier, ::-2 means “Select every second item starting at the end and
#moving backward.”
#What do you think 2::2 means? What about -2::-2 vs. -2:2:-2 vs.
#2:2:-2?

x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

x[2::2] # ['c', 'e', 'g']
x[-2::-2] # ['g', 'e', 'c', 'a']
x[-2:2:-2] # ['g', 'e']
x[2:2:-2] # []

# Item 13: Prefer catch all unpacking over slicing

# catch-all unpacking through a starred expression
#  This syntax allows one part
# of the unpacking assignment to receive all values that didn’t match
# any other part of the unpacking pattern

short_list = [1, 2]
first, second, *rest = short_list

print(first, second, rest)
# 1 2 []

short_list = [1, 2 ,3 , 4 , 5 , 6]
first, second, *rest = short_list

print(first, second, rest)
# 1 2 [3 , 4 , 5 , 6]

#to unpack assignments that contain a starred expression
#, you must have at least one required part

# Item 14: Sort by Complex Criteria Using the key parameter

numbers = [93, 86, 11, 68, 70]
numbers.sort()
print(numbers)

#[11, 68, 70, 86, 93]

class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def __repr__(self):
        return f'Tool({self.name!r}, {self.weight})'

tools = [
 Tool('level', 3.5),
 Tool('hammer', 1.25),
 Tool('screwdriver', 0.5),
 Tool('chisel', 0.25),
]

tools.sort(key=lambda x: x.weight)
print('By weight:', tools)

#first by weight and then by name.

tools.sort(key=lambda x: (x.weight, x.name))
print(tools)

#Item 15: Be Cautious When Relying on dict Insertion Ordering

# dict Python 3.5 > Random order. All methods too.

# **kwargs catch-all parameter (key, value), now keeps order

# __dict__ contains all the attributes which describe the object in question, now keeps order.

# if wrapper with SortedDict for creating a new list, oreder won't be preserved


# Item 16: Prefer get Over in and KeyError to Handle Missing Dictionary Keys

counters = {
 'pumpernickel': 2,
 'sourdough': 1,
}

key = 'sourdough'

# verbose
if key in counters:
 count = counters[key]
else:
 count = 0
counters[key] = count + 1

# key error

try:
 count = counters[key]
except KeyError:
 count = 0
counters[key] = count + 1

# dict API does exactly that

count = counters.get(key, 0)
counters[key] = count + 1

#setdefault The setdefault() method returns the value of the item with the specified key.
#If the key does not exist, insert the key, with the specified value,

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("chasis", "titanium")

print(car)
print(x)

# Item 17: Prefer defaultdict Over setdefault to
# Handle Missing Items in Internal State

visits = {
 'Mexico': {'Tulum', 'Puerto Vallarta'},
 'Japan': {'Hakone'},
}

visits.setdefault('France', set()).add('Arles') 

#defaultdict class from the collections built-in module
#simplifies this common use case by automatically storing a default
#value when a key doesn’t exist

from collections import defaultdict

visits = defaultdict(set)
visits['country123'].add('city123')
print(visits)

# Item 18: Know How to Construct Key-Dependent
# Default Values with __missing__

from collections import defaultdict

def open_picture(profile_path):
  try:
    return open(profile_path, 'a+b')
  except OSError:
    print(f'Failed to open path {profile_path}')
    raise

#  implement the __missing__ special method 
#  to add custom logic for handling missing keys

class Pictures(dict):
  def __missing__(self, key):
    value = open_picture(key)
    self[key] = value
    return value

pictures = {}
path = 'profile_1234.png'

pictures = Pictures()
handle = pictures[path]
handle.seek(0)
image_data = handle.read()