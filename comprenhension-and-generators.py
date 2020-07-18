#Item 27: Use Comprehensions Instead of map and filter

# Comprenhension (iterable to list)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in a] # List comprehension

even_squares = [x**2 for x in a if x % 2 == 0]

#same with map and filter

alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))

assert even_squares == list(alt)

# Item 28: Avoid More Than Two Control Subexpressions in Comprehensions

my_lists = [
 [[1, 2, 3], [4, 5, 6]],
]

flat = [x for sublist1 in my_lists
 for sublist2 in sublist1
 for x in sublist2]

 # better

flat = []
for sublist1 in my_lists:
 for sublist2 in sublist1:
 flat.extend(sublist2)

# Item 29: Avoid Repeated Work in Comprehensions by Using Assignment Expressions

#  ✦ Assignment expressions make it possible for comprehensions and
#  generator expressions to reuse the value from one condition elsewhere in the same comprehension, which can improve readability
#  and performance.

#  ✦ Although it’s possible to use an assignment expression outside of
#  a comprehension or generator expression’s condition, you should
#  avoid doing so.

# Item 30: Consider Generators Instead of Returning Lists

def read_csv(file_name):
    for row in open(file_name, "r"):
        yield row

# By introducing the keyword yield, 
# we’ve essentially turned the function into a generator function. 
# This new version of our code opens a file, loops through each line, 
# and yields each row.

def index_words_iter(text):
 if text:
 yield 0
 for index, letter in enumerate(text):
 if letter == ' ':
 yield index + 1
 
# When called, a generator function does not actually run but instead
# immediately returns an iterator. With each call to the next built-in
# function, the iterator advances the generator to its next yield expression. 
# Each value passed to yield by the generator is returned by the
# iterator to the caller:

it = index_words_iter(address)
print(next(it))
print(next(it))

# ✦ Using generators can be clearer than the alternative of having a
# function return a list of accumulated results.

# ✦ The iterator returned by a generator produces the set of values
# passed to yield expressions within the generator function’s body.

# ✦ Generators can produce a sequence of outputs for arbitrarily large
# inputs because their working memory doesn’t include all inputs and
# outputs.

# Item 31: Be Defensive When Iterating Over Arguments

# normalization problem ( percentage from total)

def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
    percent = 100 * value / total
    result.append(percent)
    return result

# say that values come from a generator

def read_visits(data_path):
    with open(data_path) as f:
    for line in f:
    yield int(line)

# calling 

it = read_visits('my_numbers.txt')
percentages = normalize(it)
print(percentages)

#[] never calls iterator next before normalizing

#alternatives

# 1. numbers_copy = list(numbers) # copy iterator, works but could be extremely large
# 2. percentages = normalize_func(lambda: read_visits(path)) # pass a lambda expression, difficult to read
# 3. implementing the __iter__ (iterator protocol)

class ReadVisits:
 def __init__(self, data_path):
    self.data_path = data_path
 def __iter__(self):
    with open(self.data_path) as f:
        for line in f:
            yield int(line)

visits = ReadVisits(path)
percentages = normalize(visits)
print(percentages)
assert sum(percentages) == 100.0

# defensive check: if isinstance(numbers, Iterator):

# Item 32: Consider Generator Expressions for Large List Comprehensions

# read a file and return the number of
# characters on each line. Doing this with a list comprehension would
# require holding the length of every line of the file in memory

# big file or stream : problem

value = [len(x) for x in open('my_file.txt')]
print(value)

# solution: generator expression 

it = (len(x) for x in open('my_file.txt'))
print(next(it))

# generator expression composition

roots = ((x, x**0.5) for x in it)

# Item 33: Compose Multiple Generators with yield from
# animation using combined generators

#noisy approach 

def animate():
 for delta in move(4, 5.0):
    yield delta
 for delta in pause(3):
    yield delta
 for delta in move(2, 3.0):
    yield delta

def render(delta):
 print(f'Delta: {delta:.1f}')
 # Move the images onscreen
def run(func):
 for delta in func()

#better approach 

def animate_composed():
    yield from move(4, 5.0)
    yield from pause(3)
    yield from move(2, 3.0)

# Item 34: Avoid Injecting Data into Generators with send

# Python generators support the send method, which upgrades yield
# expressions into a two-way channel. The send method can be used to
# provide streaming inputs to a generator at the same time it’s yielding
# outputs.

# SIN(X) function plus step

def wave_modulating(steps):
    step_size = 2 * math.pi / steps
    amplitude = yield # Receive initial amplitude
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        amplitude = yield output # Receive next amplitude

def run_modulating(it):
    amplitudes = [None, 7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]
    for amplitude in amplitudes:
        output = it.send(amplitude)
        transmit(output)

run_modulating(wave_modulating(12))

#hard to read but works

# ✦ The send method can be used to inject data into a generator by giving the yield expression 
# a value that can be assigned to a variable.
# ✦ Using send with yield from expressions may cause surprising behavior, 
# such as None values appearing at unexpected times in the generator output.
# ✦ Providing an input iterator to a set of composed generators is a better approach than using the send method, 
# which should be avoided.

# Item 35 and 36 : TODO