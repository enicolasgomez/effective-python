
# Item 37: Compose Classes Instead of Nesting Many Levels of Built-in Types

# Classic example in which understanding the auhtor's logic is more complicated than understanding the point.
# OOP solid principle: Single-responsibility Principle

# from collections import namedtuple
# Grade = namedtuple('Grade', ('score', 'weight'))

#✦ Avoid making dictionaries with values that are dictionaries, long
#    tuples, or complex nestings of other built-in types.
# ✦ Use namedtuple for lightweight, immutable data containers before
#    you need the flexibility of a full class.
# ✦ Move your bookkeeping code to using multtiple classes when your
#   internal state dictionaries get complicated.

# Item 38: Accept Functions Instead of Classes for Simple Interfaces

def startsWithS(word):
    return word[0] == 'S'

names = ['Socrates', 'Archimedes', 'Plato', 'Satiro', 'Aristotle']
names.sort(key=startsWithS)
print(names)

#function (as it's a first class member) hook to sort

#example, pass a function to defaultdic to count missing values using nonlocal
from collections import defaultdict

current = {'green': 12, 'blue': 3}
increments = [
 ('red', 5),
 ('blue', 17),
 ('orange', 9),
]

def increment_with_report(current, increments):
    added_count = 0
    def missing():
        nonlocal added_count # Stateful closure
        added_count += 1
        return 0
    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount
        return result, added_count

result, count = increment_with_report(current, increments)
assert count == 2

# Item 39: Use @classmethod Polymorphism to Construct Objects Generically

class InputData:
    def read(self):
        raise NotImplementedError

#I also have a concrete subclass of InputData that reads data from a
#file on disk:

class PathInputData(InputData):
    def __init__(self, path):
        super().__init__()
        self.path = path
    
    def read(self):
        with open(self.path) as f:
            return f.read()

# again, an example that overshoots the point

#@classmethod means: when this method is called, 
#we pass the class as the first argument instead of the instance of that class (as we normally do with methods). 
#This means you can use the class and its properties inside that method rather than a particular instance.

#@staticmethod means: when this method is called, 
#we don't pass an instance of the class to it (as we normally do with methods). 
#This means you can put a function inside a class but you can't access the instance of that class (this is useful when your method does not use the instance).

class Hero:

  @staticmethod
  def say_hello():
     print("Helllo...")

  @classmethod
  def say_class_hello(cls):
     if(cls.__name__=="HeroSon"):
        print("Hi Kido")
     elif(cls.__name__=="HeroDaughter"):
        print("Hi Princess")

class HeroSon(Hero):
  def say_son_hello(self):
     print("test  hello")

class HeroDaughter(Hero):
  def say_daughter_hello(self):
     print("test  hello daughter")


testson = HeroSon()
testson.say_class_hello() #Output: "Hi Kido"
testson.say_hello() #Outputs: "Helllo..."
testdaughter = HeroDaughter()
testdaughter.say_class_hello() #Outputs: "Hi Princess"
testdaughter.say_hello() #Outputs: "Helllo..."

# Item 40: Initialize Parent Classes with super

class Parent:
  def __init__(self, txt):
    self.message = txt

  def printmessage(self):
    print(self.message)

class Child(Parent):
  def __init__(self, txt):
    super().__init__(txt)

x = Child("Hello, and welcome!")
x.printmessage()

# ✦ Python’s standard method resolution order (MRO) solves the problems of superclass initialization order 
# and diamond inheritance.

# ✦ Use the super built-in function with zero arguments to initialize
# parent classes.

# Item 41: Consider Composing Functionality with Mix-in Classes
