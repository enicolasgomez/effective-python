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

