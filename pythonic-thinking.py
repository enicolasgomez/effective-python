#EFFECTIVE PYTHON: 90 SPECIFIC WAYS TO WRITE BETTER PYTHON

#Chapter 1: Pythonic Thinking

#Item 1: Know which py version you are using

import sys
print(sys.version_info)
print(sys.version)

#Item 3: know the differences between bytes and str

a3 = b'test'
print(list(a3))

#[116, 101, 115, 116]

a4 = 'test'
print(list(a4))

#['t', 'e', 's', 't']

print (list(b'test1' + b'test2'))

#file write argumens: w (string), wb (binary)

#Item 4 :  
# % formatting operator, C operators

a = 0b10111011
b = 0xc5f
print('Binary is %d, hex is %d' % (a, b))

#formating dictionaries

pantry = { 'avocados': 1.25,
 'bananas': 2.5,
 'cherries': 15,
}

#auto type

for key,value in pantry.items(): 
    new_way = '%(key)-10s = %(value).2f' % {
    'key': key, 'value': value} # Original

    print(new_way)

    reordered = '%(key)-10s = %(value).2f' % {
    'value': value, 'key': key} # Swapped

    print(reordered)

#template

name = 'Max'
template = '%s loves food. See %s cook.'
before = template % (name, name) # Tuple

#format built in / str.format 

#(, for thousands separators and ^ for centering) to
#format values:

a = 1234.5678
formatted = format(a, ',.2f')
print(formatted)
b = 'my string'
formatted = format(b, '^20s')
print('*', formatted, '*')

for key,value in pantry.items(): 
    formatted = '{1} = {0}'.format(key, value)
    print(formatted)

#Item 5: Write Helper functions instead of complex expressions

from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green=',
 keep_blank_values=True)

red = my_values.get('red', ['']) or 0
print(red)

red_str = my_values.get('red', [''])
red = int(red_str[0]) if red_str[0] else 0 #ternary operator 
print(red)

#Item 6: Prefer Multiple assignment un packing over indexing

item = ('Peanut butter', 'Jelly')
first, second = item # Unpacking
print(first, 'and', second)

#inline swap
# a[i-1], a[i] = a[i], a[i-1] # Swap

#Item 7: Prefer enumarte over range

#clumsy

flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']

for i in range(len(flavor_list)):
 flavor = flavor_list[i]
 print(f'{i + 1}: {flavor}')

it = enumerate(flavor_list)
print(next(it))
print(next(it))

for i, flavor in enumerate(flavor_list):
 print(f'{i + 1}: {flavor}')

#Item 8: Use zip to process itearators in parallel

names = ['Cecilia', 'Lise', 'Marie']
counts = [len(n) for n in names]
print(counts)

longest_name = None
max_count = 0

for i, name in enumerate(names):
 count = counts[i]
 if count > max_count:
  longest_name = name
  max_count = count

# The zip generator yields tuples containing 
# the next value from each iterator. These
# tuples can be unpacked directly within a for statement

for name, count in zip(names, counts):
 if count > max_count:
   longest_name = name
   max_count = count

#Item 9: avoid else blocks after for and while loops

for i in range(3):
 print('Loop', i)
else:
 print('Else block!')

 #Avoid using else blocks after loops because their behavior isn’t
#intuitive and can be confusing.

#Item 10: prevent repetition with assignment expressions

#Python 3.8 - warlus opeartor, assignment expression
# a := b 
# 'a warlus b'

# count = fresh_fruit.get('lemon', 0)
# if count:
#  make_lemonade(count)
# else:
#  out_of_stock()

 #warlus

# if count := fresh_fruit.get('lemon', 0):
#  make_lemonade(count)
# else:
#  out_of_stock()

