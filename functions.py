# Item 19: Never Unpack More Than Three Variables
# When Functions Return Multiple Values

def get_stats(numbers):
  minimum = min(numbers)
  maximum = max(numbers)
  return minimum, maximum

lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]

minimum, maximum = get_stats(lengths) # Two return values
print(f'Min: {minimum}, Max: {maximum}')

# more than 3, API consumers could swap values

# Item 20: Prefer Raising Exceptions to Returning None

# None is not False-equivalent

if not None:
  print('Invalid inputs') # This runs! But shouldn't

# better to rise Exception

def careful_divide(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs {$s}', e)

# Item 21: Know How Closures Interact with
# Variable Scope

#1. Py supports closures, variables within the scope they are defined
#2. Functions are first class objects, refer or pass
#3. Python has specific rules for comparing sequences (including
# tuples). It first compares items at index zero; then, if those are
# equal, it compares items at index one

def sort_priority2(numbers, group):
    found = False
    def helper(x):
        if x in group:
            found = True # Seems simple
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

# returns False
# If the variable doesn’t exist in the current scope, Python treats
# the assignment as a variable definition

# this behavior is the intended result: 
# It prevents local variables in a function from polluting the containing
# module. Otherwise, every assignment within a function would put
# garbage into the global module scope

# The nonlocal statement makes it clear when data is being assigned
# out of a closure and into another scope

def sort_priority3(numbers, group):
    found = False
    def helper(x):
        nonlocal found # Added
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

#   ✦ Closure functions can refer to variables from any of the scopes in
#   which they were defined.

#   ✦ By default, closures can’t affect enclosing scopes by assigning
#   variables.

#   ✦ Use the nonlocal statement to indicate when a closure can modify a
#   variable in its enclosing scopes.

#   ✦ Avoid using nonlocal statements for anything beyond simple
#   functions.

# Item 22: Reduce Visual Noise with Variable Positional Arguments

def log(message, values):

# if values is array, passing empty is noisy: log('test', [])
# using star args: log(message, *values), then 2nd argument is optional

#   ✦ Functions can accept a variable number of positional arguments by
#   using *args in the def statement.

#   ✦ You can use the items from a sequence as the positional arguments
#   for a function with the * operator.

#   ✦ Using the * operator with a generator may cause a program to run
#   out of memory and crash.

#   ✦ Adding new positional parameters to functions that accept *args
#   can introduce hard-to-detect bugs

# Item 23: Provide Optional Behavior with
# Keyword Arguments

#Positional arguments must be specified before keyword arguments:

def print_parameters(**kwargs):
 for key, value in kwargs.items():
 print(f'{key} = {value}')

print_parameters(alpha=1.5, beta=9, gamma=4)

#alpha = 1.5
#beta = 9
#gamma = 4

#The first benefit is that keyword arguments make the function call
# clearer to new readers of the code

#The second benefit of keyword arguments is that they can have
#default values specified in the function definition

# Item 24: Use None and Docstrings to Specify Dynamic Default Arguments

# A default argument value is evaluated only once per module, start up

def log(message, when=datetime.now()): #same value
 print(f'{when}: {message}')

def log(message, when=None):
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')

#  odd behaviors for dynamic values (like {}, [], or datetime.now()).

# Item 25: Enforce Clarity with Keyword-Only and Positional-Only Arguments

def safe_division(number, divisor,
 ignore_overflow,
 ignore_zero_division): #confusing for the two last arguments

 #Use keyword arguments

 def safe_division_b(number, divisor,
    ignore_overflow=False, # Changed
    ignore_zero_division=False): # Changed

#still unsafe

def safe_division_c(number, divisor, *, # Changed
 ignore_overflow=False,
 ignore_zero_division=False):

# The * symbol in the argument list indicates the end
# of positional arguments and the beginning of keyword-only
# arguments

# Item 26: Define Function Decorators with
# functools.wraps

# A decorator has the ability to run additional code before
# and after each call to a function it wraps


# ✦ Decorators in Python are syntax to allow one function to modify
# another function at runtime.
# ✦ Using decorators can cause strange behaviors in tools that do introspection, such as debuggers.
# ✦ Use the wraps decorator from the functools built-in module when
# you define your own decorators to avoid issues.